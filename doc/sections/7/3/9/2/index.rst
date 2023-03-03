.. _9899_7.3.9.2:

7.3.9.2 The cimag functions
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.3.9.2p1:

:ref:`1 <9899_7.3.9.2p1>`

::

    #include <complex.h>
    double cimag(double complex z);
    float cimagf(float complex z);
    long double cimagl(long double complex z);

.. rubric:: Description

.. _9899_7.3.9.2p2:

:ref:`2 <9899_7.3.9.2p2>` The cimag functions compute the imaginary part of z.\ [#9899_note170]_

.. rubric:: Returns

.. _9899_7.3.9.2p3:

:ref:`3 <9899_7.3.9.2p3>` The cimag functions return the imaginary part value (as a real).





.. rubric:: Footnotes

.. [#9899_note170] For a variable z of complex type, z == creal(z) + cimag(z)*I.
