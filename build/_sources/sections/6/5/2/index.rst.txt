.. _9899_6.5.2:

6.5.2 Postfix operators
^^^^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index
   4/index
   5/index


.. rubric:: Syntax

.. _9899_6.5.2p1:

.. container:: snum

   :ref:`1 <9899_6.5.2p1>`



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

