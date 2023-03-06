.. _9899_7.19.5.4:

7.19.5.4 The freopen function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.5.4p1:

.. container:: snum

   :ref:`1 <9899_7.19.5.4p1>`



::

    #include <stdio.h>
    FILE *freopen(const char * restrict filename,
         const char * restrict mode,
         FILE * restrict stream);

.. rubric:: Description

.. _9899_7.19.5.4p2:

.. container:: snum

   :ref:`2 <9899_7.19.5.4p2>`

The freopen function opens the file whose name is the string pointed to by filename and associates the stream pointed to by stream with it. The mode argument is used just as in the fopen function.\ [#9899_note238]_

.. _9899_7.19.5.4p3:

.. container:: snum

   :ref:`3 <9899_7.19.5.4p3>`

If filename is a null pointer, the freopen function attempts to change the mode of the stream to that specified by mode, as if the name of the file currently associated with the stream had been used. It is implementation-defined which changes of mode are permitted (if any), and under what circumstances.

.. _9899_7.19.5.4p4:

.. container:: snum

   :ref:`4 <9899_7.19.5.4p4>`

The freopen function first attempts to close any file that is associated with the specified stream. Failure to close the file is ignored. The error and end-of-file indicators for the stream are cleared.

.. rubric:: Returns

.. _9899_7.19.5.4p5:

.. container:: snum

   :ref:`5 <9899_7.19.5.4p5>`

The freopen function returns a null pointer if the open operation fails. Otherwise, freopen returns the value of stream.





.. rubric:: Footnotes

.. [#9899_note238] The primary use of the freopen function is to change the file associated with a standard text stream (stderr, stdin, or stdout), as those identifiers need not be modifiable lvalues to which the value returned by the fopen function may be assigned.
