.. _9899_6.8.4:

6.8.4 Selection statements
^^^^^^^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index


.. rubric:: Syntax

.. _9899_6.8.4p1:

.. container:: snum

   :ref:`1 <9899_6.8.4p1>`



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

.. rubric:: Semantics

.. _9899_6.8.4p2:

.. container:: snum

   :ref:`2 <9899_6.8.4p2>`

A selection statement selects among a set of statements depending on the value of a controlling expression.

.. _9899_6.8.4p3:

.. container:: snum

   :ref:`3 <9899_6.8.4p3>`

A selection statement is a block whose scope is a strict subset of the scope of its enclosing block. Each associated substatement is also a block whose scope is a strict subset of the scope of the selection statement.

