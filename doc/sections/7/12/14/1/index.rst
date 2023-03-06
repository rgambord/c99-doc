.. _9899_7.12.14.1:

7.12.14.1 The isgreater macro
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.14.1p1:

.. container:: snum

   :ref:`1 <9899_7.12.14.1p1>`



::

    #include <math.h>
    int isgreater(real-floating x, real-floating y);

.. rubric:: Description

.. _9899_7.12.14.1p2:

.. container:: snum

   :ref:`2 <9899_7.12.14.1p2>`

The isgreater macro determines whether its first argument is greater than its second argument. The value of isgreater(x, y) is always equal to (x) > (y); however, unlike (x) > (y), isgreater(x, y) does not raise the "invalid" floating-point exception when x and y are unordered.

.. rubric:: Returns

.. _9899_7.12.14.1p3:

.. container:: snum

   :ref:`3 <9899_7.12.14.1p3>`

The isgreater macro returns the value of (x) > (y).

