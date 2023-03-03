.. _9899_7.21.5.2:

7.21.5.2 The strchr function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.21.5.2p1:

:ref:`1 <9899_7.21.5.2p1>`

::

    #include <string.h>
    char *strchr(const char *s, int c);

.. rubric:: Description

.. _9899_7.21.5.2p2:

:ref:`2 <9899_7.21.5.2p2>` The strchr function locates the first occurrence of c (converted to a char) in the string pointed to by s. The terminating null character is considered to be part of the string.

.. rubric:: Returns

.. _9899_7.21.5.2p3:

:ref:`3 <9899_7.21.5.2p3>` The strchr function returns a pointer to the located character, or a null pointer if the character does not occur in the string.

