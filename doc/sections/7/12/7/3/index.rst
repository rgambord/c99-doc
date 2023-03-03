.. _9899_7.12.7.3:

7.12.7.3 The hypot functions
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.7.3p1:

:ref:`1 <9899_7.12.7.3p1>`

::

    #include <math.h>
    double hypot(double x, double y);
    float hypotf(float x, float y);
    long double hypotl(long double x, long double y);

.. rubric:: Description

.. _9899_7.12.7.3p2:

:ref:`2 <9899_7.12.7.3p2>` The hypot functions compute the square root of the sum of the squares of x and y, without undue overflow or underflow. A range error may occur.

.. _9899_7.12.7.3p3:

:ref:`3 <9899_7.12.7.3p3>`

.. rubric:: Returns

.. _9899_7.12.7.3p4:

:ref:`4 <9899_7.12.7.3p4>` The hypot functions return (sqrt)(x\ :sup:`2` + y\ :sup:`2`).

