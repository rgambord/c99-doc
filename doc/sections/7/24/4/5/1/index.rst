.. _9899_7.24.4.5.1:

7.24.4.5.1 The wcschr function
""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.4.5.1p1:

:ref:`1 <9899_7.24.4.5.1p1>`

::

    #include <wchar.h>
    wchar_t *wcschr(const wchar_t *s, wchar_t c);

.. rubric:: Description

.. _9899_7.24.4.5.1p2:

:ref:`2 <9899_7.24.4.5.1p2>` The wcschr function locates the first occurrence of c in the wide string pointed to by s. The terminating null wide character is considered to be part of the wide string.

.. rubric:: Returns

.. _9899_7.24.4.5.1p3:

:ref:`3 <9899_7.24.4.5.1p3>` The wcschr function returns a pointer to the located wide character, or a null pointer if the wide character does not occur in the wide string.

