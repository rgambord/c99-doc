.. _9899_7.12.14.3:

7.12.14.3 The isless macro
''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.14.3p1:

.. container:: snum

   :ref:`1 <9899_7.12.14.3p1>`



::

    #include <math.h>
    int isless(real-floating x, real-floating y);

.. rubric:: Description

.. _9899_7.12.14.3p2:

.. container:: snum

   :ref:`2 <9899_7.12.14.3p2>`

The isless macro determines whether its first argument is less than its second argument. The value of isless(x, y) is always equal to (x) < (y); however, unlike (x) < (y), isless(x, y) does not raise the "invalid" floating-point exception when x and y are unordered.

.. rubric:: Returns

.. _9899_7.12.14.3p3:

.. container:: snum

   :ref:`3 <9899_7.12.14.3p3>`

The isless macro returns the value of (x) < (y).

