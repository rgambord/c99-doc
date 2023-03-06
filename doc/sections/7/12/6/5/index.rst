.. _9899_7.12.6.5:

7.12.6.5 The ilogb functions
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.6.5p1:

.. container:: snum

   :ref:`1 <9899_7.12.6.5p1>`



::

    #include <math.h>
    int ilogb(double x);
    int ilogbf(float x);
    int ilogbl(long double x);

.. rubric:: Description

.. _9899_7.12.6.5p2:

.. container:: snum

   :ref:`2 <9899_7.12.6.5p2>`

The ilogb functions extract the exponent of x as a signed int value. If x is zero they compute the value FP_ILOGB0; if x is infinite they compute the value INT_MAX; if x is a NaN they compute the value FP_ILOGBNAN; otherwise, they are equivalent to calling the corresponding logb function and casting the returned value to type int. A domain error or range error may occur if x is zero, infinite, or NaN. If the correct value is outside the range of the return type, the numeric result is unspecified.

.. rubric:: Returns

.. _9899_7.12.6.5p3:

.. container:: snum

   :ref:`3 <9899_7.12.6.5p3>`

The ilogb functions return the exponent of x as a signed int value.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_7.12.6.11`

