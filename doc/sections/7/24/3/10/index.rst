.. _9899_7.24.3.10:

7.24.3.10 The ungetwc function
''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.24.3.10p1:

:ref:`1 <9899_7.24.3.10p1>`

::

    #include <stdio.h>
    #include <wchar.h>
    wint_t ungetwc(wint_t c, FILE *stream);

.. rubric:: Description

.. _9899_7.24.3.10p2:

:ref:`2 <9899_7.24.3.10p2>` The ungetwc function pushes the wide character specified by c back onto the input stream pointed to by stream. Pushed-back wide characters will be returned by subsequent reads on that stream in the reverse order of their pushing. A successful intervening call (with the stream pointed to by stream) to a file positioning function (fseek, fsetpos, or rewind) discards any pushed-back wide characters for the stream. The external storage corresponding to the stream is unchanged.

.. _9899_7.24.3.10p3:

:ref:`3 <9899_7.24.3.10p3>` One wide character of pushback is guaranteed, even if the call to the ungetwc function follows just after a call to a formatted wide character input function fwscanf, vfwscanf, vwscanf, or wscanf. If the ungetwc function is called too many times on the same stream without an intervening read or file positioning operation on that stream, the operation may fail.

.. _9899_7.24.3.10p4:

:ref:`4 <9899_7.24.3.10p4>` If the value of c equals that of the macro WEOF, the operation fails and the input stream is unchanged.

.. _9899_7.24.3.10p5:

:ref:`5 <9899_7.24.3.10p5>` A successful call to the ungetwc function clears the end-of-file indicator for the stream. The value of the file position indicator for the stream after reading or discarding all pushed-back wide characters is the same as it was before the wide characters were pushed back. For a text or binary stream, the value of its file position indicator after a successful call to the ungetwc function is unspecified until all pushed-back wide characters are read or discarded.

.. rubric:: Returns

.. _9899_7.24.3.10p6:

:ref:`6 <9899_7.24.3.10p6>` The ungetwc function returns the wide character pushed back, or WEOF if the operation fails.

