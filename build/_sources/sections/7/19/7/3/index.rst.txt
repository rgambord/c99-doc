.. _9899_7.19.7.3:

7.19.7.3 The fputc function
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.7.3p1:

.. container:: snum

   :ref:`1 <9899_7.19.7.3p1>`



::

    #include <stdio.h>
    int fputc(int c, FILE *stream);

.. rubric:: Description

.. _9899_7.19.7.3p2:

.. container:: snum

   :ref:`2 <9899_7.19.7.3p2>`

The fputc function writes the character specified by c (converted to an unsigned char) to the output stream pointed to by stream, at the position indicated by the associated file position indicator for the stream (if defined), and advances the indicator appropriately. If the file cannot support positioning requests, or if the stream was opened with append mode, the character is appended to the output stream.

.. rubric:: Returns

.. _9899_7.19.7.3p3:

.. container:: snum

   :ref:`3 <9899_7.19.7.3p3>`

The fputc function returns the character written. If a write error occurs, the error indicator for the stream is set and fputc returns EOF.

