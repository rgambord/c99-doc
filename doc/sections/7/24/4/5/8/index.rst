.. _9899_7.24.4.5.8:

7.24.4.5.8 The wmemchr function
"""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.4.5.8p1:

:ref:`1 <9899_7.24.4.5.8p1>`

::

    #include <wchar.h>
    wchar_t *wmemchr(const wchar_t *s, wchar_t c,
         size_t n);

.. rubric:: Description

.. _9899_7.24.4.5.8p2:

:ref:`2 <9899_7.24.4.5.8p2>` The wmemchr function locates the first occurrence of c in the initial n wide characters of the object pointed to by s.

.. rubric:: Returns

.. _9899_7.24.4.5.8p3:

:ref:`3 <9899_7.24.4.5.8p3>` The wmemchr function returns a pointer to the located wide character, or a null pointer if the wide character does not occur in the object.

.. _9899_7.24.4.6:

