.. _9899_6.3.1.3:

6.3.1.3 Signed and unsigned integers
''''''''''''''''''''''''''''''''''''

.. _9899_6.3.1.3p1:

:ref:`1 <9899_6.3.1.3p1>` When a value with integer type is converted to another integer type other than \_Bool, if the value can be represented by the new type, it is unchanged.

.. _9899_6.3.1.3p2:

:ref:`2 <9899_6.3.1.3p2>` Otherwise, if the new type is unsigned, the value is converted by repeatedly adding or subtracting one more than the maximum value that can be represented in the new type until the value is in the range of the new type.\ [#9899_note49]_

.. _9899_6.3.1.3p3:

:ref:`3 <9899_6.3.1.3p3>` Otherwise, the new type is signed and the value cannot be represented in it; either the result is implementation-defined or an implementation-defined signal is raised.





.. rubric:: Footnotes

.. [#9899_note49] The rules describe arithmetic on the mathematical value, not the value of a given type of expression.
