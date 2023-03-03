.. _9899_7.12.6.12:

7.12.6.12 The modf functions
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.6.12p1:

:ref:`1 <9899_7.12.6.12p1>`

::

    #include <math.h>
    double modf(double value, double *iptr);
    float modff(float value, float *iptr);
    long double modfl(long double value, long double *iptr);

.. rubric:: Description

.. _9899_7.12.6.12p2:

:ref:`2 <9899_7.12.6.12p2>` The modf functions break the argument value into integral and fractional parts, each of which has the same type and sign as the argument. They store the integral part (in floating-point format) in the object pointed to by iptr.

.. rubric:: Returns

.. _9899_7.12.6.12p3:

:ref:`3 <9899_7.12.6.12p3>` The modf functions return the signed fractional part of value.

