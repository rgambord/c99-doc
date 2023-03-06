.. _9899_7.25.2.1.5:

7.25.2.1.5 The iswdigit function
""""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.25.2.1.5p1:

.. container:: snum

   :ref:`1 <9899_7.25.2.1.5p1>`



::

    #include <wctype.h>
    int iswdigit(wint_t wc);

.. rubric:: Description

.. _9899_7.25.2.1.5p2:

.. container:: snum

   :ref:`2 <9899_7.25.2.1.5p2>`

The iswdigit function tests for any wide character that corresponds to a decimal-digit character (as defined in :ref:`5.2.1 <9899_5.2.1>`).

