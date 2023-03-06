.. _9899_7.21.6.1:

7.21.6.1 The memset function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.21.6.1p1:

.. container:: snum

   :ref:`1 <9899_7.21.6.1p1>`



::

    #include <string.h>
    void *memset(void *s, int c, size_t n);

.. rubric:: Description

.. _9899_7.21.6.1p2:

.. container:: snum

   :ref:`2 <9899_7.21.6.1p2>`

The memset function copies the value of c (converted to an unsigned char) into each of the first n characters of the object pointed to by s.

.. rubric:: Returns

.. _9899_7.21.6.1p3:

.. container:: snum

   :ref:`3 <9899_7.21.6.1p3>`

The memset function returns the value of s.

