.. _9899_7.25.2.1.2:

7.25.2.1.2 The iswalpha function
""""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.25.2.1.2p1:

.. container:: snum

   :ref:`1 <9899_7.25.2.1.2p1>`



::

    #include <wctype.h>
    int iswalpha(wint_t wc);

.. rubric:: Description

.. _9899_7.25.2.1.2p2:

.. container:: snum

   :ref:`2 <9899_7.25.2.1.2p2>`

The iswalpha function tests for any wide character for which iswupper or iswlower is true, or any wide character that is one of a locale-specific set of alphabetic wide characters for which none of iswcntrl, iswdigit, iswpunct, or iswspace is true.\ [#9899_note305]_





.. rubric:: Footnotes

.. [#9899_note305] The functions iswlower and iswupper test true or false separately for each of these additional wide characters; all four combinations are possible.
