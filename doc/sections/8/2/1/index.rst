.. _9899_A.2.1:

A.2.1 Expressions
^^^^^^^^^^^^^^^^^

(:ref:`6.5.1 <9899_6.5.1>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            primary-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            identifier
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            constant
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            string-literal
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            expression
     
   
         .. container:: syntax-terminal
   
            )

(:ref:`6.5.2 <9899_6.5.2>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            postfix-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            primary-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            postfix-expression
     
   
         .. container:: syntax-terminal
   
            [
     
   
         .. container:: syntax-nonterminal
   
            expression
     
   
         .. container:: syntax-terminal
   
            ]
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            postfix-expression
     
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            argument-expression-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            )
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            postfix-expression
     
   
         .. container:: syntax-terminal
   
            .
     
   
         .. container:: syntax-nonterminal
   
            identifier
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            postfix-expression
     
   
         .. container:: syntax-terminal
   
            ->
     
   
         .. container:: syntax-nonterminal
   
            identifier
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            postfix-expression
     
   
         .. container:: syntax-terminal
   
            ++
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            postfix-expression
     
   
         .. container:: syntax-terminal
   
            --
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            type-name
     
   
         .. container:: syntax-terminal
   
            )
     
   
         .. container:: syntax-terminal
   
            {
     
   
         .. container:: syntax-nonterminal
   
            initializer-list
     
   
         .. container:: syntax-terminal
   
            }
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            type-name
     
   
         .. container:: syntax-terminal
   
            )
     
   
         .. container:: syntax-terminal
   
            {
     
   
         .. container:: syntax-nonterminal
   
            initializer-list
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-terminal
   
            }

(:ref:`6.5.2 <9899_6.5.2>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            argument-expression-list
   
         :

      .. container:: syntax-rule
         
         .. container:: nonterminal

            assignment-expression

      .. container:: syntax-rule
         
         .. container:: syntax-nonterminal

            argument-expression-list 
        
         .. container:: syntax-terminal
            
            ,

         .. container:: syntax-nonterminal

            assignment-expression

(:ref:`6.5.3 <9899_6.5.3>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            unary-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            postfix-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            ++
     
   
         .. container:: syntax-nonterminal
   
            unary-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            --
     
   
         .. container:: syntax-nonterminal
   
            unary-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            unary-operator
     
   
         .. container:: syntax-nonterminal
   
            cast-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            sizeof
     
   
         .. container:: syntax-nonterminal
   
            unary-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            sizeof
     
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            type-name
     
   
         .. container:: syntax-terminal
   
            )
   
(:ref:`6.5.3 <9899_6.5.3>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            unary-operator
   
         : one of
   
      .. container:: syntax-rule-tbl
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               &
      
            .. container:: syntax-terminal
      
               \*
      
            .. container:: syntax-terminal
      
               \+
      
            .. container:: syntax-terminal
      
               \-
      
            .. container:: syntax-terminal
      
               ~
      
            .. container:: syntax-terminal
      
               !

(:ref:`6.5.4 <9899_6.5.4>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            cast-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            unary-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            type-name
     
   
         .. container:: syntax-terminal
   
            )
     
   
         .. container:: syntax-nonterminal
   
            cast-expression

(:ref:`6.5.5 <9899_6.5.5>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            multiplicative-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            cast-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            multiplicative-expression
     
   
         .. container:: syntax-terminal
   
            \*
     
   
         .. container:: syntax-nonterminal
   
            cast-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            multiplicative-expression
     
   
         .. container:: syntax-terminal
   
            /
     
   
         .. container:: syntax-nonterminal
   
            cast-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            multiplicative-expression
     
   
         .. container:: syntax-terminal
   
            \%
     
   
         .. container:: syntax-nonterminal
   
            cast-expression

(:ref:`6.5.6 <9899_6.5.6>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            additive-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            multiplicative-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            additive-expression
     
   
         .. container:: syntax-terminal
   
            \+
     
   
         .. container:: syntax-nonterminal
   
            multiplicative-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            additive-expression
     
   
         .. container:: syntax-terminal
   
            \-
     
   
         .. container:: syntax-nonterminal
   
            multiplicative-expression

(:ref:`6.5.7 <9899_6.5.7>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            shift-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            additive-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            shift-expression
     
   
         .. container:: syntax-terminal
   
            <<
     
   
         .. container:: syntax-nonterminal
   
            additive-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            shift-expression
     
   
         .. container:: syntax-terminal
   
            >>
     
   
         .. container:: syntax-nonterminal
   
            additive-expression

(:ref:`6.5.8 <9899_6.5.8>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            relational-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            shift-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            relational-expression
     
   
         .. container:: syntax-terminal
   
            <
     
   
         .. container:: syntax-nonterminal
   
            shift-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            relational-expression
     
   
         .. container:: syntax-terminal
   
            >
     
   
         .. container:: syntax-nonterminal
   
            shift-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            relational-expression
     
   
         .. container:: syntax-terminal
   
            <=
     
   
         .. container:: syntax-nonterminal
   
            shift-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            relational-expression
     
   
         .. container:: syntax-terminal
   
            >=
     
   
         .. container:: syntax-nonterminal
   
            shift-expression

(:ref:`6.5.9 <9899_6.5.9>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            equality-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            relational-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            equality-expression
     
   
         .. container:: syntax-terminal
   
            ==
     
   
         .. container:: syntax-nonterminal
   
            relational-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            equality-expression
     
   
         .. container:: syntax-terminal
   
            !=
     
   
         .. container:: syntax-nonterminal
   
            relational-expression

(:ref:`6.5.10 <9899_6.5.10>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            AND-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            equality-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            AND-expression
     
   
         .. container:: syntax-terminal
   
            &
     
   
         .. container:: syntax-nonterminal
   
            equality-expression

(:ref:`6.5.11 <9899_6.5.11>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            exclusive-OR-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            AND-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            exclusive-OR-expression
     
   
         .. container:: syntax-terminal
   
            ^
     
   
         .. container:: syntax-nonterminal
   
            AND-expression

(:ref:`6.5.12 <9899_6.5.12>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            inclusive-OR-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            exclusive-OR-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            inclusive-OR-expression
     
   
         .. container:: syntax-terminal
   
            \|
     
   
         .. container:: syntax-nonterminal
   
            exclusive-OR-expression

(:ref:`6.5.13 <9899_6.5.13>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            logical-AND-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            inclusive-OR-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            logical-AND-expression
     
   
         .. container:: syntax-terminal
   
            &&
     
   
         .. container:: syntax-nonterminal
   
            inclusive-OR-expression

(:ref:`6.5.14 <9899_6.5.14>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            logical-OR-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            logical-AND-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            logical-OR-expression
     
   
         .. container:: syntax-terminal
   
            \|\|
     
   
         .. container:: syntax-nonterminal
   
            logical-AND-expression

(:ref:`6.5.15 <9899_6.5.15>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            conditional-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            logical-OR-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            logical-OR-expression
     
   
         .. container:: syntax-terminal
   
            ?
     
   
         .. container:: syntax-nonterminal
   
            expression
     
   
         .. container:: syntax-terminal
   
            :
     
   
         .. container:: syntax-nonterminal
   
            conditional-expression

(:ref:`6.5.16 <9899_6.5.16>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            assignment-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            conditional-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            unary-expression
     
   
         .. container:: syntax-nonterminal
   
            assignment-operator
     
   
         .. container:: syntax-nonterminal
   
            assignment-expression
   
(:ref:`6.5.16 <9899_6.5.16>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            assignment-operator
   
         : one of
   
      .. container:: syntax-rule-tbl
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               =
      
            .. container:: syntax-terminal
      
               \*=
      
            .. container:: syntax-terminal
      
               /=
      
            .. container:: syntax-terminal
      
               \%=
      
            .. container:: syntax-terminal
      
               +=
      
            .. container:: syntax-terminal
      
               -=
      
            .. container:: syntax-terminal
      
               <<=
      
            .. container:: syntax-terminal
      
               >>=
      
            .. container:: syntax-terminal
      
               &=
      
            .. container:: syntax-terminal
      
               ^=
      
            .. container:: syntax-terminal
      
               \|=

(:ref:`6.5.17 <9899_6.5.17>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            assignment-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            expression
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-nonterminal
   
            assignment-expression

(:ref:`6.6 <9899_6.6>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            constant-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            conditional-expression

