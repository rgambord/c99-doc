.. _9899_6.4.4.1:

6.4.4.1 Integer constants
'''''''''''''''''''''''''

.. rubric:: Syntax

.. _9899_6.4.4.1p1:

:ref:`1 <9899_6.4.4.1p1>`

.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            integer-constant
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            decimal-constant
     
   
         .. container:: syntax-nonterminal
   
            integer-suffix
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            octal-constant
     
   
         .. container:: syntax-nonterminal
   
            integer-suffix
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            hexadecimal-constant
     
   
         .. container:: syntax-nonterminal
   
            integer-suffix
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            decimal-constant
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            nonzero-digit
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            decimal-constant
     
   
         .. container:: syntax-nonterminal
   
            digit
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            octal-constant
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            0
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            octal-constant
     
   
         .. container:: syntax-nonterminal
   
            octal-digit
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            hexadecimal-constant
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            hexadecimal-prefix
     
   
         .. container:: syntax-nonterminal
   
            hexadecimal-digit
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            hexadecimal-constant
     
   
         .. container:: syntax-nonterminal
   
            hexadecimal-digit
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            hexadecimal-prefix
   
         : one of
   
      .. container:: syntax-rule-tbl
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               0x
      
            .. container:: syntax-terminal
      
               0X
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            nonzero-digit
   
         : one of
   
      .. container:: syntax-rule-tbl
      
         .. container:: syntax-rule
      
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
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            octal-digit
   
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
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            hexadecimal-digit
   
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
      
      
         .. container:: syntax-rule
         
      
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
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            integer-suffix
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            unsigned-suffix
     
   
         .. container:: syntax-nonterminal
   
            long-suffix
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            unsigned-suffix
     
   
         .. container:: syntax-nonterminal
   
            long-long-suffix
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            long-suffix
     
   
         .. container:: syntax-nonterminal
   
            unsigned-suffix
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            long-long-suffix
     
   
         .. container:: syntax-nonterminal
   
            unsigned-suffix
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            unsigned-suffix
   
         : one of
   
      .. container:: syntax-rule-tbl
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               u
      
            .. container:: syntax-terminal
      
               U
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            long-suffix
   
         : one of
   
      .. container:: syntax-rule-tbl
         
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               l
      
            .. container:: syntax-terminal
      
               L
      
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            long-long-suffix
   
         : one of
   
      .. container:: syntax-rule-tbl
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               ll
      
            .. container:: syntax-terminal
      
               LL

.. rubric:: Description

.. _9899_6.4.4.1p2:

:ref:`2 <9899_6.4.4.1p2>` An integer constant begins with a digit, but has no period or exponent part. It may have a prefix that specifies its base and a suffix that specifies its type.

.. _9899_6.4.4.1p3:

:ref:`3 <9899_6.4.4.1p3>` A decimal constant begins with a nonzero digit and consists of a sequence of decimal digits. An octal constant consists of the prefix 0 optionally followed by a sequence of the digits 0 through 7 only. A hexadecimal constant consists of the prefix 0x or 0X followed by a sequence of the decimal digits and the letters a (or A) through f (or F) with values 10 through 15 respectively.

.. rubric:: Semantics

.. _9899_6.4.4.1p4:

:ref:`4 <9899_6.4.4.1p4>` The value of a decimal constant is computed base 10; that of an octal constant, base 8; that of a hexadecimal constant, base 16. The lexically first digit is the most significant.

.. _9899_6.4.4.1p5:

:ref:`5 <9899_6.4.4.1p5>` The type of an integer constant is the first of the corresponding list in which its value can be represented.

Suffix

Decimal Constant

Octal or Hexadecimal Constant

none

::





::








u or U

::





::





l or L

::

             



::






Both u or U and l or L

::




::




ll or LL

::



::




Both u or U and ll or LL

::



::



.. _9899_6.4.4.1p6:

:ref:`6 <9899_6.4.4.1p6>` If an integer constant cannot be represented by any type in its list, it may have an extended integer type, if the extended integer type can represent its value. If all of the types in the list for the constant are signed, the extended integer type shall be signed. If all of the types in the list for the constant are unsigned, the extended integer type shall be unsigned. If the list contains both signed and unsigned types, the extended integer type may be signed or unsigned. If an integer constant cannot be represented by any type in its list and has no extended integer type, then the integer constant has no type.

