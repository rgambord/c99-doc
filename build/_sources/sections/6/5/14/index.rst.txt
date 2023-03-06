.. _9899_6.5.14:

6.5.14 Logical OR operator
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.5.14p1:

.. container:: snum

   :ref:`1 <9899_6.5.14p1>`



.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            logical-OR-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            logical-AND-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            logical-OR-expression
     
   
         .. container:: syntax-terminal
   
            \|\|
     
   
         .. container:: syntax-nonterminal
   
            logical-AND-expression

.. rubric:: Constraints

.. _9899_6.5.14p2:

.. container:: snum

   :ref:`2 <9899_6.5.14p2>`

Each of the operands shall have scalar type.

.. rubric:: Semantics

.. _9899_6.5.14p3:

.. container:: snum

   :ref:`3 <9899_6.5.14p3>`

The \|\| operator shall yield 1 if either of its operands compare unequal to 0; otherwise, it yields 0. The result has type int.

.. _9899_6.5.14p4:

.. container:: snum

   :ref:`4 <9899_6.5.14p4>`

Unlike the bitwise \| operator, the \|\| operator guarantees left-to-right evaluation; there is a sequence point after the evaluation of the first operand. If the first operand compares unequal to 0, the second operand is not evaluated.

