.. _9899_7.12.6.2:

7.12.6.2 The exp2 functions
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.6.2p1:

.. container:: snum

   :ref:`1 <9899_7.12.6.2p1>`



::

    #include <math.h>
    double exp2(double x);
    float exp2f(float x);
    long double exp2l(long double x);

.. rubric:: Description

.. _9899_7.12.6.2p2:

.. container:: snum

   :ref:`2 <9899_7.12.6.2p2>`

The exp2 functions compute the base-2 exponential of x. A range error occurs if the magnitude of x is too large.

.. rubric:: Returns

.. _9899_7.12.6.2p3:

.. container:: snum

   :ref:`3 <9899_7.12.6.2p3>`

The exp2 functions return 2\ :sup:`x`.

