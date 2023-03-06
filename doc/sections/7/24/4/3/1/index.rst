.. _9899_7.24.4.3.1:

7.24.4.3.1 The wcscat function
""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.4.3.1p1:

.. container:: snum

   :ref:`1 <9899_7.24.4.3.1p1>`



::

    #include <wchar.h>
    wchar_t *wcscat(wchar_t * restrict s1,
         const wchar_t * restrict s2);

.. rubric:: Description

.. _9899_7.24.4.3.1p2:

.. container:: snum

   :ref:`2 <9899_7.24.4.3.1p2>`

The wcscat function appends a copy of the wide string pointed to by s2 (including the terminating null wide character) to the end of the wide string pointed to by s1. The initial wide character of s2 overwrites the null wide character at the end of s1.

.. rubric:: Returns

.. _9899_7.24.4.3.1p3:

.. container:: snum

   :ref:`3 <9899_7.24.4.3.1p3>`

The wcscat function returns the value of s1.

