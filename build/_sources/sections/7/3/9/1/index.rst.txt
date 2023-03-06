.. _9899_7.3.9.1:

7.3.9.1 The carg functions
''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.3.9.1p1:

.. container:: snum

   :ref:`1 <9899_7.3.9.1p1>`



::

    #include <complex.h>
    double carg(double complex z);
    float cargf(float complex z);
    long double cargl(long double complex z);

.. rubric:: Description

.. _9899_7.3.9.1p2:

.. container:: snum

   :ref:`2 <9899_7.3.9.1p2>`

The carg functions compute the argument (also called phase angle) of z, with a branch cut along the negative real axis.

.. rubric:: Returns

.. _9899_7.3.9.1p3:

.. container:: snum

   :ref:`3 <9899_7.3.9.1p3>`

The carg functions return the value of the argument in the interval [-pi , +pi ].

