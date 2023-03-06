.. _9899_6.5.12:

6.5.12 Bitwise inclusive OR operator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.5.12p1:

.. container:: snum

   :ref:`1 <9899_6.5.12p1>`



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

.. rubric:: Constraints

.. _9899_6.5.12p2:

.. container:: snum

   :ref:`2 <9899_6.5.12p2>`

Each of the operands shall have integer type.

.. rubric:: Semantics

.. _9899_6.5.12p3:

.. container:: snum

   :ref:`3 <9899_6.5.12p3>`

The usual arithmetic conversions are performed on the operands.

.. _9899_6.5.12p4:

.. container:: snum

   :ref:`4 <9899_6.5.12p4>`

The result of the \| operator is the bitwise inclusive OR of the operands (that is, each bit in the result is set if and only if at least one of the corresponding bits in the converted operands is set).

