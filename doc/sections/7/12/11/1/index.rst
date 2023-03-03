.. _9899_7.12.11.1:

7.12.11.1 The copysign functions
''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.11.1p1:

:ref:`1 <9899_7.12.11.1p1>`

::

    #include <math.h>
    double copysign(double x, double y);
    float copysignf(float x, float y);
    long double copysignl(long double x, long double y);

.. rubric:: Description

.. _9899_7.12.11.1p2:

:ref:`2 <9899_7.12.11.1p2>` The copysign functions produce a value with the magnitude of x and the sign of y. They produce a NaN (with the sign of y) if x is a NaN. On implementations that represent a signed zero but do not treat negative zero consistently in arithmetic operations, the copysign functions regard the sign of zero as positive.

.. rubric:: Returns

.. _9899_7.12.11.1p3:

:ref:`3 <9899_7.12.11.1p3>` The copysign functions return a value with the magnitude of x and the sign of y.

