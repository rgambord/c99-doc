.. _9899_7.24.3.1:

7.24.3.1 The fgetwc function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.24.3.1p1:

.. container:: snum

   :ref:`1 <9899_7.24.3.1p1>`



::

    #include <stdio.h>
    #include <wchar.h>
    wint_t fgetwc(FILE *stream);

.. rubric:: Description

.. _9899_7.24.3.1p2:

.. container:: snum

   :ref:`2 <9899_7.24.3.1p2>`

If the end-of-file indicator for the input stream pointed to by stream is not set and a next wide character is present, the fgetwc function obtains that wide character as a wchar_t converted to a wint_t and advances the associated file position indicator for the stream (if defined).

.. rubric:: Returns

.. _9899_7.24.3.1p3:

.. container:: snum

   :ref:`3 <9899_7.24.3.1p3>`

If the end-of-file indicator for the stream is set, or if the stream is at end-of-file, the end- of-file indicator for the stream is set and the fgetwc function returns WEOF. Otherwise, the fgetwc function returns the next wide character from the input stream pointed to by stream. If a read error occurs, the error indicator for the stream is set and the fgetwc function returns WEOF. If an encoding error occurs (including too few bytes), the value of the macro EILSEQ is stored in errno and the fgetwc function returns WEOF.\ [#9899_note292]_





.. rubric:: Footnotes

.. [#9899_note292] An end-of-file and a read error can be distinguished by use of the feof and ferror functions. Also, errno will be set to EILSEQ by input/output functions only if an encoding error occurs.
