.. _9899_6.4.3:

6.4.3 Universal character names
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.4.3p1:

:ref:`1 <9899_6.4.3p1>`

.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            universal-character-name
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            \\u
     
   
         .. container:: syntax-nonterminal
   
            hex-quad
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            \\U
     
   
         .. container:: syntax-nonterminal
   
            hex-quad
     
   
         .. container:: syntax-nonterminal
   
            hex-quad
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            hex-quad
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            hexadecimal-digit
     
   
         .. container:: syntax-nonterminal
   
            hexadecimal-digit
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            hexadecimal-digit
     
   
         .. container:: syntax-nonterminal
   
            hexadecimal-digit

.. rubric:: Constraints

.. _9899_6.4.3p2:

:ref:`2 <9899_6.4.3p2>` A universal character name shall not specify a character whose short identifier is less than 00A0 other than 0024 ($), 0040 (@), or 0060 ('), nor one in the range D800 through DFFF inclusive.\ [#9899_note62]_

.. rubric:: Description

.. _9899_6.4.3p3:

:ref:`3 <9899_6.4.3p3>` Universal character names may be used in identifiers, character constants, and string literals to designate characters that are not in the basic character set.

.. rubric:: Semantics

.. _9899_6.4.3p4:

:ref:`4 <9899_6.4.3p4>` The universal character name \\Unnnnnnnn designates the character whose eight-digit short identifier (as specified by ISO/IEC 10646) is nnnnnnnn.\ [#9899_note63]_ Similarly, the universal character name \\unnnn designates the character whose four-digit short identifier is nnnn (and whose eight-digit short identifier is 0000nnnn).






.. rubric:: Footnotes

.. [#9899_note62] The disallowed characters are the characters in the basic character set and the code positions reserved by ISO/IEC 10646 for control characters, the character DELETE, and the S-zone (reserved for use by UTF-16).
.. [#9899_note63] Short identifiers for characters were first specified in ISO/IEC 10646-1/AMD9:1997.
