.. _9899_7.12.6.9:

7.12.6.9 The log1p functions
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.6.9p1:

.. container:: snum

   :ref:`1 <9899_7.12.6.9p1>`



::

    #include <math.h>
    double log1p(double x);
    float log1pf(float x);
    long double log1pl(long double x);

.. rubric:: Description

.. _9899_7.12.6.9p2:

.. container:: snum

   :ref:`2 <9899_7.12.6.9p2>`

The log1p functions compute the base-e (natural) logarithm of 1 plus the argument.\ [#9899_note209]_ A domain error occurs if the argument is less than -1. A range error may occur if the argument equals -1.

.. rubric:: Returns

.. _9899_7.12.6.9p3:

.. container:: snum

   :ref:`3 <9899_7.12.6.9p3>`

The log1p functions return loge (1 + x).





.. rubric:: Footnotes

.. [#9899_note209] For small magnitude x, log1p(x) is expected to be more accurate than log(1 + x).
