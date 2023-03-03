.. _9899_7.25.2.1.9:

7.25.2.1.9 The iswpunct function
""""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.25.2.1.9p1:

:ref:`1 <9899_7.25.2.1.9p1>`

::

    #include <wctype.h>
    int iswpunct(wint_t wc);

.. rubric:: Description

.. _9899_7.25.2.1.9p2:

:ref:`2 <9899_7.25.2.1.9p2>` The iswpunct function tests for any printing wide character that is one of a locale- specific set of punctuation wide characters for which neither iswspace nor iswalnum is true.\ [#9899_note306]_



.. rubric:: Footnotes

.. [#9899_note306] Note that the behavior of the iswgraph and iswpunct functions may differ from their corresponding functions in :ref:`7.4.1 <9899_7.4.1>` with respect to printing, white-space, single-byte execution characters other than ' '.
