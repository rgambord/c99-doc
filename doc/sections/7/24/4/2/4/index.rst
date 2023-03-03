.. _9899_7.24.4.2.4:

7.24.4.2.4 The wmemmove function
""""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.4.2.4p1:

:ref:`1 <9899_7.24.4.2.4p1>`

::

    #include <wchar.h>
    wchar_t *wmemmove(wchar_t *s1, const wchar_t *s2,
         size_t n);

.. rubric:: Description

.. _9899_7.24.4.2.4p2:

:ref:`2 <9899_7.24.4.2.4p2>` The wmemmove function copies n wide characters from the object pointed to by s2 to the object pointed to by s1. Copying takes place as if the n wide characters from the object pointed to by s2 are first copied into a temporary array of n wide characters that does not overlap the objects pointed to by s1 or s2, and then the n wide characters from the temporary array are copied into the object pointed to by s1.

.. rubric:: Returns

.. _9899_7.24.4.2.4p3:

:ref:`3 <9899_7.24.4.2.4p3>` The wmemmove function returns the value of s1.

