.. _9899_7.12.9.5:

7.12.9.5 The lrint and llrint functions
'''''''''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.9.5p1:

.. container:: snum

   :ref:`1 <9899_7.12.9.5p1>`



::

    #include <math.h>
    long int lrint(double x);
    long int lrintf(float x);
    long int lrintl(long double x);
    long long int llrint(double x);
    long long int llrintf(float x);
    long long int llrintl(long double x);

.. rubric:: Description

.. _9899_7.12.9.5p2:

.. container:: snum

   :ref:`2 <9899_7.12.9.5p2>`

The lrint and llrint functions round their argument to the nearest integer value, rounding according to the current rounding direction. If the rounded value is outside the range of the return type, the numeric result is unspecified and a domain error or range error may occur. \*

.. rubric:: Returns

.. _9899_7.12.9.5p3:

.. container:: snum

   :ref:`3 <9899_7.12.9.5p3>`

The lrint and llrint functions return the rounded integer value.

