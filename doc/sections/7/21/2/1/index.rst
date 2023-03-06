.. _9899_7.21.2.1:

7.21.2.1 The memcpy function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.21.2.1p1:

.. container:: snum

   :ref:`1 <9899_7.21.2.1p1>`



::

    #include <string.h>
    void *memcpy(void * restrict s1,
         const void * restrict s2,
         size_t n);

.. rubric:: Description

.. _9899_7.21.2.1p2:

.. container:: snum

   :ref:`2 <9899_7.21.2.1p2>`

The memcpy function copies n characters from the object pointed to by s2 into the object pointed to by s1. If copying takes place between objects that overlap, the behavior is undefined.

.. rubric:: Returns

.. _9899_7.21.2.1p3:

.. container:: snum

   :ref:`3 <9899_7.21.2.1p3>`

The memcpy function returns the value of s1.

