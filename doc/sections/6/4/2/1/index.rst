.. _9899_general-1:

6.4.2.1 General
'''''''''''''''

.. rubric:: Syntax

.. _9899_6.4.2.1p1:

:ref:`1 <9899_6.4.2.1p1>`

.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            identifier
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            identifier-nondigit
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            identifier
     
   
         .. container:: syntax-nonterminal
   
            identifier-nondigit
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            identifier
     
   
         .. container:: syntax-nonterminal
   
            digit
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            identifier-nondigit
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            nondigit
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            universal-character-name
   
   
      .. container:: syntax-rule

         other implementation-defined characters
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            nondigit
   
         : one of
   
      .. container:: syntax-rule-tbl
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               _
      
            .. container:: syntax-terminal
      
               a
      
            .. container:: syntax-terminal
      
               b
      
            .. container:: syntax-terminal
      
               c
      
            .. container:: syntax-terminal
      
               d
      
            .. container:: syntax-terminal
      
               e
      
            .. container:: syntax-terminal
      
               f
      
            .. container:: syntax-terminal
      
               g
      
            .. container:: syntax-terminal
      
               h
      
            .. container:: syntax-terminal
      
               i
      
            .. container:: syntax-terminal
      
               j
      
            .. container:: syntax-terminal
      
               k
      
            .. container:: syntax-terminal
      
               l
      
            .. container:: syntax-terminal
      
               m
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               n
      
            .. container:: syntax-terminal
      
               o
      
            .. container:: syntax-terminal
      
               p
      
            .. container:: syntax-terminal
      
               q
      
            .. container:: syntax-terminal
      
               r
      
            .. container:: syntax-terminal
      
               s
      
            .. container:: syntax-terminal
      
               t
      
            .. container:: syntax-terminal
      
               u
      
            .. container:: syntax-terminal
      
               v
      
            .. container:: syntax-terminal
      
               w
      
            .. container:: syntax-terminal
      
               x
      
            .. container:: syntax-terminal
      
               y
      
            .. container:: syntax-terminal
      
               z
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               A
      
            .. container:: syntax-terminal
      
               B
      
            .. container:: syntax-terminal
      
               C
      
            .. container:: syntax-terminal
      
               D
      
            .. container:: syntax-terminal
      
               E
      
            .. container:: syntax-terminal
      
               F
      
            .. container:: syntax-terminal
      
               G
      
            .. container:: syntax-terminal
      
               H
      
            .. container:: syntax-terminal
      
               I
      
            .. container:: syntax-terminal
      
               J
      
            .. container:: syntax-terminal
      
               K
      
            .. container:: syntax-terminal
      
               L
      
            .. container:: syntax-terminal
      
               M
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               N
      
            .. container:: syntax-terminal
      
               O
      
            .. container:: syntax-terminal
      
               P
      
            .. container:: syntax-terminal
      
               Q
      
            .. container:: syntax-terminal
      
               R
      
            .. container:: syntax-terminal
      
               S
      
            .. container:: syntax-terminal
      
               T
      
            .. container:: syntax-terminal
      
               U
      
            .. container:: syntax-terminal
      
               V
      
            .. container:: syntax-terminal
      
               W
      
            .. container:: syntax-terminal
      
               X
      
            .. container:: syntax-terminal
      
               Y
      
            .. container:: syntax-terminal
      
               Z
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            digit
   
         : one of
   
      .. container:: syntax-rule-tbl
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               0
      
            .. container:: syntax-terminal
      
               1
      
            .. container:: syntax-terminal
      
               2
      
            .. container:: syntax-terminal
      
               3
      
            .. container:: syntax-terminal
      
               4
      
            .. container:: syntax-terminal
      
               5
      
            .. container:: syntax-terminal
      
               6
      
            .. container:: syntax-terminal
      
               7
      
            .. container:: syntax-terminal
      
               8
      
            .. container:: syntax-terminal
      
               9

.. rubric:: Semantics

.. _9899_6.4.2.1p2:

:ref:`2 <9899_6.4.2.1p2>` An identifier is a sequence of nondigit characters (including the underscore \_, the lowercase and uppercase Latin letters, and other characters) and digits, which designates one or more entities as described in :ref:`6.2.1 <9899_6.2.1>`. Lowercase and uppercase letters are distinct. There is no specific limit on the maximum length of an identifier.

.. _9899_6.4.2.1p3:

:ref:`3 <9899_6.4.2.1p3>` Each universal character name in an identifier shall designate a character whose encoding in ISO/IEC 10646 falls into one of the ranges specified in :ref:`annex D <9899_D>`.\ [#9899_note60]_ The initial character shall not be a universal character name designating a digit. An implementation may allow multibyte characters that are not part of the basic source character set to appear in identifiers; which characters and their correspondence to universal character names is implementation-defined.

.. _9899_6.4.2.1p4:

:ref:`4 <9899_6.4.2.1p4>` When preprocessing tokens are converted to tokens during translation phase 7, if a preprocessing token could be converted to either a keyword or an identifier, it is converted to a keyword.

.. rubric:: Implementation limits

.. _9899_6.4.2.1p5:

:ref:`5 <9899_6.4.2.1p5>` As discussed in :ref:`5.2.4.1 <9899_5.2.4.1>`, an implementation may limit the number of significant initial characters in an identifier; the limit for an external name (an identifier that has external linkage) may be more restrictive than that for an internal name (a macro name or an identifier that does not have external linkage). The number of significant characters in an identifier is implementation-defined.

.. _9899_6.4.2.1p6:

:ref:`6 <9899_6.4.2.1p6>` Any identifiers that differ in a significant character are different identifiers. If two identifiers differ only in nonsignificant characters, the behavior is undefined.

**Forward references**: universal character names (:ref:`6.4.3 <9899_6.4.3>`), macro replacement (:ref:`6.10.3 <9899_6.10.3>`).





.. rubric:: Footnotes

.. [#9899_note60] On systems in which linkers cannot accept extended characters, an encoding of the universal character name may be used in forming valid external identifiers. For example, some otherwise unused character or sequence of characters may be used to encode the \\u in a universal character name. Extended characters may produce a long external identifier.
