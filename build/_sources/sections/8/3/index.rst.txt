.. _9899_A.3:

A.3 Preprocessing directives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(:ref:`6.10 <9899_6.10>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            preprocessing-file
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            group
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
(:ref:`6.10 <9899_6.10>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            group
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            group-part
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            group
     
   
         .. container:: syntax-nonterminal
   
            group-part
   
(:ref:`6.10 <9899_6.10>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            group-part
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            if-section
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            control-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            text-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-nonterminal
   
            non-directive
   
(:ref:`6.10 <9899_6.10>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            if-section
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            if-group
     
   
         .. container:: syntax-nonterminal
   
            elif-groups
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            else-group
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            endif-line
   
(:ref:`6.10 <9899_6.10>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            if-group
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            if
     
   
         .. container:: syntax-nonterminal
   
            constant-expression
     
   
         .. container:: syntax-nonterminal
   
            new-line
     
   
         .. container:: syntax-nonterminal
   
            group
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            ifdef
     
   
         .. container:: syntax-nonterminal
   
            identifier
     
   
         .. container:: syntax-nonterminal
   
            new-line
     
   
         .. container:: syntax-nonterminal
   
            group
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            ifndef
     
   
         .. container:: syntax-nonterminal
   
            identifier
     
   
         .. container:: syntax-nonterminal
   
            new-line
     
   
         .. container:: syntax-nonterminal
   
            group
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
(:ref:`6.10 <9899_6.10>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            elif-groups
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            elif-group
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            elif-groups
     
   
         .. container:: syntax-nonterminal
   
            elif-group
   
(:ref:`6.10 <9899_6.10>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            elif-group
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            elif
     
   
         .. container:: syntax-nonterminal
   
            constant-expression
     
   
         .. container:: syntax-nonterminal
   
            new-line
     
   
         .. container:: syntax-nonterminal
   
            group
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
(:ref:`6.10 <9899_6.10>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            else-group
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            else
     
   
         .. container:: syntax-nonterminal
   
            new-line
     
   
         .. container:: syntax-nonterminal
   
            group
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
(:ref:`6.10 <9899_6.10>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            endif-line
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            endif
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
(:ref:`6.10 <9899_6.10>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            control-line
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            include
     
   
         .. container:: syntax-nonterminal
   
            pp-tokens
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            define
     
   
         .. container:: syntax-nonterminal
   
            identifier
     
   
         .. container:: syntax-nonterminal
   
            replacement-list
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            define
     
   
         .. container:: syntax-nonterminal
   
            identifier
     
   
         .. container:: syntax-nonterminal
   
            lparen
     
   
         .. container:: syntax-nonterminal
   
            identifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            )
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            replacement-list
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            define
     
   
         .. container:: syntax-nonterminal
   
            identifier
     
   
         .. container:: syntax-nonterminal
   
            lparen
     
   
         .. container:: syntax-terminal
   
            \.\.\.
     
   
         .. container:: syntax-terminal
   
            )
     
   
         .. container:: syntax-nonterminal
   
            replacement-list
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            define
     
   
         .. container:: syntax-nonterminal
   
            identifier
     
   
         .. container:: syntax-nonterminal
   
            lparen
     
   
         .. container:: syntax-nonterminal
   
            identifier-list
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-terminal
   
            \.\.\.
     
   
         .. container:: syntax-terminal
   
            )
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            replacement-list
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            undef
     
   
         .. container:: syntax-nonterminal
   
            identifier
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            line
     
   
         .. container:: syntax-nonterminal
   
            pp-tokens
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            error
     
   
         .. container:: syntax-nonterminal
   
            pp-tokens
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            pragma
     
   
         .. container:: syntax-nonterminal
   
            pp-tokens
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
(:ref:`6.10 <9899_6.10>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            text-line
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pp-tokens
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
(:ref:`6.10 <9899_6.10>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            non-directive
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pp-tokens
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
(:ref:`6.10 <9899_6.10>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            lparen
   
         :
   
      .. container:: syntax-rule
       
   
         a
     
   
         .. container:: syntax-terminal
   
            (
     
   
         character not immediately preceded by white-space
   
(:ref:`6.10 <9899_6.10>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            replacement-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pp-tokens
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
(:ref:`6.10 <9899_6.10>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            pp-tokens
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            preprocessing-token
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pp-tokens
     
   
         .. container:: syntax-nonterminal
   
            preprocessing-token
   
(:ref:`6.10 <9899_6.10>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            new-line
   
         :
   
      .. container:: syntax-rule
   
         the
   
         .. container:: syntax-nonterminal
   
            new-line
   
         character

