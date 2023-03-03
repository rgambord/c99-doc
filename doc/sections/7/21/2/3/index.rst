.. _9899_7.21.2.3:

7.21.2.3 The strcpy function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.21.2.3p1:

:ref:`1 <9899_7.21.2.3p1>`

::

    #include <string.h>
    char *strcpy(char * restrict s1,
         const char * restrict s2);

.. rubric:: Description

.. _9899_7.21.2.3p2:

:ref:`2 <9899_7.21.2.3p2>` The strcpy function copies the string pointed to by s2 (including the terminating null character) into the array pointed to by s1. If copying takes place between objects that overlap, the behavior is undefined.

.. rubric:: Returns

.. _9899_7.21.2.3p3:

:ref:`3 <9899_7.21.2.3p3>` The strcpy function returns the value of s1.

