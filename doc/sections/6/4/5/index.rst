.. _9899_6.4.5:

6.4.5 String literals
^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.4.5p1:

:ref:`1 <9899_6.4.5p1>`

.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            string-literal
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            "
     
   
         .. container:: syntax-nonterminal
   
            s-char-sequence
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            "
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            L"
     
   
         .. container:: syntax-nonterminal
   
            s-char-sequence
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            "
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            s-char-sequence
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            s-char
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            s-char-sequence
     
   
         .. container:: syntax-nonterminal
   
            s-char
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            s-char
   
         :
   
      .. container:: syntax-rule
       
         any member of the source character set except the double-quote
   
         .. container:: syntax-terminal
   
            "

         , backslash
   
         .. container:: syntax-terminal
   
            \\

         , or
   
         .. container:: syntax-nonterminal
   
            new-line
   
         character
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            escape-sequence

.. rubric:: Description

.. _9899_6.4.5p2:

:ref:`2 <9899_6.4.5p2>` A character string literal is a sequence of zero or more multibyte characters enclosed in double-quotes, as in "xyz". A wide string literal is the same, except prefixed by the letter L.

.. _9899_6.4.5p3:

:ref:`3 <9899_6.4.5p3>` The same considerations apply to each element of the sequence in a character string literal or a wide string literal as if it were in an integer character constant or a wide character constant, except that the single-quote ' is representable either by itself or by the escape sequence \\', but the double-quote " shall be represented by the escape sequence \\".

.. rubric:: Semantics

.. _9899_6.4.5p4:

:ref:`4 <9899_6.4.5p4>` In translation phase 6, the multibyte character sequences specified by any sequence of adjacent character and wide string literal tokens are concatenated into a single multibyte character sequence. If any of the tokens are wide string literal tokens, the resulting multibyte character sequence is treated as a wide string literal; otherwise, it is treated as a character string literal.

.. _9899_6.4.5p5:

:ref:`5 <9899_6.4.5p5>` In translation phase 7, a byte or code of value zero is appended to each multibyte character sequence that results from a string literal or literals.\ [#9899_note66]_ The multibyte character sequence is then used to initialize an array of static storage duration and length just sufficient to contain the sequence. For character string literals, the array elements have type char, and are initialized with the individual bytes of the multibyte character sequence; for wide string literals, the array elements have type wchar_t, and are initialized with the sequence of wide characters corresponding to the multibyte character sequence, as defined by the mbstowcs function with an implementation-defined current locale. The value of a string literal containing a multibyte character or escape sequence not represented in the execution character set is implementation-defined.

.. _9899_6.4.5p6:

:ref:`6 <9899_6.4.5p6>` It is unspecified whether these arrays are distinct provided their elements have the appropriate values. If the program attempts to modify such an array, the behavior is undefined.

.. _9899_6.4.5p7:

:ref:`7 <9899_6.4.5p7>` EXAMPLE This pair of adjacent character string literals

::

    "\x12" "3"

produces a single character string literal containing the two characters whose values are '\\x12' and '3', because escape sequences are converted into single members of the execution character set just prior to adjacent string literal concatenation.

**Forward references**: common definitions :ref:`\<stddef.h> <9899_7.17>` (:ref:`7.17 <9899_7.17>`), the mbstowcs function (:ref:`7.20.8.1 <9899_7.20.8.1>`).





.. rubric:: Footnotes

.. [#9899_note66] A character string literal need not be a string (see :ref:`7.1.1 <9899_7.1.1>`), because a null character may be embedded in it by a \\0 escape sequence.
