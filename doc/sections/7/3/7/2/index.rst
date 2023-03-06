.. _9899_7.3.7.2:

7.3.7.2 The clog functions
''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.3.7.2p1:

.. container:: snum

   :ref:`1 <9899_7.3.7.2p1>`



::

    #include <complex.h>
    double complex clog(double complex z);
    float complex clogf(float complex z);
    long double complex clogl(long double complex z);

.. rubric:: Description

.. _9899_7.3.7.2p2:

.. container:: snum

   :ref:`2 <9899_7.3.7.2p2>`

The clog functions compute the complex natural (base-e) logarithm of z, with a branch cut along the negative real axis.

.. rubric:: Returns

.. _9899_7.3.7.2p3:

.. container:: snum

   :ref:`3 <9899_7.3.7.2p3>`

The clog functions return the complex natural logarithm value, in the range of a strip mathematically unbounded along the real axis and in the interval [-ipi , +ipi ] along the imaginary axis.

