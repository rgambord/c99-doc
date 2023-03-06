.. _9899_6.5.16.2:

6.5.16.2 Compound assignment
''''''''''''''''''''''''''''

.. rubric:: Constraints

.. _9899_6.5.16.2p1:

.. container:: snum

   :ref:`1 <9899_6.5.16.2p1>`

For the operators += and -= only, either the left operand shall be a pointer to an object type and the right shall have integer type, or the left operand shall have qualified or unqualified arithmetic type and the right shall have arithmetic type.

.. _9899_6.5.16.2p2:

.. container:: snum

   :ref:`2 <9899_6.5.16.2p2>`

For the other operators, each operand shall have arithmetic type consistent with those allowed by the corresponding binary operator.

.. rubric:: Semantics

.. _9899_6.5.16.2p3:

.. container:: snum

   :ref:`3 <9899_6.5.16.2p3>`

A compound assignment of the form E1 op = E2 differs from the simple assignment expression E1 = E1 op (E2) only in that the lvalue E1 is evaluated only once.

