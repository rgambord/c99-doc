.. _9899_7.12.5.1:

7.12.5.1 The acosh functions
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.5.1p1:

.. container:: snum

   :ref:`1 <9899_7.12.5.1p1>`



::

    #include <math.h>
    double acosh(double x);
    float acoshf(float x);
    long double acoshl(long double x);

.. rubric:: Description

.. _9899_7.12.5.1p2:

.. container:: snum

   :ref:`2 <9899_7.12.5.1p2>`

The acosh functions compute the (nonnegative) arc hyperbolic cosine of x. A domain error occurs for arguments less than 1.

.. rubric:: Returns

.. _9899_7.12.5.1p3:

.. container:: snum

   :ref:`3 <9899_7.12.5.1p3>`

The acosh functions return arcosh x in the interval [0, +(inf)].

