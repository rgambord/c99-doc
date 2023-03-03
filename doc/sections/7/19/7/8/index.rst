.. _9899_7.19.7.8:

7.19.7.8 The putc function
''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.7.8p1:

:ref:`1 <9899_7.19.7.8p1>`

::

    #include <stdio.h>
    int putc(int c, FILE *stream);

.. rubric:: Description

.. _9899_7.19.7.8p2:

:ref:`2 <9899_7.19.7.8p2>` The putc function is equivalent to fputc, except that if it is implemented as a macro, it may evaluate stream more than once, so that argument should never be an expression with side effects.

.. rubric:: Returns

.. _9899_7.19.7.8p3:

:ref:`3 <9899_7.19.7.8p3>` The putc function returns the character written. If a write error occurs, the error indicator for the stream is set and putc returns EOF.

