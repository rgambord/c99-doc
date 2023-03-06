.. _9899_6.4.4.2:

6.4.4.2 Floating constants
''''''''''''''''''''''''''

.. rubric:: Syntax

.. _9899_6.4.4.2p1:

.. container:: snum

   :ref:`1 <9899_6.4.4.2p1>`



.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            floating-constant
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            decimal-floating-constant
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            hexadecimal-floating-constant
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            decimal-floating-constant
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            fractional-constant
     
   
         .. container:: syntax-nonterminal
   
            exponent-part
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            floating-suffix
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            digit-sequence
     
   
         .. container:: syntax-nonterminal
   
            exponent-part
     
   
         .. container:: syntax-nonterminal
   
            floating-suffix
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            hexadecimal-floating-constant
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            hexadecimal-prefix
     
   
         .. container:: syntax-nonterminal
   
            hexadecimal-fractional-constant
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            binary-exponent-part
     
   
         .. container:: syntax-nonterminal
   
            floating-suffix
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            hexadecimal-prefix
     
   
         .. container:: syntax-nonterminal
   
            hexadecimal-digit-sequence
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            binary-exponent-part
     
   
         .. container:: syntax-nonterminal
   
            floating-suffix
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            fractional-constant
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            digit-sequence
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            .
     
   
         .. container:: syntax-nonterminal
   
            digit-sequence
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            digit-sequence
     
   
         .. container:: syntax-terminal
   
            .
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            exponent-part
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            e
     
   
         .. container:: syntax-nonterminal
   
            sign
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            digit-sequence
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            E
     
   
         .. container:: syntax-nonterminal
   
            sign
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            digit-sequence
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            sign
   
         : one of
   
      .. container:: syntax-rule-tbl
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               \+
      
            .. container:: syntax-terminal
      
               \-
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            digit-sequence
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            digit
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            digit-sequence
     
   
         .. container:: syntax-nonterminal
   
            digit
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            hexadecimal-fractional-constant
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            hexadecimal-digit-sequence
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            .
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            hexadecimal-digit-sequence
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            hexadecimal-digit-sequence
     
   
         .. container:: syntax-terminal
   
            .
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            binary-exponent-part
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            p
     
   
         .. container:: syntax-nonterminal
   
            sign
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            digit-sequence
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            P
     
   
         .. container:: syntax-nonterminal
   
            sign
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            digit-sequence
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            hexadecimal-digit-sequence
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            hexadecimal-digit
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            hexadecimal-digit-sequence
     
   
         .. container:: syntax-nonterminal
   
            hexadecimal-digit
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            floating-suffix
   
         : one of
   
      .. container:: syntax-rule-tbl
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               f
      
            .. container:: syntax-terminal
      
               l
      
            .. container:: syntax-terminal
      
               F
      
            .. container:: syntax-terminal
      
               L

.. rubric:: Description

.. _9899_6.4.4.2p2:

.. container:: snum

   :ref:`2 <9899_6.4.4.2p2>`

A floating constant has a significand part that may be followed by an exponent part and a suffix that specifies its type. The components of the significand part may include a digit sequence representing the whole-number part, followed by a period (.), followed by a digit sequence representing the fraction part. The components of the exponent part are an e, E, p, or P followed by an exponent consisting of an optionally signed digit sequence. Either the whole-number part or the fraction part has to be present; for decimal floating constants, either the period or the exponent part has to be present.

.. rubric:: Semantics

.. _9899_6.4.4.2p3:

.. container:: snum

   :ref:`3 <9899_6.4.4.2p3>`

The significand part is interpreted as a (decimal or hexadecimal) rational number; the digit sequence in the exponent part is interpreted as a decimal integer. For decimal floating constants, the exponent indicates the power of 10 by which the significand part is to be scaled. For hexadecimal floating constants, the exponent indicates the power of 2 by which the significand part is to be scaled. For decimal floating constants, and also for hexadecimal floating constants when FLT_RADIX is not a power of 2, the result is either the nearest representable value, or the larger or smaller representable value immediately adjacent to the nearest representable value, chosen in an implementation-defined manner. For hexadecimal floating constants when FLT_RADIX is a power of 2, the result is correctly rounded.

.. _9899_6.4.4.2p4:

.. container:: snum

   :ref:`4 <9899_6.4.4.2p4>`

An unsuffixed floating constant has type double. If suffixed by the letter f or F, it has type float. If suffixed by the letter l or L, it has type long double.

.. _9899_6.4.4.2p5:

.. container:: snum

   :ref:`5 <9899_6.4.4.2p5>`

Floating constants are converted to internal format as if at translation-time. The conversion of a floating constant shall not raise an exceptional condition or a floating- point exception at execution time.

.. rubric:: Recommended practice

.. _9899_6.4.4.2p6:

.. container:: snum

   :ref:`6 <9899_6.4.4.2p6>`

The implementation should produce a diagnostic message if a hexadecimal constant cannot be represented exactly in its evaluation format; the implementation should then proceed with the translation of the program.

.. _9899_6.4.4.2p7:

.. container:: snum

   :ref:`7 <9899_6.4.4.2p7>`

The translation-time conversion of floating constants should match the execution-time conversion of character strings by library functions, such as strtod, given matching inputs suitable for both conversions, the same result format, and default execution-time rounding.\ [#9899_note64]_





.. rubric:: Footnotes

.. [#9899_note64] The specification for the library functions recommends more accurate conversion than required for floating constants (see :ref:`7.20.1.3 <9899_7.20.1.3>`).
