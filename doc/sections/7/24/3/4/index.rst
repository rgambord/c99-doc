.. _9899_7.24.3.4:

7.24.3.4 The fputws function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.24.3.4p1:

.. container:: snum

   :ref:`1 <9899_7.24.3.4p1>`



::

    #include <stdio.h>
    #include <wchar.h>
    int fputws(const wchar_t * restrict s,
         FILE * restrict stream);

.. rubric:: Description

.. _9899_7.24.3.4p2:

.. container:: snum

   :ref:`2 <9899_7.24.3.4p2>`

The fputws function writes the wide string pointed to by s to the stream pointed to by stream. The terminating null wide character is not written.

.. rubric:: Returns

.. _9899_7.24.3.4p3:

.. container:: snum

   :ref:`3 <9899_7.24.3.4p3>`

The fputws function returns EOF if a write or encoding error occurs; otherwise, it returns a nonnegative value.

