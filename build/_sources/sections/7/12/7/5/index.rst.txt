.. _9899_7.12.7.5:

7.12.7.5 The sqrt functions
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.7.5p1:

.. container:: snum

   :ref:`1 <9899_7.12.7.5p1>`



::

    #include <math.h>
    double sqrt(double x);
    float sqrtf(float x);
    long double sqrtl(long double x);

.. rubric:: Description

.. _9899_7.12.7.5p2:

.. container:: snum

   :ref:`2 <9899_7.12.7.5p2>`

The sqrt functions compute the nonnegative square root of x. A domain error occurs if the argument is less than zero.

.. rubric:: Returns

.. _9899_7.12.7.5p3:

.. container:: snum

   :ref:`3 <9899_7.12.7.5p3>`

The sqrt functions return (sqrt)(x).

