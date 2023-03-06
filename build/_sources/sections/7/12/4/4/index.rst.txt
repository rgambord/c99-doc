.. _9899_7.12.4.4:

7.12.4.4 The atan2 functions
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.4.4p1:

.. container:: snum

   :ref:`1 <9899_7.12.4.4p1>`



::

    #include <math.h>
    double atan2(double y, double x);
    float atan2f(float y, float x);
    long double atan2l(long double y, long double x);

.. rubric:: Description

.. _9899_7.12.4.4p2:

.. container:: snum

   :ref:`2 <9899_7.12.4.4p2>`

The atan2 functions compute the value of the arc tangent of y/x, using the signs of both arguments to determine the quadrant of the return value. A domain error may occur if both arguments are zero.

.. rubric:: Returns

.. _9899_7.12.4.4p3:

.. container:: snum

   :ref:`3 <9899_7.12.4.4p3>`

The atan2 functions return arctan y/x in the interval [-pi , +pi ] radians.

