.. _9899_7.3.5.2:

7.3.5.2 The casin functions
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.3.5.2p1:

.. container:: snum

   :ref:`1 <9899_7.3.5.2p1>`



::

    #include <complex.h>
    double complex casin(double complex z);
    float complex casinf(float complex z);
    long double complex casinl(long double complex z);

.. rubric:: Description

.. _9899_7.3.5.2p2:

.. container:: snum

   :ref:`2 <9899_7.3.5.2p2>`

The casin functions compute the complex arc sine of z, with branch cuts outside the interval [-1, +1] along the real axis.

.. rubric:: Returns

.. _9899_7.3.5.2p3:

.. container:: snum

   :ref:`3 <9899_7.3.5.2p3>`

The casin functions return the complex arc sine value, in the range of a strip mathematically unbounded along the imaginary axis and in the interval [-pi /2, +pi /2] along the real axis.

