#!/bin/bash

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

CHAR=$1

while [ ${#CHAR} -ne 1 ]; do
    read -n 1 -p "Input only one char:" CHAR
    echo .
done

ORD=`python3 -c "print(hex(ord('${CHAR}'))[2:].rjust(6, '0'))"`

BASE=${ORD:0:4}

IFS=$'\n' read -r -d '' -a FONTS <<< `fc-list -v | grep -P "${BASE}:|family:" | sed -n -r "N; s/\n//; s/\t*(family[^\t]*?)\t*(${BASE}: .*)/\1 \2/; /family.*${BASE}/p; d;"`

echo "Font list support char [ ${CHAR} ](${ORD}): "

for FONT in "${FONTS[@]}"; do
    python3 -c "import sys,re;f,c=sys.argv[1:];s=f[f.rfind(':')+2:];r=[int(x,16) for x in s.split(' ')][(ord(c)&0xff)//32]&(1<<(ord(c)&0xff%32));print(''.join(map(lambda x:x.ljust(30),re.findall(r'\"(.*?)\"',f)))+'\n' if r != 0 else '',end='')" "${FONT}" "${CHAR}"
done
