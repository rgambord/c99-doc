.. _9899_7.24.4.4.5:

7.24.4.4.5 The wmemcmp function
"""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.4.4.5p1:

:ref:`1 <9899_7.24.4.4.5p1>`

::

    #include <wchar.h>
    int wmemcmp(const wchar_t *s1, const wchar_t *s2,
         size_t n);

.. rubric:: Description

.. _9899_7.24.4.4.5p2:

:ref:`2 <9899_7.24.4.4.5p2>` The wmemcmp function compares the first n wide characters of the object pointed to by s1 to the first n wide characters of the object pointed to by s2.

.. rubric:: Returns

.. _9899_7.24.4.4.5p3:

:ref:`3 <9899_7.24.4.4.5p3>` The wmemcmp function returns an integer greater than, equal to, or less than zero, accordingly as the object pointed to by s1 is greater than, equal to, or less than the object pointed to by s2.

