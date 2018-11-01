#!/usr/bin/env python3

# MIT License

# Copyright (c) 2017-2018 7sDream

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import sys, re, subprocess, binascii, collections, argparse, tempfile

import wcwidth

__version__ = '1.1.0'

__all__ = ['available_font_for_codepoint']

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
    <p>
        {font_previews}
    </p>
</body>
</html>
'''

__PREVIEW_BLOCK_TEMPLATE__ = r'''
<div>
    <p class="preview" style="font-family: '{font_name}'">{char}</p>
    <p class="fontName">{font_name}</p>
</div>
'''

def __parser_arg():
    parser = argparse.ArgumentParser(
        description='Find which fonts support specified character',
        epilog='Github: https://github.com/7sDream/which_fonts_support',
    )
    parser.add_argument('char', default='')
    parser.add_argument('-v', '--version', action='version', version=__version__)
    parser.add_argument(
        '-p', '--preview', action='store_true',
        help='show font preview for the char in browser',
    )

    return parser.parse_args()

def __get_char_codepoint(char):
    assert len(char) == 1

    codepoint = ord(char)

    return {
        'decimal': codepoint, 
        'hex': hex(codepoint)[2:].rjust(6, '0'), 
        'utf8': binascii.hexlify(char.encode('utf8')).decode("ascii"),
    }

def available_font_for_codepoint(codepoint):
    assert 0 < codepoint < 0x10FFFF

    codepoint_base = codepoint >> 8
    codepoint_tail = codepoint & 0xFF
    codepoint_base_str = hex(codepoint_base)[2:].rjust(4, '0')

    # fc-list format is each line 8 block, 3 bit, so rshift 5 bit to get the index
    block_index = codepoint_tail >> 5
    # get last five bit because each block has 32 char
    pos_in_block = codepoint_tail & 0b11111
    # start from left, so lshift to the pos
    pos_mask = 1 << (32 - pos_in_block - 1)

    result = subprocess.run(['fc-list', '-v'], stdout=subprocess.PIPE)
    if result.returncode != 0:
        raise RuntimeError(
            'run fc-list failed, please check your environment\n'
        )

    descriptions = result.stdout.decode('utf-8').split('\n')

    last_font = ''
    for line in descriptions:
        if 'family:' in line:
            last_font = line
        elif (codepoint_base_str + ':') in line:
            charset = line[line.rfind(':')+2:]
            blocks = [int(x,16) for x in charset.split(' ')]
            number = blocks[block_index]
            supported = number & pos_mask

            if supported:
                font_name = iter(collections.deque(
                    map(
                        lambda x: x.group(1), 
                        re.finditer(r'"([^"]+)"', last_font)
                    ),
                    maxlen=1
                ))
                yield from font_name

def __main():
    args = __parser_arg()

    if len(args.char) == 0:
        args.char = input('Input one character: ')
    if len(args.char) != 1:
        sys.stderr.write('Please provide ONE character')
        exit(1)

    cp = __get_char_codepoint(args.char)
    codepoint = cp['decimal']
    codepoint_hex_str = cp['hex']
    codepoint_utf8_seq = cp['utf8']

    print(
        f'Font(s) support the char [ {args.char} ]' +
        f'({codepoint}, U+{codepoint_hex_str}, {codepoint_utf8_seq}):'
    )

    fonts = collections.Counter(available_font_for_codepoint(codepoint))
    typefaces = sorted(fonts)
    max_width = max(map(wcwidth.wcswidth, typefaces))

    font_previews = []

    for typeface in typefaces:
        style_amount = fonts[typeface]
        print(
            typeface, ' ' * (max_width - wcwidth.wcswidth(typeface)),
            f' with {style_amount} style{"s" if style_amount > 1 else ""}',
            sep=''
        )
        font_previews.append(__PREVIEW_BLOCK_TEMPLATE__.format(
            font_name=typeface,
            char=args.char,
        ))
    
    if args.preview:
        html = __HTML_TEMPLATE__.format(
            style=__STYLE__,
            font_previews='\n'.join(font_previews),
        )
        f = tempfile.NamedTemporaryFile(suffix='.html', delete=False)
        f.write(html.encode('utf-8'))
        subprocess.Popen(['open', f.name])

if __name__ == '__main__':
    __main()
