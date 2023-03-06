.. _9899_7.20.7:

7.20.7 Multibyte/wide character conversion functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index


.. _9899_7.20.7p1:

.. container:: snum

   :ref:`1 <9899_7.20.7p1>`

The behavior of the multibyte character functions is affected by the LC_CTYPE category of the current locale. For a state-dependent encoding, each function is placed into its initial conversion state by a call for which its character pointer argument, s, is a null pointer. Subsequent calls with s as other than a null pointer cause the internal conversion state of the function to be altered as necessary. A call with s as a null pointer causes these functions to return a nonzero value if encodings have state dependency, and zero otherwise.\ [#9899_note266]_ Changing the LC_CTYPE category causes the conversion state of these functions to be indeterminate.





.. rubric:: Footnotes

.. [#9899_note266] If the locale employs special bytes to change the shift state, these bytes do not produce separate wide character codes, but are grouped with an adjacent multibyte character.
