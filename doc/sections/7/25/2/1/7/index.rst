.. _9899_7.25.2.1.7:

7.25.2.1.7 The iswlower function
""""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.25.2.1.7p1:

.. container:: snum

   :ref:`1 <9899_7.25.2.1.7p1>`



::

    #include <wctype.h>
    int iswlower(wint_t wc);

.. rubric:: Description

.. _9899_7.25.2.1.7p2:

.. container:: snum

   :ref:`2 <9899_7.25.2.1.7p2>`

The iswlower function tests for any wide character that corresponds to a lowercase letter or is one of a locale-specific set of wide characters for which none of iswcntrl, iswdigit, iswpunct, or iswspace is true.

