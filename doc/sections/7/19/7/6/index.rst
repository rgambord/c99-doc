.. _9899_7.19.7.6:

7.19.7.6 The getchar function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.7.6p1:

.. container:: snum

   :ref:`1 <9899_7.19.7.6p1>`



::

    #include <stdio.h>
    int getchar(void);

.. rubric:: Description

.. _9899_7.19.7.6p2:

.. container:: snum

   :ref:`2 <9899_7.19.7.6p2>`

The getchar function is equivalent to getc with the argument stdin.

.. rubric:: Returns

.. _9899_7.19.7.6p3:

.. container:: snum

   :ref:`3 <9899_7.19.7.6p3>`

The getchar function returns the next character from the input stream pointed to by stdin. If the stream is at end-of-file, the end-of-file indicator for the stream is set and getchar returns EOF. If a read error occurs, the error indicator for the stream is set and getchar returns EOF.

