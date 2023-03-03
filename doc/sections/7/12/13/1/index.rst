.. _9899_7.12.13.1:

7.12.13.1 The fma functions
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.13.1p1:

:ref:`1 <9899_7.12.13.1p1>`

::

    #include <math.h>
    double fma(double x, double y, double z);
    float fmaf(float x, float y, float z);
    long double fmal(long double x, long double y,
         long double z);

.. rubric:: Description

.. _9899_7.12.13.1p2:

:ref:`2 <9899_7.12.13.1p2>` The fma functions compute (x y) + z, rounded as one ternary operation: they compute the value (as if) to infinite precision and round once to the result format, according to the current rounding mode. A range error may occur.

.. rubric:: Returns

.. _9899_7.12.13.1p3:

:ref:`3 <9899_7.12.13.1p3>` The fma functions return (x y) + z, rounded as one ternary operation.

