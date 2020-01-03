import functools
import threading
from http import HTTPStatus
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler


__STYLE__ = r'''
a, abbr, acronym, address, applet, article, aside, audio, b, big, blockquote, body, canvas, caption, center, cite, code,
dd, del, details, dfn, div, dl, dt, em, embed, fieldset, figcaption, figure, footer, form, h1, h2, h3, h4, h5, h6, 
header, hgroup, html, i, iframe, img, ins, kbd, label, legend, li, mark, menu, nav, object, ol, output, p, pre, q, ruby,
s, samp, section, small, span, strike, strong, sub, summary, sup, table, tbody, td, tfoot, th, thead, time, tr, tt, u, 
ul, var, video {
    margin: 0;
    padding: 0;
    border: 0;
    font-size: 100%;
    font: inherit;
    vertical-align: baseline;
}
article, aside, details, figcaption, figure, footer, header, hgroup, menu, nav, section {
    display: block;
}
body {
    font-size: 1.5em;
    line-height: 2rem;
    font-weight: 400;
    font-family: "Helvetica Neue", HelveticaNeue, Helvetica, Arial, sans-serif;
    color: #222;
    height: 100%;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
ol, ul {
    list-style: none;
}
blockquote, q {
    quotes: none;
}
blockquote:after, blockquote:before, q:after, q:before {
    content: '';
    content: none;
}
table {
    border-collapse: collapse;
    border-spacing: 0;
}
.container {
    position: relative;
    font-size: 32px;
    min-height: 100vh;
    width: 100%;
    height: 100%;
    padding: 1rem;
    display: flex;
    background-color: #e1e1e1;
    flex-flow: row wrap;
    text-align: center;
    box-sizing: border-box;
}
.container .item {
    position: relative;
    display: inline-block;
    flex: 1 1 auto;
    padding: 1rem;
    margin: 1rem;
    text-align: center;
    background-color: #fafafa;
    border: 3px solid transparent;
}
.container .item .preview {
    padding: 1.5rem 6.5rem;
    line-height: 1.4em;
    font-size: 2.827em;
}
.container .item .fontName {
    font-size: .85rem;
    color: #bfbfbf;
    letter-spacing: .5px;
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
    <div class="container">
        {font_previews}
    </div>
</body>
</html>
'''

__PREVIEW_BLOCK_TEMPLATE__ = r'''
<div class="item">
    <p class="preview" style="font-family: '{family}'">{char}</p>
    <p class="fontName">{family}</p>
</div>
'''


class FontPreviewRequestHandler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def __init__(self, *args, preview_html_content=None, **kwargs):
        self._preview_html_content = preview_html_content.encode('utf8')
        self._content_length = str(len(self._preview_html_content))
        super().__init__(*args, **kwargs)

    # noinspection PyPep8Naming
    def do_GET(self):
        if self.path != '/':
            return
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', self._content_length)
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
