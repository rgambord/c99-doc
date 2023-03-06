.. _9899_7.24.4.2.3:

7.24.4.2.3 The wmemcpy function
"""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.4.2.3p1:

.. container:: snum

   :ref:`1 <9899_7.24.4.2.3p1>`



::

    #include <wchar.h>
    wchar_t *wmemcpy(wchar_t * restrict s1,
         const wchar_t * restrict s2,
         size_t n);

.. rubric:: Description

.. _9899_7.24.4.2.3p2:

.. container:: snum

   :ref:`2 <9899_7.24.4.2.3p2>`

The wmemcpy function copies n wide characters from the object pointed to by s2 to the object pointed to by s1.

.. rubric:: Returns

.. _9899_7.24.4.2.3p3:

.. container:: snum

   :ref:`3 <9899_7.24.4.2.3p3>`

The wmemcpy function returns the value of s1.

