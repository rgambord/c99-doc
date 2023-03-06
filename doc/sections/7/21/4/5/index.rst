.. _9899_7.21.4.5:

7.21.4.5 The strxfrm function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.21.4.5p1:

.. container:: snum

   :ref:`1 <9899_7.21.4.5p1>`



::

    #include <string.h>
    size_t strxfrm(char * restrict s1,
         const char * restrict s2,
         size_t n);

.. rubric:: Description

.. _9899_7.21.4.5p2:

.. container:: snum

   :ref:`2 <9899_7.21.4.5p2>`

The strxfrm function transforms the string pointed to by s2 and places the resulting string into the array pointed to by s1. The transformation is such that if the strcmp function is applied to two transformed strings, it returns a value greater than, equal to, or less than zero, corresponding to the result of the strcoll function applied to the same two original strings. No more than n characters are placed into the resulting array pointed to by s1, including the terminating null character. If n is zero, s1 is permitted to be a null pointer. If copying takes place between objects that overlap, the behavior is undefined.

.. rubric:: Returns

.. _9899_7.21.4.5p3:

.. container:: snum

   :ref:`3 <9899_7.21.4.5p3>`

The strxfrm function returns the length of the transformed string (not including the terminating null character). If the value returned is n or more, the contents of the array pointed to by s1 are indeterminate.

.. _9899_7.21.4.5p4:

.. container:: snum

   :ref:`4 <9899_7.21.4.5p4>`

EXAMPLE The value of the following expression is the size of the array needed to hold the transformation of the string pointed to by s.

::

    1 + strxfrm(NULL, s, 0)

