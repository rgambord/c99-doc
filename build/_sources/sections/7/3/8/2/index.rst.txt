.. _9899_7.3.8.2:

7.3.8.2 The cpow functions
''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.3.8.2p1:

.. container:: snum

   :ref:`1 <9899_7.3.8.2p1>`



::

    #include <complex.h>
    double complex cpow(double complex x, double complex y);
    float complex cpowf(float complex x, float complex y);
    long double complex cpowl(long double complex x,
         long double complex y);

.. rubric:: Description

.. _9899_7.3.8.2p2:

.. container:: snum

   :ref:`2 <9899_7.3.8.2p2>`

The cpow functions compute the complex power function x\ :sup:`y` , with a branch cut for the first parameter along the negative real axis.

.. rubric:: Returns

.. _9899_7.3.8.2p3:

.. container:: snum

   :ref:`3 <9899_7.3.8.2p3>`

The cpow functions return the complex power function value.

