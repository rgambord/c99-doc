.. _9899_7.12.6.8:

7.12.6.8 The log10 functions
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.6.8p1:

.. container:: snum

   :ref:`1 <9899_7.12.6.8p1>`



::

    #include <math.h>
    double log10(double x);
    float log10f(float x);
    long double log10l(long double x);

.. rubric:: Description

.. _9899_7.12.6.8p2:

.. container:: snum

   :ref:`2 <9899_7.12.6.8p2>`

The log10 functions compute the base-10 (common) logarithm of x. A domain error occurs if the argument is negative. A range error may occur if the argument is zero.

.. rubric:: Returns

.. _9899_7.12.6.8p3:

.. container:: snum

   :ref:`3 <9899_7.12.6.8p3>`

The log10 functions return log10 x.

