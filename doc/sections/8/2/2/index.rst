.. _9899_A.2.2:

A.2.2 Declarations
^^^^^^^^^^^^^^^^^^

(:ref:`6.7 <9899_6.7>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            declaration
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            declaration-specifiers
     
   
         .. container:: syntax-nonterminal
   
            init-declarator-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            ;
   
(:ref:`6.7 <9899_6.7>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            declaration-specifiers
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            storage-class-specifier
     
   
         .. container:: syntax-nonterminal
   
            declaration-specifiers
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            type-specifier
     
   
         .. container:: syntax-nonterminal
   
            declaration-specifiers
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            type-qualifier
     
   
         .. container:: syntax-nonterminal
   
            declaration-specifiers
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            function-specifier
     
   
         .. container:: syntax-nonterminal
   
            declaration-specifiers
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
(:ref:`6.7 <9899_6.7>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            init-declarator-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            init-declarator
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            init-declarator-list
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-nonterminal
   
            init-declarator
   
(:ref:`6.7 <9899_6.7>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            init-declarator
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            declarator
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            declarator
     
   
         .. container:: syntax-terminal
   
            =
     
   
         .. container:: syntax-nonterminal
   
            initializer

(:ref:`6.7.1 <9899_6.7.1>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            storage-class-specifier
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            typedef
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            extern
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            static
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            auto
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            register

(:ref:`6.7.2 <9899_6.7.2>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            type-specifier
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            void
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            char
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            short
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            int
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            long
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            float
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            double
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            signed
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            unsigned
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            _Bool
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            _Complex
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            struct-or-union-specifier
     
   
         .. container:: syntax-terminal
   
            \*
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            enum-specifier
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            typedef-name

(:ref:`6.7.2.1 <9899_6.7.2.1>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            struct-or-union-specifier
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            struct-or-union
     
   
         .. container:: syntax-nonterminal
   
            identifier
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            {
     
   
         .. container:: syntax-nonterminal
   
            struct-declaration-list
     
   
         .. container:: syntax-terminal
   
            }
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            struct-or-union
     
   
         .. container:: syntax-nonterminal
   
            identifier
   
(:ref:`6.7.2.1 <9899_6.7.2.1>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            struct-or-union
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            struct
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            union
   
(:ref:`6.7.2.1 <9899_6.7.2.1>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            struct-declaration-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            struct-declaration
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            struct-declaration-list
     
   
         .. container:: syntax-nonterminal
   
            struct-declaration
   
(:ref:`6.7.2.1 <9899_6.7.2.1>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            struct-declaration
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            specifier-qualifier-list
     
   
         .. container:: syntax-nonterminal
   
            struct-declarator-list
     
   
         .. container:: syntax-terminal
   
            ;
   
(:ref:`6.7.2.1 <9899_6.7.2.1>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            specifier-qualifier-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            type-specifier
     
   
         .. container:: syntax-nonterminal
   
            specifier-qualifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            type-qualifier
     
   
         .. container:: syntax-nonterminal
   
            specifier-qualifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
(:ref:`6.7.2.1 <9899_6.7.2.1>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            struct-declarator-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            struct-declarator
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            struct-declarator-list
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-nonterminal
   
            struct-declarator
   
(:ref:`6.7.2.1 <9899_6.7.2.1>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            struct-declarator
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            declarator
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            declarator
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            :
     
   
         .. container:: syntax-nonterminal
   
            constant-expression

(:ref:`6.7.2.2 <9899_6.7.2.2>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            enum-specifier
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            enum
     
   
         .. container:: syntax-nonterminal
   
            identifier
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            {
     
   
         .. container:: syntax-nonterminal
   
            enumerator-list
     
   
         .. container:: syntax-terminal
   
            }
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            enum
     
   
         .. container:: syntax-nonterminal
   
            identifier
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            {
     
   
         .. container:: syntax-nonterminal
   
            enumerator-list
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-terminal
   
            }
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            enum
     
   
         .. container:: syntax-nonterminal
   
            identifier
   
(:ref:`6.7.2.2 <9899_6.7.2.2>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            enumerator-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            enumerator
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            enumerator-list
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-nonterminal
   
            enumerator
   
(:ref:`6.7.2.2 <9899_6.7.2.2>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            enumerator
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            enumeration-constant
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            enumeration-constant
     
   
         .. container:: syntax-terminal
   
            =
     
   
         .. container:: syntax-nonterminal
   
            constant-expression

(:ref:`6.7.3 <9899_6.7.3>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            type-qualifier
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            const
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            restrict
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            volatile

(:ref:`6.7.4 <9899_6.7.4>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            function-specifier
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            inline

(:ref:`6.7.5 <9899_6.7.5>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            declarator
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pointer
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            direct-declarator
   
(:ref:`6.7.5 <9899_6.7.5>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            direct-declarator
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            identifier
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            declarator
     
   
         .. container:: syntax-terminal
   
            )
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-declarator
     
   
         .. container:: syntax-terminal
   
            [
     
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            assignment-expression
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            ]
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-declarator
     
   
         .. container:: syntax-terminal
   
            [
     
   
         .. container:: syntax-terminal
   
            static
     
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            assignment-expression
     
   
         .. container:: syntax-terminal
   
            ]
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-declarator
     
   
         .. container:: syntax-terminal
   
            [
     
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
     
   
         .. container:: syntax-terminal
   
            static
     
   
         .. container:: syntax-nonterminal
   
            assignment-expression
     
   
         .. container:: syntax-terminal
   
            ]
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-declarator
     
   
         .. container:: syntax-terminal
   
            [
     
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            \*
     
   
         .. container:: syntax-terminal
   
            ]
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-declarator
     
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            parameter-type-list
     
   
         .. container:: syntax-terminal
   
            )
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-declarator
     
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            identifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            )
   
(:ref:`6.7.5 <9899_6.7.5>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            pointer
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            \*
     
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            \*
     
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            pointer
   
(:ref:`6.7.5 <9899_6.7.5>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            type-qualifier
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
     
   
         .. container:: syntax-nonterminal
   
            type-qualifier
   
(:ref:`6.7.5 <9899_6.7.5>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            parameter-type-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            parameter-list
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            parameter-list
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-terminal
   
            \.\.\.
   
(:ref:`6.7.5 <9899_6.7.5>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            parameter-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            parameter-declaration
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            parameter-list
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-nonterminal
   
            parameter-declaration
   
(:ref:`6.7.5 <9899_6.7.5>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            parameter-declaration
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            declaration-specifiers
     
   
         .. container:: syntax-nonterminal
   
            declarator
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            declaration-specifiers
     
   
         .. container:: syntax-nonterminal
   
            abstract-declarator
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
(:ref:`6.7.5 <9899_6.7.5>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            identifier-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            identifier
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            identifier-list
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-nonterminal
   
            identifier

(:ref:`6.7.6 <9899_6.7.6>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            type-name
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            specifier-qualifier-list
     
   
         .. container:: syntax-nonterminal
   
            abstract-declarator
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
(:ref:`6.7.6 <9899_6.7.6>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            abstract-declarator
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pointer
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pointer
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            direct-abstract-declarator
   
(:ref:`6.7.6 <9899_6.7.6>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            direct-abstract-declarator
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            abstract-declarator
     
   
         .. container:: syntax-terminal
   
            )
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-abstract-declarator
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            [
     
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            assignment-expression
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            ]
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-abstract-declarator
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            [
     
   
         .. container:: syntax-terminal
   
            static
     
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            assignment-expression
     
   
         .. container:: syntax-terminal
   
            ]
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-abstract-declarator
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            [
     
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
     
   
         .. container:: syntax-terminal
   
            static
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            assignment-expression
     
   
         .. container:: syntax-terminal
   
            ]
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-abstract-declarator
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            [
     
   
         .. container:: syntax-terminal
   
            \*
     
   
         .. container:: syntax-terminal
   
            ]
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-abstract-declarator
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            parameter-type-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            )

(:ref:`6.7.7 <9899_6.7.7>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            typedef-name
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            identifier

(:ref:`6.7.8 <9899_6.7.8>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            initializer
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            assignment-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            {
     
   
         .. container:: syntax-nonterminal
   
            initializer-list
     
   
         .. container:: syntax-terminal
   
            }
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            {
     
   
         .. container:: syntax-nonterminal
   
            initializer-list
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-terminal
   
            }
   
(:ref:`6.7.8 <9899_6.7.8>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            initializer-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            designation
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            initializer
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            initializer-list
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-nonterminal
   
            designation
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            initializer
   
(:ref:`6.7.8 <9899_6.7.8>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            designation
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            designator-list
     
   
         .. container:: syntax-terminal
   
            =
   
(:ref:`6.7.8 <9899_6.7.8>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            designator-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            designator
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            designator-list
     
   
         .. container:: syntax-nonterminal
   
            designator
   
(:ref:`6.7.8 <9899_6.7.8>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            designator
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            [
     
   
         .. container:: syntax-nonterminal
   
            constant-expression
     
   
         .. container:: syntax-terminal
   
            ]
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            .
     
   
         .. container:: syntax-nonterminal
   
            identifier

