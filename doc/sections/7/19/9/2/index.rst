.. _9899_7.19.9.2:

7.19.9.2 The fseek function
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.9.2p1:

:ref:`1 <9899_7.19.9.2p1>`

::

    #include <stdio.h>
    int fseek(FILE *stream, long int offset, int whence);

.. rubric:: Description

.. _9899_7.19.9.2p2:

:ref:`2 <9899_7.19.9.2p2>` The fseek function sets the file position indicator for the stream pointed to by stream. If a read or write error occurs, the error indicator for the stream is set and fseek fails.

.. _9899_7.19.9.2p3:

:ref:`3 <9899_7.19.9.2p3>` For a binary stream, the new position, measured in characters from the beginning of the file, is obtained by adding offset to the position specified by whence. The specified position is the beginning of the file if whence is SEEK_SET, the current value of the file position indicator if SEEK_CUR, or end-of-file if SEEK_END. A binary stream need not meaningfully support fseek calls with a whence value of SEEK_END.

.. _9899_7.19.9.2p4:

:ref:`4 <9899_7.19.9.2p4>` For a text stream, either offset shall be zero, or offset shall be a value returned by an earlier successful call to the ftell function on a stream associated with the same file and whence shall be SEEK_SET.

.. _9899_7.19.9.2p5:

:ref:`5 <9899_7.19.9.2p5>` After determining the new position, a successful call to the fseek function undoes any effects of the ungetc function on the stream, clears the end-of-file indicator for the stream, and then establishes the new position. After a successful fseek call, the next operation on an update stream may be either input or output.

.. rubric:: Returns

.. _9899_7.19.9.2p6:

:ref:`6 <9899_7.19.9.2p6>` The fseek function returns nonzero only for a request that cannot be satisfied.

**Forward references**: the ftell function (:ref:`7.19.9.4 <9899_7.19.9.4>`).

