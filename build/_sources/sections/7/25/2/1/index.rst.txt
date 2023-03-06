.. _9899_7.25.2.1:

7.25.2.1 Wide character classification functions
''''''''''''''''''''''''''''''''''''''''''''''''


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index
   4/index
   5/index
   6/index
   7/index
   8/index
   9/index
   10/index
   11/index
   12/index


.. _9899_7.25.2.1p1:

.. container:: snum

   :ref:`1 <9899_7.25.2.1p1>`

The functions in this subclause return nonzero (true) if and only if the value of the argument wc conforms to that in the description of the function.

.. _9899_7.25.2.1p2:

.. container:: snum

   :ref:`2 <9899_7.25.2.1p2>`

Each of the following functions returns true for each wide character that corresponds (as if by a call to the wctob function) to a single-byte character for which the corresponding character classification function from :ref:`7.4.1 <9899_7.4.1>` returns true, except that the iswgraph and iswpunct functions may differ with respect to wide characters other than L' ' that are both printing and white-space wide characters.\ [#9899_note304]_

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_7.24.6.1.2`





.. rubric:: Footnotes

.. [#9899_note304] For example, if the expression isalpha(wctob(wc)) evaluates to true, then the call iswalpha(wc) also returns true. But, if the expression isgraph(wctob(wc)) evaluates to true (which cannot occur for wc == L' ' of course), then either iswgraph(wc) or iswprint(wc) && iswspace(wc) is true, but not both.
