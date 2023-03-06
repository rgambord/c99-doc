.. _9899_7.24.4.5.5:

7.24.4.5.5 The wcsspn function
""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.4.5.5p1:

.. container:: snum

   :ref:`1 <9899_7.24.4.5.5p1>`



::

    #include <wchar.h>
    size_t wcsspn(const wchar_t *s1, const wchar_t *s2);

.. rubric:: Description

.. _9899_7.24.4.5.5p2:

.. container:: snum

   :ref:`2 <9899_7.24.4.5.5p2>`

The wcsspn function computes the length of the maximum initial segment of the wide string pointed to by s1 which consists entirely of wide characters from the wide string pointed to by s2.

.. rubric:: Returns

.. _9899_7.24.4.5.5p3:

.. container:: snum

   :ref:`3 <9899_7.24.4.5.5p3>`

The wcsspn function returns the length of the segment.

