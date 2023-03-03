.. _9899_7.12.4.1:

7.12.4.1 The acos functions
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.4.1p1:

:ref:`1 <9899_7.12.4.1p1>`

::

    #include <math.h>
    double acos(double x);
    float acosf(float x);
    long double acosl(long double x);

.. rubric:: Description

.. _9899_7.12.4.1p2:

:ref:`2 <9899_7.12.4.1p2>` The acos functions compute the principal value of the arc cosine of x. A domain error occurs for arguments not in the interval [-1, +1].

.. rubric:: Returns

.. _9899_7.12.4.1p3:

:ref:`3 <9899_7.12.4.1p3>` The acos functions return arccos x in the interval [0, pi ] radians.

