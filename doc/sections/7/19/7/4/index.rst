.. _9899_7.19.7.4:

7.19.7.4 The fputs function
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.7.4p1:

.. container:: snum

   :ref:`1 <9899_7.19.7.4p1>`



::

    #include <stdio.h>
    int fputs(const char * restrict s,
         FILE * restrict stream);

.. rubric:: Description

.. _9899_7.19.7.4p2:

.. container:: snum

   :ref:`2 <9899_7.19.7.4p2>`

The fputs function writes the string pointed to by s to the stream pointed to by stream. The terminating null character is not written.

.. rubric:: Returns

.. _9899_7.19.7.4p3:

.. container:: snum

   :ref:`3 <9899_7.19.7.4p3>`

The fputs function returns EOF if a write error occurs; otherwise it returns a nonnegative value.

