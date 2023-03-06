.. _9899_7.3.5.1:

7.3.5.1 The cacos functions
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.3.5.1p1:

.. container:: snum

   :ref:`1 <9899_7.3.5.1p1>`



::

    #include <complex.h>
    double complex cacos(double complex z);
    float complex cacosf(float complex z);
    long double complex cacosl(long double complex z);

.. rubric:: Description

.. _9899_7.3.5.1p2:

.. container:: snum

   :ref:`2 <9899_7.3.5.1p2>`

The cacos functions compute the complex arc cosine of z, with branch cuts outside the interval [-1, +1] along the real axis.

.. rubric:: Returns

.. _9899_7.3.5.1p3:

.. container:: snum

   :ref:`3 <9899_7.3.5.1p3>`

The cacos functions return the complex arc cosine value, in the range of a strip mathematically unbounded along the imaginary axis and in the interval [0, pi ] along the real axis.

