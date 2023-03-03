.. _9899_7.12.14.2:

7.12.14.2 The isgreaterequal macro
''''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.14.2p1:

:ref:`1 <9899_7.12.14.2p1>`

::

    #include <math.h>
    int isgreaterequal(real-floating x, real-floating y);

.. rubric:: Description

.. _9899_7.12.14.2p2:

:ref:`2 <9899_7.12.14.2p2>` The isgreaterequal macro determines whether its first argument is greater than or equal to its second argument. The value of isgreaterequal(x, y) is always equal to (x) >= (y); however, unlike (x) >= (y), isgreaterequal(x, y) does not raise the ''invalid'' floating-point exception when x and y are unordered.

.. rubric:: Returns

.. _9899_7.12.14.2p3:

:ref:`3 <9899_7.12.14.2p3>` The isgreaterequal macro returns the value of (x) >= (y).

