import argparse
import binascii
import collections
import re
import sys
import webbrowser

import wcwidth

from .main import available_fonts_for_codepoint
from .preview_server import FontPreviewServer

__RE_GET_NAME__ = re.compile(r'"\.?([^"]+)"')
__RE_UNICODE_HEX__ = re.compile(r'^U\+[0-9a-fA-F]{4,6}$')


def parser_arg():
    from . import __version__

    parser = argparse.ArgumentParser(
        prog="which_fonts_support",
        description='Find which fonts support specified character',
        epilog='Github: https://github.com/7sDream/which_fonts_support',
    )
    parser.add_argument(
        'char', default='',
        help='the character, if you want to check character not in BMP, ' +
             'use U+XXXX or U+XXXXXX format.'
    )
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument(
        '-f', '--fc-list', type=str, default='fc-list', metavar='PATH',
        help='provide custom fc-list executable file path',
    )
    parser.add_argument(
        '-v', '--verbose', action='store_true',
        help='show each style full name',
    )
    parser.add_argument(
        '-p', '--preview', action='store_true',
        help='show font preview for the char in browser',
    )

    return parser.parse_args()


def get_char_codepoint(c):
    assert len(c) == 1

    codepoint = ord(c)

    return {
        'decimal': codepoint,
        'hex': hex(codepoint)[2:].rjust(6, '0'),
        'utf8': binascii.hexlify(c.encode('utf8')).decode("ascii"),
    }


def cli():
    args = parser_arg()

    if __RE_UNICODE_HEX__.match(args.char):
        args.char = chr(int(args.char[2:], 16))

    if len(args.char) == 0:
        args.char = input('Input one character: ')
    if len(args.char) != 1:
        sys.stderr.write('Please provide ONE character')
        exit(1)

    cp = get_char_codepoint(args.char)
    codepoint = cp['decimal']
    codepoint_hex_str = cp['hex']
    codepoint_utf8_seq = cp['utf8']

    fullname_to_family_map = {
        fullname: family for family, fullname in available_fonts_for_codepoint(codepoint, args.fc_list)
    }

    family_to_fullname_list_map = collections.defaultdict(list)
    for fullname, family in fullname_to_family_map.items():
        family_to_fullname_list_map[family].append(fullname)

    if len(fullname_to_family_map) == 0:
        print("No fonts support this character")
        exit(0)

    family_style_counts = collections.Counter(fullname_to_family_map.values())
    families = sorted(family_style_counts)

    max_width = max(map(wcwidth.wcswidth, families)) if not args.verbose else 0

    print(
        f'Font(s) support the char [ {args.char} ]' +
        f'({codepoint}, U+{codepoint_hex_str}, {codepoint_utf8_seq}):'
    )

    font_preview_server = FontPreviewServer(args.char)

    for family in families:
        style_count = family_style_counts[family]
        print(
            family,
            ' ' * (max_width - wcwidth.wcswidth(family))
            if not args.verbose else '',
            f' with {style_count} style{"s" if style_count > 1 else ""}'
            if not args.verbose else '',
            sep=''
        )
        if style_count > 1 and args.verbose:
            for fullname in sorted(family_to_fullname_list_map[family]):
                print(' ' * 4, fullname, sep='')
        font_preview_server.add_font(family)

    if args.preview:
        font_preview_server.start()
        print('-' * 80)
        print("Opening your browser for preview...")

        webbrowser.open("http://localhost:" + str(font_preview_server.port) + '/')

        input("Press Enter when you finish preview...")

        font_preview_server.stop()
