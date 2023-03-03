.. _9899_7.12.6.10:

7.12.6.10 The log2 functions
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.6.10p1:

:ref:`1 <9899_7.12.6.10p1>`

::

    #include <math.h>
    double log2(double x);
    float log2f(float x);
    long double log2l(long double x);

.. rubric:: Description

.. _9899_7.12.6.10p2:

:ref:`2 <9899_7.12.6.10p2>` The log2 functions compute the base-2 logarithm of x. A domain error occurs if the argument is less than zero. A range error may occur if the argument is zero.

.. rubric:: Returns

.. _9899_7.12.6.10p3:

:ref:`3 <9899_7.12.6.10p3>` The log2 functions return log2 x.

