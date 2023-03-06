.. _9899_7.19.9.4:

7.19.9.4 The ftell function
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.9.4p1:

.. container:: snum

   :ref:`1 <9899_7.19.9.4p1>`



::

    #include <stdio.h>
    long int ftell(FILE *stream);

.. rubric:: Description

.. _9899_7.19.9.4p2:

.. container:: snum

   :ref:`2 <9899_7.19.9.4p2>`

The ftell function obtains the current value of the file position indicator for the stream pointed to by stream. For a binary stream, the value is the number of characters from the beginning of the file. For a text stream, its file position indicator contains unspecified information, usable by the fseek function for returning the file position indicator for the stream to its position at the time of the ftell call; the difference between two such return values is not necessarily a meaningful measure of the number of characters written or read.

.. rubric:: Returns

.. _9899_7.19.9.4p3:

.. container:: snum

   :ref:`3 <9899_7.19.9.4p3>`

If successful, the ftell function returns the current value of the file position indicator for the stream. On failure, the ftell function returns -1L and stores an implementation-defined positive value in errno.

