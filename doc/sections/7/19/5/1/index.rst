.. _9899_7.19.5.1:

7.19.5.1 The fclose function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.5.1p1:

:ref:`1 <9899_7.19.5.1p1>`

::

    #include <stdio.h>
    int fclose(FILE *stream);

.. rubric:: Description

.. _9899_7.19.5.1p2:

:ref:`2 <9899_7.19.5.1p2>` A successful call to the fclose function causes the stream pointed to by stream to be flushed and the associated file to be closed. Any unwritten buffered data for the stream are delivered to the host environment to be written to the file; any unread buffered data are discarded. Whether or not the call succeeds, the stream is disassociated from the file and any buffer set by the setbuf or setvbuf function is disassociated from the stream (and deallocated if it was automatically allocated).

.. rubric:: Returns

.. _9899_7.19.5.1p3:

:ref:`3 <9899_7.19.5.1p3>` The fclose function returns zero if the stream was successfully closed, or EOF if any errors were detected.

