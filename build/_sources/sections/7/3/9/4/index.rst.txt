.. _9899_7.3.9.4:

7.3.9.4 The cproj functions
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.3.9.4p1:

.. container:: snum

   :ref:`1 <9899_7.3.9.4p1>`



::

    #include <complex.h>
    double complex cproj(double complex z);
    float complex cprojf(float complex z);
    long double complex cprojl(long double complex z);

.. rubric:: Description

.. _9899_7.3.9.4p2:

.. container:: snum

   :ref:`2 <9899_7.3.9.4p2>`

The cproj functions compute a projection of z onto the Riemann sphere: z projects to z except that all complex infinities (even those with one infinite part and one NaN part) project to positive infinity on the real axis. If z has an infinite part, then cproj(z) is equivalent to

::

    INFINITY + I * copysign(0.0, cimag(z))

.. rubric:: Returns

.. _9899_7.3.9.4p3:

.. container:: snum

   :ref:`3 <9899_7.3.9.4p3>`

The cproj functions return the value of the projection onto the Riemann sphere.

