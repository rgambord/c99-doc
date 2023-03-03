#!/usr/bin/env python3

import sys,os
import regex as re

with open(sys.argv[1], "r") as f:
    lines = f.readlines()

section_levels = []
snum=[]

sections=[{'section': [0], 'lines':[], 'footnotes':[]}]
footnotes = {}


lno=0
while lno + 3 < len(lines):
    if lines[lno] == ".. rubric:: Footnotes\n":
        lno += 1
        continue

    fn = re.match(r"^\.\. \[#([^\]]+)\] (.*)", lines[lno])
    if fn:
        assert(fn.group(1) not in footnotes.keys())
        footnotes[fn.group(1)] = fn.group(2)
        lno += 1
        continue

    fnrefs = re.findall(r"\[#([^\]]+)\]", lines[lno])
    for fnref in fnrefs:
        if fnref not in sections[-1]['footnotes']:
            sections[-1]['footnotes'].append(fnref)

    # Section is blank + #.#... title + punctuation
    ref = re.match(r"^.. _.*:$", lines[lno])
    pblank = True if lno == 0 else re.match(r"^\s*$", lines[lno+1])
    sect = re.match(r"[^\s]+", lines[lno+2])
    npunct = False if lno == len(lines) - 1 else re.match(r"([[:punct:]])\1*$", lines[lno+3])

    if ref and pblank and npunct and sect:
        if npunct.group(1) not in section_levels:
            section_levels.append(npunct.group(1))
        depth = section_levels.index(npunct.group(1)) + 1
        snum = snum[:depth] + [0]*(depth - len(snum))
        snum[-1] += 1
        lines[lno+3] = section_levels[depth-1] * (len(lines[lno+2]) - 1) + '\n'
        sections.append({'section': list(snum), 'lines':[], 'footnotes':[]})

    sections[-1]['lines'].append(lines[lno])
                    
    lno += 1


for sno in range(1, len(sections)):
    section = sections[sno]
    dir = 'split/' + '/'.join([str(n) for n in section['section']])
    os.makedirs(dir, exist_ok=True)
    with open(dir + '/index.rst', "w+") as f:
        f.writelines(section['lines'][:4])
        if sno + 1 < len(sections):
            next_section = sections[sno+1]
            if len(section['section']) < len(next_section['section']):
                f.write("""

.. toctree::
   :maxdepth: 2

""")
                for subsec in sections[sno+1:]:
                    if len(subsec['section']) <= len(section['section']):
                        f.write("\n")
                        break
                    if len(subsec['section']) == len(section['section']) + 1:
                        f.write("   " + str(subsec['section'][-1]) + "/index\n")

        f.writelines(section['lines'][4:])
        if section['footnotes']:
            f.write("""

.. rubric:: Footnotes

""")
            for fn in section['footnotes']:
                f.write(".. [#" + fn + "] " + footnotes[fn] + "\n")

