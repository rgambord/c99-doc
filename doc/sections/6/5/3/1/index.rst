.. _9899_6.5.3.1:

6.5.3.1 Prefix increment and decrement operators
''''''''''''''''''''''''''''''''''''''''''''''''

.. rubric:: Constraints

.. _9899_6.5.3.1p1:

.. container:: snum

   :ref:`1 <9899_6.5.3.1p1>`

The operand of the prefix increment or decrement operator shall have qualified or unqualified real or pointer type and shall be a modifiable lvalue.

.. rubric:: Semantics

.. _9899_6.5.3.1p2:

.. container:: snum

   :ref:`2 <9899_6.5.3.1p2>`

The value of the operand of the prefix ++ operator is incremented. The result is the new value of the operand after incrementation. The expression ++E is equivalent to (E+=1). See the discussions of additive operators and compound assignment for information on constraints, types, side effects, and conversions and the effects of operations on pointers.

.. _9899_6.5.3.1p3:

.. container:: snum

   :ref:`3 <9899_6.5.3.1p3>`

The prefix -- operator is analogous to the prefix ++ operator, except that the value of the operand is decremented.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.5.6`
   - :ref:`9899_6.5.16.2`

