#!/usr/bin/env python

## Convert most syntax production rules into the proper format

import sys
import regex as re

with open(sys.argv[1]) as f:
    lines = f.readlines()
           
nonterminals = {}

# One pass to collect all the nonterminals
lno = 0
while lno < len(lines):
    if lines[lno] == '      .. container:: syntax-definition\n':
        tmp = [lines[lno]]
        lno += 1
        while lines[lno] != '         .. container:: syntax-nonterminal\n':
            tmp.append(lines[lno])
            lno += 1
        tmp.append(lines[lno])
        lno += 1
        while re.match(r'^\s*$', lines[lno]):
            tmp.append(lines[lno])
            lno += 1
        nt = re.match(r'^\s*(\S+)$', lines[lno]).group(1)
        while True:
            tmp.append(lines[lno])
            lno += 1
            if re.match(r'^\s*$', lines[lno]):
                continue
            if re.match(r'^      ', lines[lno]):
                continue
            break
        nonterminals[nt] = tmp
    else:
        lno += 1

newlines = []

# Second pass to replace all production rules
lno = 0
while lines[lno] != 'Annex A\n':
    newlines.append(lines[lno])
    lno += 1

while lines[lno] != 'Annex B\n':
    start = re.match(r'(\(:ref:`[^`]+`\)) ([^:]+):.*', lines[lno])
    if not start:
        newlines.append(lines[lno])
        lno += 1
        continue
    
    nt = start.group(2)
    assert(nt in nonterminals.keys())
    newlines.append(start.group(1) + '\n')
    lno += 1

    while lines[lno] != '.. code-block:: text\n' and lines[lno] != '::\n':
        lno += 1
    lno += 1

    while re.match(r'^\s*$', lines[lno]):
        lno += 1

    spc = re.match(r'^\s*', lines[lno])
    spc = spc.group(0)
    if len(spc) != 0:
        indent = len(spc)
        lno += 1
        while re.match(r'^\s*$', lines[lno]) or re.match(r'^' + spc, lines[lno]):
            lno += 1

    newlines.append("\n")
    newlines.append(".. container:: syntax-block\n")
    newlines.append("\n")
    newlines.append("   .. container:: syntax-production\n")
    newlines.append("\n")
    newlines += nonterminals[start.group(2)]

newlines += lines[lno:]

print(''.join(newlines), end='')
