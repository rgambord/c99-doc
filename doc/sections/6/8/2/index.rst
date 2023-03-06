.. _9899_6.8.2:

6.8.2 Compound statement
^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.8.2p1:

.. container:: snum

   :ref:`1 <9899_6.8.2p1>`



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

.. rubric:: Semantics

.. _9899_6.8.2p2:

.. container:: snum

   :ref:`2 <9899_6.8.2p2>`

A compound statement is a block.

