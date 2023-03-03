.. _9899_7.21.5.4:

7.21.5.4 The strpbrk function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.21.5.4p1:

:ref:`1 <9899_7.21.5.4p1>`

::

    #include <string.h>
    char *strpbrk(const char *s1, const char *s2);

.. rubric:: Description

.. _9899_7.21.5.4p2:

:ref:`2 <9899_7.21.5.4p2>` The strpbrk function locates the first occurrence in the string pointed to by s1 of any character from the string pointed to by s2.

.. rubric:: Returns

.. _9899_7.21.5.4p3:

:ref:`3 <9899_7.21.5.4p3>` The strpbrk function returns a pointer to the character, or a null pointer if no character from s2 occurs in s1.

