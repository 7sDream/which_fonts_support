#!/usr/bin/env python3

# MIT License

# Copyright (c) 2017 7sDream

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

import sys, re, subprocess

char = ''
if len(sys.argv) > 1:
    char = sys.argv[1]
if len(char) == 0:
    char = input('Input only one char: ')
if len(char) != 1:
    if char == '-h' or char == '--help':
        print(f'Usage: {sys.argv[0]} char')
        exit(0)
    if len(char) == 0:
        sys.stderr.write('Please input one char\n')
    elif len(char) > 1:
        sys.stderr.write('Please only input one char\n')
    exit(1)

codepoint = ord(char) # 2A20
codepoint_base = (codepoint & 0xFFFF00) >> 8
codepoint_tail = codepoint & 0x0000FF
codepoint_str = hex(codepoint)[2:].rjust(6, '0')
codepoint_base_str = hex(codepoint_base)[2:].rjust(4, '0')
codepoint_tail_str = hex(codepoint_tail)[2:].rjust(2, '0')

# fc-list format is each line 8 block, 3 bit, so rshift 5 bit to get the index
block_index = codepoint_tail >> 5
# get last five bit because each block has 32 char
pos_in_block = codepoint_tail & 0b11111
# start from left, so lshift to the pos
pos_mask = 1 << (32 - pos_in_block - 1)

result = subprocess.run(['fc-list', '-v'], stdout=subprocess.PIPE)
if result.returncode != 0:
    sys.stderr.write('run fc-list -v failed, please check your environment\n')
    exit(2)

descriptions = result.stdout.decode('utf-8').split('\n')


fonts = set()
last_font = ""
for line in descriptions:
    if 'family:' in line:
        last_font = line
    elif (codepoint_base_str + ':') in line:
        charset = line[line.rfind(':')+2:]
        blocks = [int(x,16) for x in charset.split(' ')]
        number = blocks[block_index]
        supported = number & pos_mask

        if supported:
            font_name = re.search(r'\"([^"]+)\"', last_font).group(1)
            if font_name not in fonts:
                fonts.add(font_name)

for font in sorted(list(fonts)):
    print(font)
