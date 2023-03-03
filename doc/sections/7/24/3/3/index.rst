.. _9899_7.24.3.3:

7.24.3.3 The fputwc function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.24.3.3p1:

:ref:`1 <9899_7.24.3.3p1>`

::

    #include <stdio.h>
    #include <wchar.h>
    wint_t fputwc(wchar_t c, FILE *stream);

.. rubric:: Description

.. _9899_7.24.3.3p2:

:ref:`2 <9899_7.24.3.3p2>` The fputwc function writes the wide character specified by c to the output stream pointed to by stream, at the position indicated by the associated file position indicator for the stream (if defined), and advances the indicator appropriately. If the file cannot support positioning requests, or if the stream was opened with append mode, the character is appended to the output stream.

.. rubric:: Returns

.. _9899_7.24.3.3p3:

:ref:`3 <9899_7.24.3.3p3>` The fputwc function returns the wide character written. If a write error occurs, the error indicator for the stream is set and fputwc returns WEOF. If an encoding error occurs, the value of the macro EILSEQ is stored in errno and fputwc returns WEOF.

