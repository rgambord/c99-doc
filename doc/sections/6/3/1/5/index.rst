.. _9899_6.3.1.5:

6.3.1.5 Real floating types
'''''''''''''''''''''''''''

.. _9899_6.3.1.5p1:

:ref:`1 <9899_6.3.1.5p1>` When a float is promoted to double or long double, or a double is promoted to long double, its value is unchanged (if the source value is represented in the precision and range of its type).

.. _9899_6.3.1.5p2:

:ref:`2 <9899_6.3.1.5p2>` When a double is demoted to float, a long double is demoted to double or float, or a value being represented in greater precision and range than required by its semantic type (see :ref:`6.3.1.8 <9899_6.3.1.8>`) is explicitly converted (including to its own type), if the value being converted can be represented exactly in the new type, it is unchanged. If the value being converted is in the range of values that can be represented but cannot be represented exactly, the result is either the nearest higher or nearest lower representable value, chosen in an implementation-defined manner. If the value being converted is outside the range of values that can be represented, the behavior is undefined.

