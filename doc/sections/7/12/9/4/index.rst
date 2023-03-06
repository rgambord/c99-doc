.. _9899_7.12.9.4:

7.12.9.4 The rint functions
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.9.4p1:

.. container:: snum

   :ref:`1 <9899_7.12.9.4p1>`



::

    #include <math.h>
    double rint(double x);
    float rintf(float x);
    long double rintl(long double x);

.. rubric:: Description

.. _9899_7.12.9.4p2:

.. container:: snum

   :ref:`2 <9899_7.12.9.4p2>`

The rint functions differ from the nearbyint functions (:ref:`7.12.9.3 <9899_7.12.9.3>`) only in that the rint functions may raise the "inexact" floating-point exception if the result differs in value from the argument.

.. rubric:: Returns

.. _9899_7.12.9.4p3:

.. container:: snum

   :ref:`3 <9899_7.12.9.4p3>`

The rint functions return the rounded integer value.

