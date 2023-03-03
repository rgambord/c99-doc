.. _9899_6.5.3:

6.5.3 Unary operators
^^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index
   4/index


.. rubric:: Syntax

.. _9899_6.5.3p1:

:ref:`1 <9899_6.5.3p1>`

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

