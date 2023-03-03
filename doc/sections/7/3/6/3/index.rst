.. _9899_7.3.6.3:

7.3.6.3 The catanh functions
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.3.6.3p1:

:ref:`1 <9899_7.3.6.3p1>`

::

    #include <complex.h>
    double complex catanh(double complex z);
    float complex catanhf(float complex z);
    long double complex catanhl(long double complex z);

.. rubric:: Description

.. _9899_7.3.6.3p2:

:ref:`2 <9899_7.3.6.3p2>` The catanh functions compute the complex arc hyperbolic tangent of z, with branch cuts outside the interval [-1, +1] along the real axis.

.. rubric:: Returns

.. _9899_7.3.6.3p3:

:ref:`3 <9899_7.3.6.3p3>` The catanh functions return the complex arc hyperbolic tangent value, in the range of a strip mathematically unbounded along the real axis and in the interval [-ipi /2, +ipi /2] along the imaginary axis.

