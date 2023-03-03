.. _9899_7.19.5.2:

7.19.5.2 The fflush function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.5.2p1:

:ref:`1 <9899_7.19.5.2p1>`

::

    #include <stdio.h>
    int fflush(FILE *stream);

.. rubric:: Description

.. _9899_7.19.5.2p2:

:ref:`2 <9899_7.19.5.2p2>` If stream points to an output stream or an update stream in which the most recent operation was not input, the fflush function causes any unwritten data for that stream to be delivered to the host environment to be written to the file; otherwise, the behavior is undefined.

.. _9899_7.19.5.2p3:

:ref:`3 <9899_7.19.5.2p3>` If stream is a null pointer, the fflush function performs this flushing action on all streams for which the behavior is defined above.

.. rubric:: Returns

.. _9899_7.19.5.2p4:

:ref:`4 <9899_7.19.5.2p4>` The fflush function sets the error indicator for the stream and returns EOF if a write error occurs, otherwise it returns zero.

**Forward references**: the fopen function (:ref:`7.19.5.3 <9899_7.19.5.3>`).

