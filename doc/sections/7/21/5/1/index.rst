.. _9899_7.21.5.1:

7.21.5.1 The memchr function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.21.5.1p1:

:ref:`1 <9899_7.21.5.1p1>`

::

    #include <string.h>
    void *memchr(const void *s, int c, size_t n);

.. rubric:: Description

.. _9899_7.21.5.1p2:

:ref:`2 <9899_7.21.5.1p2>` The memchr function locates the first occurrence of c (converted to an unsigned char) in the initial n characters (each interpreted as unsigned char) of the object pointed to by s.

.. rubric:: Returns

.. _9899_7.21.5.1p3:

:ref:`3 <9899_7.21.5.1p3>` The memchr function returns a pointer to the located character, or a null pointer if the character does not occur in the object.

