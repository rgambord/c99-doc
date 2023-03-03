.. _9899_7.12.6.11:

7.12.6.11 The logb functions
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.6.11p1:

:ref:`1 <9899_7.12.6.11p1>`

::

    #include <math.h>
    double logb(double x);
    float logbf(float x);
    long double logbl(long double x);

.. rubric:: Description

.. _9899_7.12.6.11p2:

:ref:`2 <9899_7.12.6.11p2>` The logb functions extract the exponent of x, as a signed integer value in floating-point format. If x is subnormal it is treated as though it were normalized; thus, for positive finite x,

::

    1 <= x FLT_RADIX-logb(x) < FLT_RADIX

A domain error or range error may occur if the argument is zero.

.. rubric:: Returns

.. _9899_7.12.6.11p3:

:ref:`3 <9899_7.12.6.11p3>` The logb functions return the signed exponent of x.

