.. _9899_6.3.1.4:

6.3.1.4 Real floating and integer
'''''''''''''''''''''''''''''''''

.. _9899_6.3.1.4p1:

.. container:: snum

   :ref:`1 <9899_6.3.1.4p1>`

When a finite value of real floating type is converted to an integer type other than \_Bool, the fractional part is discarded (i.e., the value is truncated toward zero). If the value of the integral part cannot be represented by the integer type, the behavior is undefined.\ [#9899_note50]_

.. _9899_6.3.1.4p2:

.. container:: snum

   :ref:`2 <9899_6.3.1.4p2>`

When a value of integer type is converted to a real floating type, if the value being converted can be represented exactly in the new type, it is unchanged. If the value being converted is in the range of values that can be represented but cannot be represented exactly, the result is either the nearest higher or nearest lower representable value, chosen in an implementation-defined manner. If the value being converted is outside the range of values that can be represented, the behavior is undefined.





.. rubric:: Footnotes

.. [#9899_note50] The remaindering operation performed when a value of integer type is converted to unsigned type need not be performed when a value of real floating type is converted to unsigned type. Thus, the range of portable real floating values is (-1, Utype_MAX+1).
