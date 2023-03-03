#!/usr/bin/env python

## Convert most syntax production rules into the proper format

import sys
import re

with open(sys.argv[1]) as f:
    lines = f.readlines()

class ProductionRule(object):

    def __init__(self, nonterminal, one_of=False):
        self.nt = nonterminal
        self.of = one_of
        self.rules = []

    def addRule(self, rule):
        self.rules.append(rule.strip())

    def to_string(self, nonterminal_list=[]):
        str = (  '\n.. container:: syntax-production'+
               '\n\n   .. container:: syntax-definition'
               '\n\n      .. container:: syntax-nonterminal'+
               '\n\n         ' + self.nt +
               '\n\n      :')
        if self.of:
            str += ' one of'
        if self.of:
            minwidth = 0
            for rule in self.rules:
                for word in rule.split():
                    minwidth = max(len(word), minwidth)
            for rule in self.rules:
                str += '\n\n   .. container:: syntax-rule'
                for word in rule.split():
                    str += ('\n\n      .. container:: syntax-terminal' +
                            '\n\n         ' + word)
            return str
        else:
            for rule in self.rules:
                str += '\n\n   .. container:: syntax-rule'
                post = []
                parts = rule.split()    
                for part in parts:
                    if part.endswith('opt'):
                        part = part[:-3]
                        opt = True
                    else:
                        opt = False
                    if part in nonterminal_list or part == self.nt:
                        post.append('\n\n      .. container:: syntax-nonterminal'+
                                    '\n\n         ' + part + '\n')
                    else:
                        post.append('\n\n      .. container:: syntax-terminal'+
                                    '\n\n         ' + part + '\n')
                    if opt:
                        post[-1] += ('\n\n         .. container:: syntax-opt'+
                                     '\n\n            :sub:`opt`\n')
                str += '\n    ' + '  '.join(post)
        return str
           
            

nonterminals = []

# One pass to collect all the nonterminals
lno = 0
while lno < len(lines):
    if lines[lno] == '**Syntax**\n':
        while lines[lno] != '.. code-block:: text\n':
            lno += 1
        lno += 1
        while lines[lno].strip() == '' or lines[lno].startswith('    '): 
            if lines[lno].strip() == '':
                lno += 1
                continue
            m = re.match('^\s*([a-z-]+):( one of)?', lines[lno])
            if m:
                nonterminals.append(m.group(1))
            lno += 1
    lno += 1

# Second pass to replace all production rules
lno = 0
while lno < len(lines):
    while lines[lno] != '**Syntax**\n':
        print(lines[lno], end='')
        lno += 1
        if not lno < len(lines):
            break
    if not lno < len(lines):
        break
    while lines[lno] != '.. code-block:: text\n':
        print(lines[lno], end='')
        lno += 1
        if not lno < len(lines):
            break
    if not lno < len(lines):
        break
    print('.. container:: syntax-block\n')
    lno += 1
    if not lno < len(lines):
        break
    prs = []
    while lines[lno].strip() == '' or lines[lno].startswith('    ') and lno:
        if lines[lno].strip() == '':
            lno += 1
            continue
        m = re.match('^\s*([A-Za-z-]+):( one of)?', lines[lno])
        if m:
            prs.append(ProductionRule(m.group(1), m.group(2)))
        else:
            prs[-1].addRule(lines[lno].replace('\\', '\\\\').replace('*', '\\*').replace('%', '\\%').replace('|', '\\|'))
        lno += 1
        if not lno < len(lines):
            break
    for pr in prs:
        print('\n'.join(['   ' + line for line in pr.to_string(nonterminals).splitlines()]))
    print()
lno += 1
