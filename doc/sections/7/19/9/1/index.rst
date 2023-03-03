.. _9899_7.19.9.1:

7.19.9.1 The fgetpos function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.9.1p1:

:ref:`1 <9899_7.19.9.1p1>`

::

    #include <stdio.h>
    int fgetpos(FILE * restrict stream,
         fpos_t * restrict pos);

.. rubric:: Description

.. _9899_7.19.9.1p2:

:ref:`2 <9899_7.19.9.1p2>` The fgetpos function stores the current values of the parse state (if any) and file position indicator for the stream pointed to by stream in the object pointed to by pos. The values stored contain unspecified information usable by the fsetpos function for repositioning the stream to its position at the time of the call to the fgetpos function.

.. rubric:: Returns

.. _9899_7.19.9.1p3:

:ref:`3 <9899_7.19.9.1p3>` If successful, the fgetpos function returns zero; on failure, the fgetpos function returns nonzero and stores an implementation-defined positive value in errno.

**Forward references**: the fsetpos function (:ref:`7.19.9.3 <9899_7.19.9.3>`).

