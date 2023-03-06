.. _9899_7.19.9.5:

7.19.9.5 The rewind function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.9.5p1:

.. container:: snum

   :ref:`1 <9899_7.19.9.5p1>`



::

    #include <stdio.h>
    void rewind(FILE *stream);

.. rubric:: Description

.. _9899_7.19.9.5p2:

.. container:: snum

   :ref:`2 <9899_7.19.9.5p2>`

The rewind function sets the file position indicator for the stream pointed to by stream to the beginning of the file. It is equivalent to

::

    (void)fseek(stream, 0L, SEEK_SET)

except that the error indicator for the stream is also cleared.

.. rubric:: Returns

.. _9899_7.19.9.5p3:

.. container:: snum

   :ref:`3 <9899_7.19.9.5p3>`

The rewind function returns no value.

