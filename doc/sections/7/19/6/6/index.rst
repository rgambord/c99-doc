.. _9899_7.19.6.6:

7.19.6.6 The sprintf function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.6.6p1:

:ref:`1 <9899_7.19.6.6p1>`

::

    #include <stdio.h>
    int sprintf(char * restrict s,
         const char * restrict format, ...);

.. rubric:: Description

.. _9899_7.19.6.6p2:

:ref:`2 <9899_7.19.6.6p2>` The sprintf function is equivalent to fprintf, except that the output is written into an array (specified by the argument s) rather than to a stream. A null character is written at the end of the characters written; it is not counted as part of the returned value. If copying takes place between objects that overlap, the behavior is undefined.

.. rubric:: Returns

.. _9899_7.19.6.6p3:

:ref:`3 <9899_7.19.6.6p3>` The sprintf function returns the number of characters written in the array, not counting the terminating null character, or a negative value if an encoding error occurred.

