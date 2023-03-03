#!/usr/bin/env python3

import sys,os
import regex as re

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

cb = []

indent = -1
for lno in range(len(lines)):
    line = lines[lno]

    # skip whitespace only lines
    if re.match(r"^\s*$", line):
        continue

    # start of codeblock
    if line == "::\n" or line == ".. code-block:: text\n":
       indent = 0
       continue
    
    # skip if not in a codeblock
    if indent == -1:
        continue

    space = re.match(r"^\s*", line)
    space = space.group(0)

    # NO indent on this line -> not a codeblock!
    if len(space) == 0:
        indent = -1
        continue
    
    cb.append(line)

    # if indent == 0, this is the first indented line
    if indent == 0:
        indent = len(space)

    # Unindented line
    if len(space) < indent:
        indent = -1
        continue
    
    lines[lno] = line[indent - 4:]

print(''.join(lines), end="")
