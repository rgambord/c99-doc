.. _9899_A.2.3:

A.2.3 Statements
^^^^^^^^^^^^^^^^

(:ref:`6.8 <9899_6.8>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            statement
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            labeled-statement
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            compound-statement
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            expression-statement
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            selection-statement
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            iteration-statement
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            jump-statement

(:ref:`6.8.1 <9899_6.8.1>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            labeled-statement
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            identifier
     
   
         .. container:: syntax-terminal
   
            :
     
   
         .. container:: syntax-nonterminal
   
            statement
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            case
     
   
         .. container:: syntax-nonterminal
   
            constant-expression
     
   
         .. container:: syntax-terminal
   
            :
     
   
         .. container:: syntax-nonterminal
   
            statement
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            default
     
   
         .. container:: syntax-terminal
   
            :
     
   
         .. container:: syntax-nonterminal
   
            statement

(:ref:`6.8.2 <9899_6.8.2>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            compound-statement
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            {
     
   
         .. container:: syntax-nonterminal
   
            block-item-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            }
   
(:ref:`6.8.2 <9899_6.8.2>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            block-item-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            block-item
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            block-item-list
     
   
         .. container:: syntax-nonterminal
   
            block-item
   
(:ref:`6.8.2 <9899_6.8.2>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            block-item
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            declaration
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            statement

(:ref:`6.8.3 <9899_6.8.3>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            expression-statement
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            expression
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            ;

(:ref:`6.8.4 <9899_6.8.4>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            selection-statement
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            if
     
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            expression
     
   
         .. container:: syntax-terminal
   
            )
     
   
         .. container:: syntax-nonterminal
   
            statement
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            if
     
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            expression
     
   
         .. container:: syntax-terminal
   
            )
     
   
         .. container:: syntax-nonterminal
   
            statement
     
   
         .. container:: syntax-terminal
   
            else
     
   
         .. container:: syntax-nonterminal
   
            statement
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            switch
     
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            expression
     
   
         .. container:: syntax-terminal
   
            )
     
   
         .. container:: syntax-nonterminal
   
            statement

(:ref:`6.8.5 <9899_6.8.5>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            iteration-statement
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            while
     
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            expression
     
   
         .. container:: syntax-terminal
   
            )
     
   
         .. container:: syntax-nonterminal
   
            statement
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            do
     
   
         .. container:: syntax-nonterminal
   
            statement
     
   
         .. container:: syntax-terminal
   
            while
     
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            expression
     
   
         .. container:: syntax-terminal
   
            )
     
   
         .. container:: syntax-terminal
   
            ;
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            for
     
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            expression
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            ;
     
   
         .. container:: syntax-nonterminal
   
            expression
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            ;
     
   
         .. container:: syntax-nonterminal
   
            expression
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            )
     
   
         .. container:: syntax-nonterminal
   
            statement
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            for
     
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            declaration
     
   
         .. container:: syntax-nonterminal
   
            expression
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            ;
     
   
         .. container:: syntax-nonterminal
   
            expression
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            )
     
   
         .. container:: syntax-nonterminal
   
            statement

(:ref:`6.8.6 <9899_6.8.6>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            jump-statement
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            goto
     
   
         .. container:: syntax-nonterminal
   
            identifier
     
   
         .. container:: syntax-terminal
   
            ;
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            continue
     
   
         .. container:: syntax-terminal
   
            ;
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            break
     
   
         .. container:: syntax-terminal
   
            ;
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            return
     
   
         .. container:: syntax-nonterminal
   
            expression
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            ;

