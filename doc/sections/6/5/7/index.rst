.. _9899_6.5.7:

6.5.7 Bitwise shift operators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.5.7p1:

:ref:`1 <9899_6.5.7p1>`

.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            shift-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            additive-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            shift-expression
     
   
         .. container:: syntax-terminal
   
            <<
     
   
         .. container:: syntax-nonterminal
   
            additive-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            shift-expression
     
   
         .. container:: syntax-terminal
   
            >>
     
   
         .. container:: syntax-nonterminal
   
            additive-expression

.. rubric:: Constraints

.. _9899_6.5.7p2:

:ref:`2 <9899_6.5.7p2>` Each of the operands shall have integer type.

.. rubric:: Semantics

.. _9899_6.5.7p3:

:ref:`3 <9899_6.5.7p3>` The integer promotions are performed on each of the operands. The type of the result is that of the promoted left operand. If the value of the right operand is negative or is greater than or equal to the width of the promoted left operand, the behavior is undefined.

.. _9899_6.5.7p4:

:ref:`4 <9899_6.5.7p4>` The result of E1 \<< E2 is E1 left-shifted E2 bit positions; vacated bits are filled with zeros. If E1 has an unsigned type, the value of the result is E1 x 2\ :sup:`E2` , reduced modulo one more than the maximum value representable in the result type. If E1 has a signed type and nonnegative value, and E1 x 2\ :sup:`E2` is representable in the result type, then that is the resulting value; otherwise, the behavior is undefined.

.. _9899_6.5.7p5:

:ref:`5 <9899_6.5.7p5>` The result of E1 >> E2 is E1 right-shifted E2 bit positions. If E1 has an unsigned type or if E1 has a signed type and a nonnegative value, the value of the result is the integral part of the quotient of E1 / 2\ :sup:`E2` . If E1 has a signed type and a negative value, the resulting value is implementation-defined.

