.. _9899_6.8.4.1:

6.8.4.1 The if statement
''''''''''''''''''''''''

.. rubric:: Constraints

.. _9899_6.8.4.1p1:

.. container:: snum

   :ref:`1 <9899_6.8.4.1p1>`

The controlling expression of an if statement shall have scalar type.

.. rubric:: Semantics

.. _9899_6.8.4.1p2:

.. container:: snum

   :ref:`2 <9899_6.8.4.1p2>`

In both forms, the first substatement is executed if the expression compares unequal to 0. In the else form, the second substatement is executed if the expression compares equal to 0. If the first substatement is reached via a label, the second substatement is not executed.

.. _9899_6.8.4.1p3:

.. container:: snum

   :ref:`3 <9899_6.8.4.1p3>`

An else is associated with the lexically nearest preceding if that is allowed by the syntax.

