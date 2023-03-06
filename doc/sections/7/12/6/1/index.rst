.. _9899_7.12.6.1:

7.12.6.1 The exp functions
''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.6.1p1:

.. container:: snum

   :ref:`1 <9899_7.12.6.1p1>`



::

    #include <math.h>
    double exp(double x);
    float expf(float x);
    long double expl(long double x);

.. rubric:: Description

.. _9899_7.12.6.1p2:

.. container:: snum

   :ref:`2 <9899_7.12.6.1p2>`

The exp functions compute the base-e exponential of x. A range error occurs if the magnitude of x is too large.

.. rubric:: Returns

.. _9899_7.12.6.1p3:

.. container:: snum

   :ref:`3 <9899_7.12.6.1p3>`

The exp functions return e\ :sup:`x`.

