.. _9899_7.12.12.1:

7.12.12.1 The fdim functions
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.12.1p1:

:ref:`1 <9899_7.12.12.1p1>`

::

    #include <math.h>
    double fdim(double x, double y);
    float fdimf(float x, float y);
    long double fdiml(long double x, long double y);

.. rubric:: Description

.. _9899_7.12.12.1p2:

:ref:`2 <9899_7.12.12.1p2>` The fdim functions determine the positive difference between their arguments:

::

    {x - y  if x > y
    {
    {+0     if x <= y

A range error may occur.

.. rubric:: Returns

.. _9899_7.12.12.1p3:

:ref:`3 <9899_7.12.12.1p3>` The fdim functions return the positive difference value.

