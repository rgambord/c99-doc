.. _9899_6.5.3.3:

6.5.3.3 Unary arithmetic operators
''''''''''''''''''''''''''''''''''

.. rubric:: Constraints

.. _9899_6.5.3.3p1:

:ref:`1 <9899_6.5.3.3p1>` The operand of the unary + or - operator shall have arithmetic type; of the ~ operator, integer type; of the ! operator, scalar type.

.. rubric:: Semantics

.. _9899_6.5.3.3p2:

:ref:`2 <9899_6.5.3.3p2>` The result of the unary + operator is the value of its (promoted) operand. The integer promotions are performed on the operand, and the result has the promoted type.

.. _9899_6.5.3.3p3:

:ref:`3 <9899_6.5.3.3p3>` The result of the unary - operator is the negative of its (promoted) operand. The integer promotions are performed on the operand, and the result has the promoted type.

.. _9899_6.5.3.3p4:

:ref:`4 <9899_6.5.3.3p4>` The result of the ~ operator is the bitwise complement of its (promoted) operand (that is, each bit in the result is set if and only if the corresponding bit in the converted operand is not set). The integer promotions are performed on the operand, and the result has the promoted type. If the promoted type is an unsigned type, the expression ~E is equivalent to the maximum value representable in that type minus E.

.. _9899_6.5.3.3p5:

:ref:`5 <9899_6.5.3.3p5>` The result of the logical negation operator ! is 0 if the value of its operand compares unequal to 0, 1 if the value of its operand compares equal to 0. The result has type int. The expression !E is equivalent to (0==E).

