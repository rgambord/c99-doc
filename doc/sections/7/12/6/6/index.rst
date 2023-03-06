.. _9899_7.12.6.6:

7.12.6.6 The ldexp functions
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.6.6p1:

.. container:: snum

   :ref:`1 <9899_7.12.6.6p1>`



::

    #include <math.h>
    double ldexp(double x, int exp);
    float ldexpf(float x, int exp);
    long double ldexpl(long double x, int exp);

.. rubric:: Description

.. _9899_7.12.6.6p2:

.. container:: snum

   :ref:`2 <9899_7.12.6.6p2>`

The ldexp functions multiply a floating-point number by an integral power of 2. A range error may occur.

.. rubric:: Returns

.. _9899_7.12.6.6p3:

.. container:: snum

   :ref:`3 <9899_7.12.6.6p3>`

The ldexp functions return x 2\ :sup:`exp` .

