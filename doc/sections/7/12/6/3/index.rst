.. _9899_7.12.6.3:

7.12.6.3 The expm1 functions
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.6.3p1:

:ref:`1 <9899_7.12.6.3p1>`

::

    #include <math.h>
    double expm1(double x);
    float expm1f(float x);
    long double expm1l(long double x);

.. rubric:: Description

.. _9899_7.12.6.3p2:

:ref:`2 <9899_7.12.6.3p2>` The expm1 functions compute the base-e exponential of the argument, minus 1. A range error occurs if x is too large.\ [#9899_note208]_

.. rubric:: Returns

.. _9899_7.12.6.3p3:

:ref:`3 <9899_7.12.6.3p3>` The expm1 functions return e\ :sup:`x` - 1.





.. rubric:: Footnotes

.. [#9899_note208] For small magnitude x, expm1(x) is expected to be more accurate than exp(x) - 1.
