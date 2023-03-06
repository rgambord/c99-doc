.. _9899_7.24.4.4.2:

7.24.4.4.2 The wcscoll function
"""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.4.4.2p1:

.. container:: snum

   :ref:`1 <9899_7.24.4.4.2p1>`



::

    #include <wchar.h>
    int wcscoll(const wchar_t *s1, const wchar_t *s2);

.. rubric:: Description

.. _9899_7.24.4.4.2p2:

.. container:: snum

   :ref:`2 <9899_7.24.4.4.2p2>`

The wcscoll function compares the wide string pointed to by s1 to the wide string pointed to by s2, both interpreted as appropriate to the LC_COLLATE category of the current locale.

.. rubric:: Returns

.. _9899_7.24.4.4.2p3:

.. container:: snum

   :ref:`3 <9899_7.24.4.4.2p3>`

The wcscoll function returns an integer greater than, equal to, or less than zero, accordingly as the wide string pointed to by s1 is greater than, equal to, or less than the wide string pointed to by s2 when both are interpreted as appropriate to the current locale.

