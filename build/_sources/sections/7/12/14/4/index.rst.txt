.. _9899_7.12.14.4:

7.12.14.4 The islessequal macro
'''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.14.4p1:

.. container:: snum

   :ref:`1 <9899_7.12.14.4p1>`



::

    #include <math.h>
    int islessequal(real-floating x, real-floating y);

.. rubric:: Description

.. _9899_7.12.14.4p2:

.. container:: snum

   :ref:`2 <9899_7.12.14.4p2>`

The islessequal macro determines whether its first argument is less than or equal to its second argument. The value of islessequal(x, y) is always equal to (x) <= (y); however, unlike (x) <= (y), islessequal(x, y) does not raise the "invalid" floating-point exception when x and y are unordered.

.. rubric:: Returns

.. _9899_7.12.14.4p3:

.. container:: snum

   :ref:`3 <9899_7.12.14.4p3>`

The islessequal macro returns the value of (x) <= (y).

