.. _9899_7.21.3.2:

7.21.3.2 The strncat function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.21.3.2p1:

.. container:: snum

   :ref:`1 <9899_7.21.3.2p1>`



::

    #include <string.h>
    char *strncat(char * restrict s1,
         const char * restrict s2,
         size_t n);

.. rubric:: Description

.. _9899_7.21.3.2p2:

.. container:: snum

   :ref:`2 <9899_7.21.3.2p2>`

The strncat function appends not more than n characters (a null character and characters that follow it are not appended) from the array pointed to by s2 to the end of the string pointed to by s1. The initial character of s2 overwrites the null character at the end of s1. A terminating null character is always appended to the result.\ [#9899_note270]_ If copying takes place between objects that overlap, the behavior is undefined.

.. rubric:: Returns

.. _9899_7.21.3.2p3:

.. container:: snum

   :ref:`3 <9899_7.21.3.2p3>`

The strncat function returns the value of s1.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_7.21.6.3`





.. rubric:: Footnotes

.. [#9899_note270] Thus, the maximum number of characters that can end up in the array pointed to by s1 is strlen(s1)+n+1.
