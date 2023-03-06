.. _9899_7.12.9.6:

7.12.9.6 The round functions
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.9.6p1:

.. container:: snum

   :ref:`1 <9899_7.12.9.6p1>`



::

    #include <math.h>
    double round(double x);
    float roundf(float x);
    long double roundl(long double x);

.. rubric:: Description

.. _9899_7.12.9.6p2:

.. container:: snum

   :ref:`2 <9899_7.12.9.6p2>`

The round functions round their argument to the nearest integer value in floating-point format, rounding halfway cases away from zero, regardless of the current rounding direction.

.. rubric:: Returns

.. _9899_7.12.9.6p3:

.. container:: snum

   :ref:`3 <9899_7.12.9.6p3>`

The round functions return the rounded integer value.

