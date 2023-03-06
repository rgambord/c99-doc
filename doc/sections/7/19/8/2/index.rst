.. _9899_7.19.8.2:

7.19.8.2 The fwrite function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.8.2p1:

.. container:: snum

   :ref:`1 <9899_7.19.8.2p1>`



::

    #include <stdio.h>
    size_t fwrite(const void * restrict ptr,
         size_t size, size_t nmemb,
         FILE * restrict stream);

.. rubric:: Description

.. _9899_7.19.8.2p2:

.. container:: snum

   :ref:`2 <9899_7.19.8.2p2>`

The fwrite function writes, from the array pointed to by ptr, up to nmemb elements whose size is specified by size, to the stream pointed to by stream. For each object, size calls are made to the fputc function, taking the values (in order) from an array of unsigned char exactly overlaying the object. The file position indicator for the stream (if defined) is advanced by the number of characters successfully written. If an error occurs, the resulting value of the file position indicator for the stream is indeterminate.

.. rubric:: Returns

.. _9899_7.19.8.2p3:

.. container:: snum

   :ref:`3 <9899_7.19.8.2p3>`

The fwrite function returns the number of elements successfully written, which will be less than nmemb only if a write error is encountered. If size or nmemb is zero, fwrite returns zero and the state of the stream remains unchanged.

