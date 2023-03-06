.. _9899_6.4.4.4:

6.4.4.4 Character constants
'''''''''''''''''''''''''''

.. rubric:: Syntax

.. _9899_6.4.4.4p1:

.. container:: snum

   :ref:`1 <9899_6.4.4.4p1>`



.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            character-constant
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            '
     
   
         .. container:: syntax-nonterminal
   
            c-char-sequence
     
   
         .. container:: syntax-terminal
   
            '
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            L'
     
   
         .. container:: syntax-nonterminal
   
            c-char-sequence
     
   
         .. container:: syntax-terminal
   
            '
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            c-char-sequence
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            c-char
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            c-char-sequence
     
   
         .. container:: syntax-nonterminal
   
            c-char
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            c-char
   
         :
   
      .. container:: syntax-text-rule
       
         any member of the source character set except the single-quote |_|
     
         .. container:: syntax-terminal
   
            '
            
         , backslash |_|
     
   
         .. container:: syntax-terminal
   
            \\

         , or |_|
   
         .. container:: syntax-nonterminal
   
            new-line
   
         |_| character
   
      .. container:: syntax-rule
   
         .. container:: syntax-nonterminal
   
            escape-sequence
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            escape-sequence
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            simple-escape-sequence
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            octal-escape-sequence
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            hexadecimal-escape-sequence
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            universal-character-name
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            simple-escape-sequence
   
         : one of
   
      .. container:: syntax-rule-tbl
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               \\'
      
            .. container:: syntax-terminal
      
               \\"
      
            .. container:: syntax-terminal
      
               \\?
      
            .. container:: syntax-terminal
      
               \\\ \\
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               \\a
      
            .. container:: syntax-terminal
      
               \\b
      
            .. container:: syntax-terminal
      
               \\f
      
            .. container:: syntax-terminal
      
               \\n
      
            .. container:: syntax-terminal
      
               \\r
      
            .. container:: syntax-terminal
      
               \\t
      
            .. container:: syntax-terminal
      
               \\v
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            octal-escape-sequence
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            \\
     
   
         .. container:: syntax-nonterminal
   
            octal-digit
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            \\
     
   
         .. container:: syntax-nonterminal
   
            octal-digit
     
   
         .. container:: syntax-nonterminal
   
            octal-digit
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            \\
     
   
         .. container:: syntax-nonterminal
   
            octal-digit
     
   
         .. container:: syntax-nonterminal
   
            octal-digit
     
   
         .. container:: syntax-nonterminal
   
            octal-digit
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            hexadecimal-escape-sequence
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            \\x
     
   
         .. container:: syntax-nonterminal
   
            hexadecimal-digit
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            hexadecimal-escape-sequence
     
   
         .. container:: syntax-nonterminal
   
            hexadecimal-digit

.. rubric:: Description

.. _9899_6.4.4.4p2:

.. container:: snum

   :ref:`2 <9899_6.4.4.4p2>`

An integer character constant is a sequence of one or more multibyte characters enclosed in single-quotes, as in `'x'`. A wide character constant is the same, except prefixed by the letter **L**\ . With a few exceptions detailed later, the elements of the sequence are any members of the source character set; they are mapped in an implementation-defined manner to members of the execution character set.

.. _9899_6.4.4.4p3:

.. container:: snum

   :ref:`3 <9899_6.4.4.4p3>`

The single-quote **'**\ , the double-quote **"**\ , the question-mark **?**\ , the backslash **\\**\ , and arbitrary integer values are representable according to the following table of escape sequences:

.. list-table::

   * - single quote **'**
     - **\\'**
   * - double quote **"**
     - **\\"**
   * - question mark **?**
     - **\\?**
   * - backslash **\\**
     - **\\\\**
   * - octal character
     - **\\**\ *octal digits*
   * - hexadecimal character
     - **\\x** *hexadecimal digits*

.. _9899_6.4.4.4p4:

.. container:: snum

   :ref:`4 <9899_6.4.4.4p4>`

The double-quote **"** and question-mark **?** are representable either by themselves or by the escape sequences **\\"** and **\\?**\ , respectively, but the single-quote **'** and the backslash **\\** shall be represented, respectively, by the escape sequences **\\'** and **\\\\**\ .

.. _9899_6.4.4.4p5:

.. container:: snum

   :ref:`5 <9899_6.4.4.4p5>`

The octal digits that follow the backslash in an octal escape sequence are taken to be part of the construction of a single character for an integer character constant or of a single wide character for a wide character constant. The numerical value of the octal integer so formed specifies the value of the desired character or wide character.

.. _9899_6.4.4.4p6:

.. container:: snum

   :ref:`6 <9899_6.4.4.4p6>`

The hexadecimal digits that follow the backslash and the letter **x** in a hexadecimal escape sequence are taken to be part of the construction of a single character for an integer character constant or of a single wide character for a wide character constant. The numerical value of the hexadecimal integer so formed specifies the value of the desired character or wide character.

.. _9899_6.4.4.4p7:

.. container:: snum

   :ref:`7 <9899_6.4.4.4p7>`

Each octal or hexadecimal escape sequence is the longest sequence of characters that can constitute the escape sequence.

.. _9899_6.4.4.4p8:

.. container:: snum

   :ref:`8 <9899_6.4.4.4p8>`

In addition, characters not in the basic character set are representable by universal character names and certain nongraphic characters are representable by escape sequences consisting of the backslash **\\** followed by a lowercase letter: **\\a**\ , **\\b**\ , **\\f**\ , **\\n**\ , **\\r**\ , **\\t**\ , and **\\v**\ .\ [#9899_note65]_

.. rubric:: Constraints

.. _9899_6.4.4.4p9:

.. container:: snum

   :ref:`9 <9899_6.4.4.4p9>`

The value of an octal or hexadecimal escape sequence shall be in the range of representable values for the type `unsigned char` for an integer character constant, or the unsigned type corresponding to `wchar_t` for a wide character constant.

.. rubric:: Semantics

.. _9899_6.4.4.4p10:

.. container:: snum

   :ref:`10 <9899_6.4.4.4p10>`

An integer character constant has type `int`. The value of an integer character constant containing a single character that maps to a single-byte execution character is the numerical value of the representation of the mapped character interpreted as an integer. The value of an integer character constant containing more than one character (e.g., `'ab'`), or containing a character or escape sequence that does not map to a single-byte execution character, is implementation-defined. If an integer character constant contains a single character or escape sequence, its value is the one that results when an object with type `char` whose value is that of the single character or escape sequence is converted to type `int`.

.. _9899_6.4.4.4p11:

.. container:: snum

   :ref:`11 <9899_6.4.4.4p11>`

A wide character constant has type `wchar_t`, an integer type defined in the :ref:`\<stddef.h> <9899_7.17>` header. The value of a wide character constant containing a single multibyte character that maps to a member of the extended execution character set is the wide character corresponding to that multibyte character, as defined by the mbtowc function, with an implementation-defined current locale. The value of a wide character constant containing more than one multibyte character, or containing a multibyte character or escape sequence not represented in the extended execution character set, is implementation-defined.

.. _9899_6.4.4.4p12:

.. container:: snum

   :ref:`12 <9899_6.4.4.4p12>`

EXAMPLE 1 The construction `'\\0'` is commonly used to represent the null character.

.. _9899_6.4.4.4p13:

.. container:: snum

   :ref:`13 <9899_6.4.4.4p13>`

EXAMPLE 2 Consider implementations that use two's-complement representation for integers and eight bits for objects that have type `char`. In an implementation in which type char has the same range of values as `signed char`, the integer character constant `'\\xFF'` has the value `-1`; if type `char` has the same range of values as `unsigned char`, the character constant `'\\xFF'` has the value `+255`.

.. _9899_6.4.4.4p14:

.. container:: snum

   :ref:`14 <9899_6.4.4.4p14>`

EXAMPLE 3 Even if eight bits are used for objects that have type char, the construction `'\\x123'` specifies an integer character constant containing only one character, since a hexadecimal escape sequence is terminated only by a non-hexadecimal character. To specify an integer character constant containing the two characters whose values are `'\\x12'` and `'3'`, the construction `'\\0223'` may be used, since an octal escape sequence is terminated after three octal digits. (The value of this two-character integer character constant is implementation-defined.)

.. _9899_6.4.4.4p15:

.. container:: snum

   :ref:`15 <9899_6.4.4.4p15>`

EXAMPLE 4 Even if 12 or more bits are used for objects that have type `wchar_t`, the construction `L'\\1234'` specifies the implementation-defined value that results from the combination of the values `0123` and `'4'`.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_7.17`
   - :ref:`9899_7.17`
   - :ref:`9899_7.20.7.2`





.. rubric:: Footnotes

.. [#9899_note65] The semantics of these characters were discussed in :ref:`5.2.2 <9899_5.2.2>`. If any other character follows a backslash, the result is not a token and a diagnostic is required. See "future language directions" (:ref:`6.11.4 <9899_6.11.4>`).
