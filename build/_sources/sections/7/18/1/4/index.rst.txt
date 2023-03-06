.. _9899_7.18.1.4:

7.18.1.4 Integer types capable of holding object pointers
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. _9899_7.18.1.4p1:

.. container:: snum

   :ref:`1 <9899_7.18.1.4p1>`

The following type designates a signed integer type with the property that any valid pointer to void can be converted to this type, then converted back to pointer to void, and the result will compare equal to the original pointer:

::

    intptr_t

The following type designates an unsigned integer type with the property that any valid pointer to void can be converted to this type, then converted back to pointer to void, and the result will compare equal to the original pointer:

::

    uintptr_t

These types are optional.

