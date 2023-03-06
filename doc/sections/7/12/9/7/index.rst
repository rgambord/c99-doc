.. _9899_7.12.9.7:

7.12.9.7 The lround and llround functions
'''''''''''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.9.7p1:

.. container:: snum

   :ref:`1 <9899_7.12.9.7p1>`



::

    #include <math.h>
    long int lround(double x);
    long int lroundf(float x);
    long int lroundl(long double x);
    long long int llround(double x);
    long long int llroundf(float x);
    long long int llroundl(long double x);

.. rubric:: Description

.. _9899_7.12.9.7p2:

.. container:: snum

   :ref:`2 <9899_7.12.9.7p2>`

The lround and llround functions round their argument to the nearest integer value, rounding halfway cases away from zero, regardless of the current rounding direction. If the rounded value is outside the range of the return type, the numeric result is unspecified and a domain error or range error may occur.

.. rubric:: Returns

.. _9899_7.12.9.7p3:

.. container:: snum

   :ref:`3 <9899_7.12.9.7p3>`

The lround and llround functions return the rounded integer value.

