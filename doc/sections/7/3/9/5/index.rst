.. _9899_7.3.9.5:

7.3.9.5 The creal functions
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.3.9.5p1:

:ref:`1 <9899_7.3.9.5p1>`

::

    #include <complex.h>
    double creal(double complex z);
    float crealf(float complex z);
    long double creall(long double complex z);

.. rubric:: Description

.. _9899_7.3.9.5p2:

:ref:`2 <9899_7.3.9.5p2>` The creal functions compute the real part of z.\ [#9899_note171]_

.. rubric:: Returns

.. _9899_7.3.9.5p3:

:ref:`3 <9899_7.3.9.5p3>` The creal functions return the real part value.





.. rubric:: Footnotes

.. [#9899_note171] For a variable z of complex type, z == creal(z) + cimag(z)*I.
