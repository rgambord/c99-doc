.. _9899_7.24.4.5.2:

7.24.4.5.2 The wcscspn function
"""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.4.5.2p1:

.. container:: snum

   :ref:`1 <9899_7.24.4.5.2p1>`



::

    #include <wchar.h>
    size_t wcscspn(const wchar_t *s1, const wchar_t *s2);

.. rubric:: Description

.. _9899_7.24.4.5.2p2:

.. container:: snum

   :ref:`2 <9899_7.24.4.5.2p2>`

The wcscspn function computes the length of the maximum initial segment of the wide string pointed to by s1 which consists entirely of wide characters not from the wide string pointed to by s2.

.. rubric:: Returns

.. _9899_7.24.4.5.2p3:

.. container:: snum

   :ref:`3 <9899_7.24.4.5.2p3>`

The wcscspn function returns the length of the segment.

