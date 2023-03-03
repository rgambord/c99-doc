.. _9899_7.19.7.1:

7.19.7.1 The fgetc function
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.7.1p1:

:ref:`1 <9899_7.19.7.1p1>`

::

    #include <stdio.h>
    int fgetc(FILE *stream);

.. rubric:: Description

.. _9899_7.19.7.1p2:

:ref:`2 <9899_7.19.7.1p2>` If the end-of-file indicator for the input stream pointed to by stream is not set and a next character is present, the fgetc function obtains that character as an unsigned char converted to an int and advances the associated file position indicator for the stream (if defined).

.. rubric:: Returns

.. _9899_7.19.7.1p3:

:ref:`3 <9899_7.19.7.1p3>` If the end-of-file indicator for the stream is set, or if the stream is at end-of-file, the end- of-file indicator for the stream is set and the fgetc function returns EOF. Otherwise, the fgetc function returns the next character from the input stream pointed to by stream. If a read error occurs, the error indicator for the stream is set and the fgetc function returns EOF.\ [#9899_note255]_





.. rubric:: Footnotes

.. [#9899_note255] An end-of-file and a read error can be distinguished by use of the feof and ferror functions.
