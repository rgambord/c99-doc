.. _9899_7.19.6.4:

7.19.6.4 The scanf function
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.6.4p1:

:ref:`1 <9899_7.19.6.4p1>`

::

    #include <stdio.h>
    int scanf(const char * restrict format, ...);

.. rubric:: Description

.. _9899_7.19.6.4p2:

:ref:`2 <9899_7.19.6.4p2>` The scanf function is equivalent to fscanf with the argument stdin interposed before the arguments to scanf.

.. rubric:: Returns

.. _9899_7.19.6.4p3:

:ref:`3 <9899_7.19.6.4p3>` The scanf function returns the value of the macro EOF if an input failure occurs before any conversion. Otherwise, the scanf function returns the number of input items assigned, which can be fewer than provided for, or even zero, in the event of an early matching failure.

