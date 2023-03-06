.. _9899_7.12.7.4:

7.12.7.4 The pow functions
''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.7.4p1:

.. container:: snum

   :ref:`1 <9899_7.12.7.4p1>`



::

    #include <math.h>
    double pow(double x, double y);
    float powf(float x, float y);
    long double powl(long double x, long double y);

.. rubric:: Description

.. _9899_7.12.7.4p2:

.. container:: snum

   :ref:`2 <9899_7.12.7.4p2>`

The pow functions compute x raised to the power y. A domain error occurs if x is finite and negative and y is finite and not an integer value. A range error may occur. A domain error may occur if x is zero and y is zero. A domain error or range error may occur if x is zero and y is less than zero.

.. rubric:: Returns

.. _9899_7.12.7.4p3:

.. container:: snum

   :ref:`3 <9899_7.12.7.4p3>`

The pow functions return x\ :sup:`y`.

