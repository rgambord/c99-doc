.. _9899_7.3.6.1:

7.3.6.1 The cacosh functions
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.3.6.1p1:

.. container:: snum

   :ref:`1 <9899_7.3.6.1p1>`



::

    #include <complex.h>
    double complex cacosh(double complex z);
    float complex cacoshf(float complex z);
    long double complex cacoshl(long double complex z);

.. rubric:: Description

.. _9899_7.3.6.1p2:

.. container:: snum

   :ref:`2 <9899_7.3.6.1p2>`

The cacosh functions compute the complex arc hyperbolic cosine of z, with a branch cut at values less than 1 along the real axis.

.. rubric:: Returns

.. _9899_7.3.6.1p3:

.. container:: snum

   :ref:`3 <9899_7.3.6.1p3>`

The cacosh functions return the complex arc hyperbolic cosine value, in the range of a half-strip of non-negative values along the real axis and in the interval [-ipi , +ipi ] along the imaginary axis.

