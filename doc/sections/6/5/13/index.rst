.. _9899_6.5.13:

6.5.13 Logical AND operator
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.5.13p1:

:ref:`1 <9899_6.5.13p1>`

.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            logical-AND-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            inclusive-OR-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            logical-AND-expression
     
   
         .. container:: syntax-terminal
   
            &&
     
   
         .. container:: syntax-nonterminal
   
            inclusive-OR-expression

.. rubric:: Constraints

.. _9899_6.5.13p2:

:ref:`2 <9899_6.5.13p2>` Each of the operands shall have scalar type.

.. rubric:: Semantics

.. _9899_6.5.13p3:

:ref:`3 <9899_6.5.13p3>` The && operator shall yield 1 if both of its operands compare unequal to 0; otherwise, it yields 0. The result has type int.

.. _9899_6.5.13p4:

:ref:`4 <9899_6.5.13p4>` Unlike the bitwise binary & operator, the && operator guarantees left-to-right evaluation; there is a sequence point after the evaluation of the first operand. If the first operand compares equal to 0, the second operand is not evaluated.

