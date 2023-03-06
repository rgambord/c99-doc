.. _9899_7.19.8.1:

7.19.8.1 The fread function
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.8.1p1:

.. container:: snum

   :ref:`1 <9899_7.19.8.1p1>`



::

    #include <stdio.h>
    size_t fread(void * restrict ptr,
         size_t size, size_t nmemb,
         FILE * restrict stream);

.. rubric:: Description

.. _9899_7.19.8.1p2:

.. container:: snum

   :ref:`2 <9899_7.19.8.1p2>`

The fread function reads, into the array pointed to by ptr, up to nmemb elements whose size is specified by size, from the stream pointed to by stream. For each object, size calls are made to the fgetc function and the results stored, in the order read, in an array of unsigned char exactly overlaying the object. The file position indicator for the stream (if defined) is advanced by the number of characters successfully read. If an error occurs, the resulting value of the file position indicator for the stream is indeterminate. If a partial element is read, its value is indeterminate.

.. rubric:: Returns

.. _9899_7.19.8.1p3:

.. container:: snum

   :ref:`3 <9899_7.19.8.1p3>`

The fread function returns the number of elements successfully read, which may be less than nmemb if a read error or end-of-file is encountered. If size or nmemb is zero, fread returns zero and the contents of the array and the state of the stream remain unchanged.

