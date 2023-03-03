.. _9899_7.12.10.1:

7.12.10.1 The fmod functions
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.10.1p1:

:ref:`1 <9899_7.12.10.1p1>`

::

    #include <math.h>
    double fmod(double x, double y);
    float fmodf(float x, float y);
    long double fmodl(long double x, long double y);

.. rubric:: Description

.. _9899_7.12.10.1p2:

:ref:`2 <9899_7.12.10.1p2>` The fmod functions compute the floating-point remainder of x/y.

.. rubric:: Returns

.. _9899_7.12.10.1p3:

:ref:`3 <9899_7.12.10.1p3>` The fmod functions return the value x - ny, for some integer n such that, if y is nonzero, the result has the same sign as x and magnitude less than the magnitude of y. If y is zero, whether a domain error occurs or the fmod functions return zero is implementation- defined.

