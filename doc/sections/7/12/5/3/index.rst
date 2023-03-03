.. _9899_7.12.5.3:

7.12.5.3 The atanh functions
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.5.3p1:

:ref:`1 <9899_7.12.5.3p1>`

::

    #include <math.h>
    double atanh(double x);
    float atanhf(float x);
    long double atanhl(long double x);

.. rubric:: Description

.. _9899_7.12.5.3p2:

:ref:`2 <9899_7.12.5.3p2>` The atanh functions compute the arc hyperbolic tangent of x. A domain error occurs for arguments not in the interval [-1, +1]. A range error may occur if the argument equals -1 or +1.

.. rubric:: Returns

.. _9899_7.12.5.3p3:

:ref:`3 <9899_7.12.5.3p3>` The atanh functions return artanh x.

