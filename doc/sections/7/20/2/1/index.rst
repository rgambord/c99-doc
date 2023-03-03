.. _9899_7.20.2.1:

7.20.2.1 The rand function
''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.2.1p1:

:ref:`1 <9899_7.20.2.1p1>`

::

    #include <stdlib.h>
    int rand(void);

.. rubric:: Description

.. _9899_7.20.2.1p2:

:ref:`2 <9899_7.20.2.1p2>` The rand function computes a sequence of pseudo-random integers in the range 0 to RAND_MAX.

.. _9899_7.20.2.1p3:

:ref:`3 <9899_7.20.2.1p3>` The implementation shall behave as if no library function calls the rand function.

.. rubric:: Returns

.. _9899_7.20.2.1p4:

:ref:`4 <9899_7.20.2.1p4>` The rand function returns a pseudo-random integer.

.. rubric:: Environmental limits

.. _9899_7.20.2.1p5:

:ref:`5 <9899_7.20.2.1p5>` The value of the RAND_MAX macro shall be at least 32767.

