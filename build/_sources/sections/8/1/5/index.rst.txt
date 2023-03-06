.. _9899_A.1.5:

A.1.5 Constants
^^^^^^^^^^^^^^^

(:ref:`6.4.4 <9899_6.4.4>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            constant
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            integer-constant
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            floating-constant
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            enumeration-constant
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            character-constant

(:ref:`6.4.4.1 <9899_6.4.4.1>`)

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
   
(:ref:`6.4.4.1 <9899_6.4.4.1>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.1 <9899_6.4.4.1>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.1 <9899_6.4.4.1>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.1 <9899_6.4.4.1>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.1 <9899_6.4.4.1>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.1 <9899_6.4.4.1>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.1 <9899_6.4.4.1>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.1 <9899_6.4.4.1>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.1 <9899_6.4.4.1>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.1 <9899_6.4.4.1>`)

.. container:: syntax-block

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
      
(:ref:`6.4.4.1 <9899_6.4.4.1>`)

.. container:: syntax-block

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

(:ref:`6.4.4.2 <9899_6.4.4.2>`)

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
   
(:ref:`6.4.4.2 <9899_6.4.4.2>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.2 <9899_6.4.4.2>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.2 <9899_6.4.4.2>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.2 <9899_6.4.4.2>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.2 <9899_6.4.4.2>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.2 <9899_6.4.4.2>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.2 <9899_6.4.4.2>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.2 <9899_6.4.4.2>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.2 <9899_6.4.4.2>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.2 <9899_6.4.4.2>`)

.. container:: syntax-block

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

(:ref:`6.4.4.3 <9899_6.4.4.3>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            enumeration-constant
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            identifier

(:ref:`6.4.4.4 <9899_6.4.4.4>`)

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
   
(:ref:`6.4.4.4 <9899_6.4.4.4>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.4 <9899_6.4.4.4>`)

.. container:: syntax-block

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
     
   
         |_| character |_|
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            escape-sequence
   
(:ref:`6.4.4.4 <9899_6.4.4.4>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.4 <9899_6.4.4.4>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.4 <9899_6.4.4.4>`)

.. container:: syntax-block

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
   
(:ref:`6.4.4.4 <9899_6.4.4.4>`)

.. container:: syntax-block

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

