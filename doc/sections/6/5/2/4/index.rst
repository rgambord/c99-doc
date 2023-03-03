.. _9899_6.5.2.4:

6.5.2.4 Postfix increment and decrement operators
'''''''''''''''''''''''''''''''''''''''''''''''''

.. rubric:: Constraints

.. _9899_6.5.2.4p1:

:ref:`1 <9899_6.5.2.4p1>` The operand of the postfix increment or decrement operator shall have qualified or unqualified real or pointer type and shall be a modifiable lvalue.

.. rubric:: Semantics

.. _9899_6.5.2.4p2:

:ref:`2 <9899_6.5.2.4p2>` The result of the postfix ++ operator is the value of the operand. After the result is obtained, the value of the operand is incremented. (That is, the value 1 of the appropriate type is added to it.) See the discussions of additive operators and compound assignment for information on constraints, types, and conversions and the effects of operations on pointers. The side effect of updating the stored value of the operand shall occur between the previous and the next sequence point.

.. _9899_6.5.2.4p3:

:ref:`3 <9899_6.5.2.4p3>` The postfix -- operator is analogous to the postfix ++ operator, except that the value of the operand is decremented (that is, the value 1 of the appropriate type is subtracted from it).

**Forward references**: additive operators (:ref:`6.5.6 <9899_6.5.6>`), compound assignment (:ref:`6.5.16.2 <9899_6.5.16.2>`).

