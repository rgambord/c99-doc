.. _9899_6.8.6:

6.8.6 Jump statements
^^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index
   4/index


.. rubric:: Syntax

.. _9899_6.8.6p1:

.. container:: snum

   :ref:`1 <9899_6.8.6p1>`



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

.. rubric:: Semantics

.. _9899_6.8.6p2:

.. container:: snum

   :ref:`2 <9899_6.8.6p2>`

A jump statement causes an unconditional jump to another place.

