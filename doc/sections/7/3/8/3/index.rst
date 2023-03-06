.. _9899_7.3.8.3:

7.3.8.3 The csqrt functions
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.3.8.3p1:

.. container:: snum

   :ref:`1 <9899_7.3.8.3p1>`



::

    #include <complex.h>
    double complex csqrt(double complex z);
    float complex csqrtf(float complex z);
    long double complex csqrtl(long double complex z);

.. rubric:: Description

.. _9899_7.3.8.3p2:

.. container:: snum

   :ref:`2 <9899_7.3.8.3p2>`

The csqrt functions compute the complex square root of z, with a branch cut along the negative real axis.

.. rubric:: Returns

.. _9899_7.3.8.3p3:

.. container:: snum

   :ref:`3 <9899_7.3.8.3p3>`

The csqrt functions return the complex square root value, in the range of the right half- plane (including the imaginary axis).

