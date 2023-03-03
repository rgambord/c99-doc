.. _9899_7.19.6.7:

7.19.6.7 The sscanf function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.6.7p1:

:ref:`1 <9899_7.19.6.7p1>`

::

    #include <stdio.h>
    int sscanf(const char * restrict s,
         const char * restrict format, ...);

.. rubric:: Description

.. _9899_7.19.6.7p2:

:ref:`2 <9899_7.19.6.7p2>` The sscanf function is equivalent to fscanf, except that input is obtained from a string (specified by the argument s) rather than from a stream. Reaching the end of the string is equivalent to encountering end-of-file for the fscanf function. If copying takes place between objects that overlap, the behavior is undefined.

.. rubric:: Returns

.. _9899_7.19.6.7p3:

:ref:`3 <9899_7.19.6.7p3>` The sscanf function returns the value of the macro EOF if an input failure occurs before any conversion. Otherwise, the sscanf function returns the number of input items assigned, which can be fewer than provided for, or even zero, in the event of an early matching failure.

