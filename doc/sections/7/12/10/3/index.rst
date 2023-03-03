.. _9899_7.12.10.3:

7.12.10.3 The remquo functions
''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.10.3p1:

:ref:`1 <9899_7.12.10.3p1>`

::

    #include <math.h>
    double remquo(double x, double y, int *quo);
    float remquof(float x, float y, int *quo);
    long double remquol(long double x, long double y,
         int *quo);

.. rubric:: Description

.. _9899_7.12.10.3p2:

:ref:`2 <9899_7.12.10.3p2>` The remquo functions compute the same remainder as the remainder functions. In the object pointed to by quo they store a value whose sign is the sign of x/y and whose magnitude is congruent modulo 2\ :sup:`n` to the magnitude of the integral quotient of x/y, where n is an implementation-defined integer greater than or equal to 3.

.. rubric:: Returns

.. _9899_7.12.10.3p3:

:ref:`3 <9899_7.12.10.3p3>` The remquo functions return x REM y. If y is zero, the value stored in the object pointed to by quo is unspecified and whether a domain error occurs or the functions return zero is implementation defined.

.. _9899_7.12.11:

