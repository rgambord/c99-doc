.. _9899_7.21.3.1:

7.21.3.1 The strcat function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.21.3.1p1:

.. container:: snum

   :ref:`1 <9899_7.21.3.1p1>`



::

    #include <string.h>
    char *strcat(char * restrict s1,
         const char * restrict s2);

.. rubric:: Description

.. _9899_7.21.3.1p2:

.. container:: snum

   :ref:`2 <9899_7.21.3.1p2>`

The strcat function appends a copy of the string pointed to by s2 (including the terminating null character) to the end of the string pointed to by s1. The initial character of s2 overwrites the null character at the end of s1. If copying takes place between objects that overlap, the behavior is undefined.

.. rubric:: Returns

.. _9899_7.21.3.1p3:

.. container:: snum

   :ref:`3 <9899_7.21.3.1p3>`

The strcat function returns the value of s1.

