.. _9899_7.24.4.5.6:

7.24.4.5.6 The wcsstr function
""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.4.5.6p1:

:ref:`1 <9899_7.24.4.5.6p1>`

::

    #include <wchar.h>
    wchar_t *wcsstr(const wchar_t *s1, const wchar_t *s2);

.. rubric:: Description

.. _9899_7.24.4.5.6p2:

:ref:`2 <9899_7.24.4.5.6p2>` The wcsstr function locates the first occurrence in the wide string pointed to by s1 of the sequence of wide characters (excluding the terminating null wide character) in the wide string pointed to by s2.

.. rubric:: Returns

.. _9899_7.24.4.5.6p3:

:ref:`3 <9899_7.24.4.5.6p3>` The wcsstr function returns a pointer to the located wide string, or a null pointer if the wide string is not found. If s2 points to a wide string with zero length, the function returns s1.

