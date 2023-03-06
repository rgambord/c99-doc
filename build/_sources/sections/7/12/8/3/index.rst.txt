.. _9899_7.12.8.3:

7.12.8.3 The lgamma functions
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.8.3p1:

.. container:: snum

   :ref:`1 <9899_7.12.8.3p1>`



::

    #include <math.h>
    double lgamma(double x);
    float lgammaf(float x);
    long double lgammal(long double x);

.. rubric:: Description

.. _9899_7.12.8.3p2:

.. container:: snum

   :ref:`2 <9899_7.12.8.3p2>`

The lgamma functions compute the natural logarithm of the absolute value of gamma of x. A range error occurs if x is too large. A range error may occur if x is a negative integer or zero.

.. rubric:: Returns

.. _9899_7.12.8.3p3:

.. container:: snum

   :ref:`3 <9899_7.12.8.3p3>`

The lgamma functions return loge \| (Gamma)(x) \|.

