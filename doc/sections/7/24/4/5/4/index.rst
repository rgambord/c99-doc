.. _9899_7.24.4.5.4:

7.24.4.5.4 The wcsrchr function
"""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.4.5.4p1:

:ref:`1 <9899_7.24.4.5.4p1>`

::

    #include <wchar.h>
    wchar_t *wcsrchr(const wchar_t *s, wchar_t c);

.. rubric:: Description

.. _9899_7.24.4.5.4p2:

:ref:`2 <9899_7.24.4.5.4p2>` The wcsrchr function locates the last occurrence of c in the wide string pointed to by s. The terminating null wide character is considered to be part of the wide string.

.. rubric:: Returns

.. _9899_7.24.4.5.4p3:

:ref:`3 <9899_7.24.4.5.4p3>` The wcsrchr function returns a pointer to the wide character, or a null pointer if c does not occur in the wide string.

