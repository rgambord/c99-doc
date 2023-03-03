.. _9899_7.21.2.4:

7.21.2.4 The strncpy function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.21.2.4p1:

:ref:`1 <9899_7.21.2.4p1>`

::

    #include <string.h>
    char *strncpy(char * restrict s1,
         const char * restrict s2,
         size_t n);

.. rubric:: Description

.. _9899_7.21.2.4p2:

:ref:`2 <9899_7.21.2.4p2>` The strncpy function copies not more than n characters (characters that follow a null character are not copied) from the array pointed to by s2 to the array pointed to by s1.\ [#9899_note269]_ If copying takes place between objects that overlap, the behavior is undefined.

.. _9899_7.21.2.4p3:

:ref:`3 <9899_7.21.2.4p3>` If the array pointed to by s2 is a string that is shorter than n characters, null characters are appended to the copy in the array pointed to by s1, until n characters in all have been written.

.. rubric:: Returns

.. _9899_7.21.2.4p4:

:ref:`4 <9899_7.21.2.4p4>` The strncpy function returns the value of s1.





.. rubric:: Footnotes

.. [#9899_note269] Thus, if there is no null character in the first n characters of the array pointed to by s2, the result will not be null-terminated.
