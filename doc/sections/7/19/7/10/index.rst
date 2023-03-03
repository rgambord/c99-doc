.. _9899_7.19.7.10:

7.19.7.10 The puts function
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.7.10p1:

:ref:`1 <9899_7.19.7.10p1>`

::

    #include <stdio.h>
    int puts(const char *s);

.. rubric:: Description

.. _9899_7.19.7.10p2:

:ref:`2 <9899_7.19.7.10p2>` The puts function writes the string pointed to by s to the stream pointed to by stdout, and appends a new-line character to the output. The terminating null character is not written.

.. rubric:: Returns

.. _9899_7.19.7.10p3:

:ref:`3 <9899_7.19.7.10p3>` The puts function returns EOF if a write error occurs; otherwise it returns a nonnegative value.

