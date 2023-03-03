.. _9899_7.12.4.2:

7.12.4.2 The asin functions
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.4.2p1:

:ref:`1 <9899_7.12.4.2p1>`

::

    #include <math.h>
    double asin(double x);
    float asinf(float x);
    long double asinl(long double x);

.. rubric:: Description

.. _9899_7.12.4.2p2:

:ref:`2 <9899_7.12.4.2p2>` The asin functions compute the principal value of the arc sine of x. A domain error occurs for arguments not in the interval [-1, +1].

.. rubric:: Returns

.. _9899_7.12.4.2p3:

:ref:`3 <9899_7.12.4.2p3>` The asin functions return arcsin x in the interval [-pi /2, +pi /2] radians.

