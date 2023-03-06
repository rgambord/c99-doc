.. _9899_7.19.5.6:

7.19.5.6 The setvbuf function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.5.6p1:

.. container:: snum

   :ref:`1 <9899_7.19.5.6p1>`



::

    #include <stdio.h>
    int setvbuf(FILE * restrict stream,
         char * restrict buf,
         int mode, size_t size);

.. rubric:: Description

.. _9899_7.19.5.6p2:

.. container:: snum

   :ref:`2 <9899_7.19.5.6p2>`

The setvbuf function may be used only after the stream pointed to by stream has been associated with an open file and before any other operation (other than an unsuccessful call to setvbuf) is performed on the stream. The argument mode determines how stream will be buffered, as follows: \_IOFBF causes input/output to be fully buffered; \_IOLBF causes input/output to be line buffered; \_IONBF causes input/output to be unbuffered. If buf is not a null pointer, the array it points to may be used instead of a buffer allocated by the setvbuf function\ [#9899_note239]_ and the argument size specifies the size of the array; otherwise, size may determine the size of a buffer allocated by the setvbuf function. The contents of the array at any time are indeterminate.

.. rubric:: Returns

.. _9899_7.19.5.6p3:

.. container:: snum

   :ref:`3 <9899_7.19.5.6p3>`

The setvbuf function returns zero on success, or nonzero if an invalid value is given for mode or if the request cannot be honored.





.. rubric:: Footnotes

.. [#9899_note239] The buffer has to have a lifetime at least as great as the open stream, so the stream should be closed before a buffer that has automatic storage duration is deallocated upon block exit.
