.. _9899_7.21.5.5:

7.21.5.5 The strrchr function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.21.5.5p1:

:ref:`1 <9899_7.21.5.5p1>`

::

    #include <string.h>
    char *strrchr(const char *s, int c);

.. rubric:: Description

.. _9899_7.21.5.5p2:

:ref:`2 <9899_7.21.5.5p2>` The strrchr function locates the last occurrence of c (converted to a char) in the string pointed to by s. The terminating null character is considered to be part of the string.

.. rubric:: Returns

.. _9899_7.21.5.5p3:

:ref:`3 <9899_7.21.5.5p3>` The strrchr function returns a pointer to the character, or a null pointer if c does not occur in the string.

