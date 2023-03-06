.. _9899_7.19.7.9:

7.19.7.9 The putchar function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.7.9p1:

.. container:: snum

   :ref:`1 <9899_7.19.7.9p1>`



::

    #include <stdio.h>
    int putchar(int c);

.. rubric:: Description

.. _9899_7.19.7.9p2:

.. container:: snum

   :ref:`2 <9899_7.19.7.9p2>`

The putchar function is equivalent to putc with the second argument stdout.

.. rubric:: Returns

.. _9899_7.19.7.9p3:

.. container:: snum

   :ref:`3 <9899_7.19.7.9p3>`

The putchar function returns the character written. If a write error occurs, the error indicator for the stream is set and putchar returns EOF.

