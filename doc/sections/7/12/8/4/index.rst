.. _9899_7.12.8.4:

7.12.8.4 The tgamma functions
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.8.4p1:

.. container:: snum

   :ref:`1 <9899_7.12.8.4p1>`



::

    #include <math.h>
    double tgamma(double x);
    float tgammaf(float x);
    long double tgammal(long double x);

.. rubric:: Description

.. _9899_7.12.8.4p2:

.. container:: snum

   :ref:`2 <9899_7.12.8.4p2>`

The tgamma functions compute the gamma function of x. A domain error or range error may occur if x is a negative integer or zero. A range error may occur if the magnitude of x is too large or too small.

.. rubric:: Returns

.. _9899_7.12.8.4p3:

.. container:: snum

   :ref:`3 <9899_7.12.8.4p3>`

The tgamma functions return (Gamma)(x).

