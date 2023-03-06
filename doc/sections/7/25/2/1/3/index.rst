.. _9899_7.25.2.1.3:

7.25.2.1.3 The iswblank function
""""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.25.2.1.3p1:

.. container:: snum

   :ref:`1 <9899_7.25.2.1.3p1>`



::

    #include <wctype.h>
    int iswblank(wint_t wc);

.. rubric:: Description

.. _9899_7.25.2.1.3p2:

.. container:: snum

   :ref:`2 <9899_7.25.2.1.3p2>`

The iswblank function tests for any wide character that is a standard blank wide character or is one of a locale-specific set of wide characters for which iswspace is true and that is used to separate words within a line of text. The standard blank wide characters are the following: space (L' '), and horizontal tab (L'\\t'). In the "C" locale, iswblank returns true only for the standard blank characters.

