.. _9899_7.21.5.7:

7.21.5.7 The strstr function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.21.5.7p1:

.. container:: snum

   :ref:`1 <9899_7.21.5.7p1>`



::

    #include <string.h>
    char *strstr(const char *s1, const char *s2);

.. rubric:: Description

.. _9899_7.21.5.7p2:

.. container:: snum

   :ref:`2 <9899_7.21.5.7p2>`

The strstr function locates the first occurrence in the string pointed to by s1 of the sequence of characters (excluding the terminating null character) in the string pointed to by s2.

.. rubric:: Returns

.. _9899_7.21.5.7p3:

.. container:: snum

   :ref:`3 <9899_7.21.5.7p3>`

The strstr function returns a pointer to the located string, or a null pointer if the string is not found. If s2 points to a string with zero length, the function returns s1.

