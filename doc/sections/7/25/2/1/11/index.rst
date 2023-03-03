.. _9899_7.25.2.1.11:

7.25.2.1.11 The iswupper function
"""""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.25.2.1.11p1:

:ref:`1 <9899_7.25.2.1.11p1>`

::

    #include <wctype.h>
    int iswupper(wint_t wc);

.. rubric:: Description

.. _9899_7.25.2.1.11p2:

:ref:`2 <9899_7.25.2.1.11p2>` The iswupper function tests for any wide character that corresponds to an uppercase letter or is one of a locale-specific set of wide characters for which none of iswcntrl, iswdigit, iswpunct, or iswspace is true.

