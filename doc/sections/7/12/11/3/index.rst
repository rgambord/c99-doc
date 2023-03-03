.. _9899_7.12.11.3:

7.12.11.3 The nextafter functions
'''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.11.3p1:

:ref:`1 <9899_7.12.11.3p1>`

::

    #include <math.h>
    double nextafter(double x, double y);
    float nextafterf(float x, float y);
    long double nextafterl(long double x, long double y);

.. rubric:: Description

.. _9899_7.12.11.3p2:

:ref:`2 <9899_7.12.11.3p2>` The nextafter functions determine the next representable value, in the type of the function, after x in the direction of y, where x and y are first converted to the type of the function.\ [#9899_note211]_ The nextafter functions return y if x equals y. A range error may occur if the magnitude of x is the largest finite value representable in the type and the result is infinite or not representable in the type.

.. rubric:: Returns

.. _9899_7.12.11.3p3:

:ref:`3 <9899_7.12.11.3p3>` The nextafter functions return the next representable value in the specified format after x in the direction of y.





.. rubric:: Footnotes

.. [#9899_note211] The argument values are converted to the type of the function, even by a macro implementation of the function.
