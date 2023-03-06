.. _9899_7.12.10.2:

7.12.10.2 The remainder functions
'''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.10.2p1:

.. container:: snum

   :ref:`1 <9899_7.12.10.2p1>`



::

    #include <math.h>
    double remainder(double x, double y);
    float remainderf(float x, float y);
    long double remainderl(long double x, long double y);

.. rubric:: Description

.. _9899_7.12.10.2p2:

.. container:: snum

   :ref:`2 <9899_7.12.10.2p2>`

The remainder functions compute the remainder x REM y required by IEC 60559.\ [#9899_note210]_

.. rubric:: Returns

.. _9899_7.12.10.2p3:

.. container:: snum

   :ref:`3 <9899_7.12.10.2p3>`

The remainder functions return x REM y. If y is zero, whether a domain error occurs or the functions return zero is implementation defined.





.. rubric:: Footnotes

.. [#9899_note210] "When y != 0, the remainder r = x REM y is defined regardless of the rounding mode by the mathematical relation r = x - ny, where n is the integer nearest the exact value of x/y; whenever \| n - x/y \| = 1/2, then n is even. Thus, the remainder is always exact. If r = 0, its sign shall be that of x.'' This definition is applicable for all implementations.
