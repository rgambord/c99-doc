.. _9899_7.21.2.2:

7.21.2.2 The memmove function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.21.2.2p1:

:ref:`1 <9899_7.21.2.2p1>`

::

    #include <string.h>
    void *memmove(void *s1, const void *s2, size_t n);

.. rubric:: Description

.. _9899_7.21.2.2p2:

:ref:`2 <9899_7.21.2.2p2>` The memmove function copies n characters from the object pointed to by s2 into the object pointed to by s1. Copying takes place as if the n characters from the object pointed to by s2 are first copied into a temporary array of n characters that does not overlap the objects pointed to by s1 and s2, and then the n characters from the temporary array are copied into the object pointed to by s1.

.. rubric:: Returns

.. _9899_7.21.2.2p3:

:ref:`3 <9899_7.21.2.2p3>` The memmove function returns the value of s1.

