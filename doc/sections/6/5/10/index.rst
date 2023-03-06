.. _9899_6.5.10:

6.5.10 Bitwise AND operator
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.5.10p1:

.. container:: snum

   :ref:`1 <9899_6.5.10p1>`



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

.. rubric:: Constraints

.. _9899_6.5.10p2:

.. container:: snum

   :ref:`2 <9899_6.5.10p2>`

Each of the operands shall have integer type.

.. rubric:: Semantics

.. _9899_6.5.10p3:

.. container:: snum

   :ref:`3 <9899_6.5.10p3>`

The usual arithmetic conversions are performed on the operands.

.. _9899_6.5.10p4:

.. container:: snum

   :ref:`4 <9899_6.5.10p4>`

The result of the binary & operator is the bitwise AND of the operands (that is, each bit in the result is set if and only if each of the corresponding bits in the converted operands is set).

