.. _9899_7.25.2.1.6:

7.25.2.1.6 The iswgraph function
""""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.25.2.1.6p1:

:ref:`1 <9899_7.25.2.1.6p1>`

::

    #include <wctype.h>
    int iswgraph(wint_t wc);

.. rubric:: Description

.. _9899_7.25.2.1.6p2:

:ref:`2 <9899_7.25.2.1.6p2>` The iswgraph function tests for any wide character for which iswprint is true and iswspace is false.\ [#9899_note306]_





.. rubric:: Footnotes

.. [#9899_note306] Note that the behavior of the iswgraph and iswpunct functions may differ from their corresponding functions in :ref:`7.4.1 <9899_7.4.1>` with respect to printing, white-space, single-byte execution characters other than ' '.
