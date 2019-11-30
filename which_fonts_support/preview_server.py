import functools
import threading
from http import HTTPStatus
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler


__STYLE__ = r'''
div {
    display: inline-block;
    text-align: center;
    padding-left: 1em;
    padding-right: 1em;
    margin-top: 1em;
    border: 2px solid black;
}
p.preview {
    font-size: 5em;
    margin-top: 0;
    margin-bottom: 0;
    padding-bottom: 0;
    padding-top: 0;
}
'''

__HTML_TEMPLATE__ = r'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Font preview</title>
    <style>
        {style}
    </style>
</head>
<body>
    {font_previews}
</body>
</html>
'''

__PREVIEW_BLOCK_TEMPLATE__ = r'''
<div>
    <p class="preview" style="font-family: '{family}'">{char}</p>
    <p class="fontName">{family}</p>
</div>
'''


class FontPreviewRequestHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def __init__(self, *args, preview_html_content=None, **kwargs):
        self._preview_html_content = preview_html_content.encode('utf8')
        super().__init__(*args, **kwargs)

    # noinspection PyPep8Naming
    def do_GET(self):
        if self.path != '/':
            return
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', str(len(self._preview_html_content)))
        self.send_header('X-Content-Type-Options', 'nosniff')
        self.end_headers()
        self.wfile.write(self._preview_html_content)

    def log_request(self, code='-', size='-'):
        pass


class FontPreviewServer:
    def __init__(self, char):
        self._char = char
        self._families = []
        self._server = self._thread = self._port = None

    def add_font(self, family):
        self._families.append(family)

    def start(self):
        assert self._server is None
        font_previews = []
        for family in self._families:
            font_previews.append(__PREVIEW_BLOCK_TEMPLATE__.format(
                family=family,
                char=self._char
            ))
        html = __HTML_TEMPLATE__.format(
            style=__STYLE__,
            font_previews='\n'.join(font_previews),
        )
        self._server = ThreadingHTTPServer(
            ('localhost', 0),
            functools.partial(FontPreviewRequestHandler, preview_html_content=html))
        self._port = self._server.socket.getsockname()[1]
        self._thread = threading.Thread(target=self._server.serve_forever)
        self._thread.start()

    def stop(self):
        assert self._server is not None
        self._server.shutdown()
        self._thread.join()

        self._server = self._thread = self._port = None

    @property
    def port(self):
        return self._port
