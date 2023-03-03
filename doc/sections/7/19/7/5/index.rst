.. _9899_7.19.7.5:

7.19.7.5 The getc function
''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.7.5p1:

:ref:`1 <9899_7.19.7.5p1>`

::

    #include <stdio.h>
    int getc(FILE *stream);

.. rubric:: Description

.. _9899_7.19.7.5p2:

:ref:`2 <9899_7.19.7.5p2>` The getc function is equivalent to fgetc, except that if it is implemented as a macro, it may evaluate stream more than once, so the argument should never be an expression with side effects.

.. rubric:: Returns

.. _9899_7.19.7.5p3:

:ref:`3 <9899_7.19.7.5p3>` The getc function returns the next character from the input stream pointed to by stream. If the stream is at end-of-file, the end-of-file indicator for the stream is set and getc returns EOF. If a read error occurs, the error indicator for the stream is set and getc returns EOF.

