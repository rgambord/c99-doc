.. _9899_7.12.6.4:

7.12.6.4 The frexp functions
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.6.4p1:

:ref:`1 <9899_7.12.6.4p1>`

::

    #include <math.h>
    double frexp(double value, int *exp);
    float frexpf(float value, int *exp);
    long double frexpl(long double value, int *exp);

.. rubric:: Description

.. _9899_7.12.6.4p2:

:ref:`2 <9899_7.12.6.4p2>` The frexp functions break a floating-point number into a normalized fraction and an integral power of 2. They store the integer in the int object pointed to by exp.

.. rubric:: Returns

.. _9899_7.12.6.4p3:

:ref:`3 <9899_7.12.6.4p3>` If value is not a floating-point number, the results are unspecified. Otherwise, the frexp functions return the value x, such that x has a magnitude in the interval [1/2, 1) or zero, and value equals x 2\ :sup:`\*exp` . If value is zero, both parts of the result are zero.

