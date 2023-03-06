.. _9899_7.25.2.1.10:

7.25.2.1.10 The iswspace function
"""""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.25.2.1.10p1:

.. container:: snum

   :ref:`1 <9899_7.25.2.1.10p1>`



::

    #include <wctype.h>
    int iswspace(wint_t wc);

.. rubric:: Description

.. _9899_7.25.2.1.10p2:

.. container:: snum

   :ref:`2 <9899_7.25.2.1.10p2>`

The iswspace function tests for any wide character that corresponds to a locale-specific set of white-space wide characters for which none of iswalnum, iswgraph, or iswpunct is true.

