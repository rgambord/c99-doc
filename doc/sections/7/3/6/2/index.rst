.. _9899_7.3.6.2:

7.3.6.2 The casinh functions
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.3.6.2p1:

:ref:`1 <9899_7.3.6.2p1>`

::

    #include <complex.h>
    double complex casinh(double complex z);
    float complex casinhf(float complex z);
    long double complex casinhl(long double complex z);

.. rubric:: Description

.. _9899_7.3.6.2p2:

:ref:`2 <9899_7.3.6.2p2>` The casinh functions compute the complex arc hyperbolic sine of z, with branch cuts outside the interval [-i, +i] along the imaginary axis.

.. rubric:: Returns

.. _9899_7.3.6.2p3:

:ref:`3 <9899_7.3.6.2p3>` The casinh functions return the complex arc hyperbolic sine value, in the range of a strip mathematically unbounded along the real axis and in the interval [-ipi /2, +ipi /2] along the imaginary axis.

