.. _9899_7.19.9.3:

7.19.9.3 The fsetpos function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.9.3p1:

.. container:: snum

   :ref:`1 <9899_7.19.9.3p1>`



::

    #include <stdio.h>
    int fsetpos(FILE *stream, const fpos_t *pos);

.. rubric:: Description

.. _9899_7.19.9.3p2:

.. container:: snum

   :ref:`2 <9899_7.19.9.3p2>`

The fsetpos function sets the mbstate_t object (if any) and file position indicator for the stream pointed to by stream according to the value of the object pointed to by pos, which shall be a value obtained from an earlier successful call to the fgetpos function on a stream associated with the same file. If a read or write error occurs, the error indicator for the stream is set and fsetpos fails.

.. _9899_7.19.9.3p3:

.. container:: snum

   :ref:`3 <9899_7.19.9.3p3>`

A successful call to the fsetpos function undoes any effects of the ungetc function on the stream, clears the end-of-file indicator for the stream, and then establishes the new parse state and position. After a successful fsetpos call, the next operation on an update stream may be either input or output.

.. rubric:: Returns

.. _9899_7.19.9.3p4:

.. container:: snum

   :ref:`4 <9899_7.19.9.3p4>`

If successful, the fsetpos function returns zero; on failure, the fsetpos function returns nonzero and stores an implementation-defined positive value in errno.

