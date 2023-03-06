.. _9899_7.24.4.6.2:

7.24.4.6.2 The wmemset function
"""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.4.6.2p1:

.. container:: snum

   :ref:`1 <9899_7.24.4.6.2p1>`



::

    #include <wchar.h>
    wchar_t *wmemset(wchar_t *s, wchar_t c, size_t n);

.. rubric:: Description

.. _9899_7.24.4.6.2p2:

.. container:: snum

   :ref:`2 <9899_7.24.4.6.2p2>`

The wmemset function copies the value of c into each of the first n wide characters of the object pointed to by s.

.. rubric:: Returns

.. _9899_7.24.4.6.2p3:

.. container:: snum

   :ref:`3 <9899_7.24.4.6.2p3>`

The wmemset function returns the value of s.

