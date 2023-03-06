.. _9899_7.24.4.5.3:

7.24.4.5.3 The wcspbrk function
"""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.4.5.3p1:

.. container:: snum

   :ref:`1 <9899_7.24.4.5.3p1>`



::

    #include <wchar.h>
    wchar_t *wcspbrk(const wchar_t *s1, const wchar_t *s2);

.. rubric:: Description

.. _9899_7.24.4.5.3p2:

.. container:: snum

   :ref:`2 <9899_7.24.4.5.3p2>`

The wcspbrk function locates the first occurrence in the wide string pointed to by s1 of any wide character from the wide string pointed to by s2.

.. rubric:: Returns

.. _9899_7.24.4.5.3p3:

.. container:: snum

   :ref:`3 <9899_7.24.4.5.3p3>`

The wcspbrk function returns a pointer to the wide character in s1, or a null pointer if no wide character from s2 occurs in s1.

