.. _9899_7.12.9.3:

7.12.9.3 The nearbyint functions
''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.9.3p1:

:ref:`1 <9899_7.12.9.3p1>`

::

    #include <math.h>
    double nearbyint(double x);
    float nearbyintf(float x);
    long double nearbyintl(long double x);

.. rubric:: Description

.. _9899_7.12.9.3p2:

:ref:`2 <9899_7.12.9.3p2>` The nearbyint functions round their argument to an integer value in floating-point format, using the current rounding direction and without raising the ''inexact'' floating- point exception.

.. rubric:: Returns

.. _9899_7.12.9.3p3:

:ref:`3 <9899_7.12.9.3p3>` The nearbyint functions return the rounded integer value.

