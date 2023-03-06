.. _9899_7.3.5.3:

7.3.5.3 The catan functions
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.3.5.3p1:

.. container:: snum

   :ref:`1 <9899_7.3.5.3p1>`



::

    #include <complex.h>
    double complex catan(double complex z);
    float complex catanf(float complex z);
    long double complex catanl(long double complex z);

.. rubric:: Description

.. _9899_7.3.5.3p2:

.. container:: snum

   :ref:`2 <9899_7.3.5.3p2>`

The catan functions compute the complex arc tangent of z, with branch cuts outside the interval [-i, +i] along the imaginary axis.

.. rubric:: Returns

.. _9899_7.3.5.3p3:

.. container:: snum

   :ref:`3 <9899_7.3.5.3p3>`

The catan functions return the complex arc tangent value, in the range of a strip mathematically unbounded along the imaginary axis and in the interval [-pi /2, +pi /2] along the real axis.

