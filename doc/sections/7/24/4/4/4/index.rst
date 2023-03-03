.. _9899_7.24.4.4.4:

7.24.4.4.4 The wcsxfrm function
"""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.4.4.4p1:

:ref:`1 <9899_7.24.4.4.4p1>`

::

    #include <wchar.h>
    size_t wcsxfrm(wchar_t * restrict s1,
         const wchar_t * restrict s2,
         size_t n);

.. rubric:: Description

.. _9899_7.24.4.4.4p2:

:ref:`2 <9899_7.24.4.4.4p2>` The wcsxfrm function transforms the wide string pointed to by s2 and places the resulting wide string into the array pointed to by s1. The transformation is such that if the wcscmp function is applied to two transformed wide strings, it returns a value greater than, equal to, or less than zero, corresponding to the result of the wcscoll function applied to the same two original wide strings. No more than n wide characters are placed into the resulting array pointed to by s1, including the terminating null wide character. If n is zero, s1 is permitted to be a null pointer.

.. rubric:: Returns

.. _9899_7.24.4.4.4p3:

:ref:`3 <9899_7.24.4.4.4p3>` The wcsxfrm function returns the length of the transformed wide string (not including the terminating null wide character). If the value returned is n or greater, the contents of the array pointed to by s1 are indeterminate.

.. _9899_7.24.4.4.4p4:

:ref:`4 <9899_7.24.4.4.4p4>` EXAMPLE The value of the following expression is the length of the array needed to hold the transformation of the wide string pointed to by s:

::

    1 + wcsxfrm(NULL, s, 0)

