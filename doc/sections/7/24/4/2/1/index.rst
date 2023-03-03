.. _9899_7.24.4.2.1:

7.24.4.2.1 The wcscpy function
""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.4.2.1p1:

:ref:`1 <9899_7.24.4.2.1p1>`

::

    #include <wchar.h>
    wchar_t *wcscpy(wchar_t * restrict s1,
         const wchar_t * restrict s2);

.. rubric:: Description

.. _9899_7.24.4.2.1p2:

:ref:`2 <9899_7.24.4.2.1p2>` The wcscpy function copies the wide string pointed to by s2 (including the terminating null wide character) into the array pointed to by s1.

.. rubric:: Returns

.. _9899_7.24.4.2.1p3:

:ref:`3 <9899_7.24.4.2.1p3>` The wcscpy function returns the value of s1.

