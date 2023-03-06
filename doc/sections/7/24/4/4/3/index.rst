.. _9899_7.24.4.4.3:

7.24.4.4.3 The wcsncmp function
"""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.4.4.3p1:

.. container:: snum

   :ref:`1 <9899_7.24.4.4.3p1>`



::

    #include <wchar.h>
    int wcsncmp(const wchar_t *s1, const wchar_t *s2,
         size_t n);

.. rubric:: Description

.. _9899_7.24.4.4.3p2:

.. container:: snum

   :ref:`2 <9899_7.24.4.4.3p2>`

The wcsncmp function compares not more than n wide characters (those that follow a null wide character are not compared) from the array pointed to by s1 to the array pointed to by s2.

.. rubric:: Returns

.. _9899_7.24.4.4.3p3:

.. container:: snum

   :ref:`3 <9899_7.24.4.4.3p3>`

The wcsncmp function returns an integer greater than, equal to, or less than zero, accordingly as the possibly null-terminated array pointed to by s1 is greater than, equal to, or less than the possibly null-terminated array pointed to by s2.

