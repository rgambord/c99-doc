.. _9899_7.24.6.3:

7.24.6.3 Restartable multibyte/wide character conversion functions
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index


.. _9899_7.24.6.3p1:

.. container:: snum

   :ref:`1 <9899_7.24.6.3p1>`

These functions differ from the corresponding multibyte character functions of :ref:`7.20.7 <9899_7.20.7>` (mblen, mbtowc, and wctomb) in that they have an extra parameter, ps, of type pointer to mbstate_t that points to an object that can completely describe the current conversion state of the associated multibyte character sequence. If ps is a null pointer, each function uses its own internal mbstate_t object instead, which is initialized at program startup to the initial conversion state. The implementation behaves as if no library function calls these functions with a null pointer for ps.

.. _9899_7.24.6.3p2:

.. container:: snum

   :ref:`2 <9899_7.24.6.3p2>`

Also unlike their corresponding functions, the return value does not represent whether the encoding is state-dependent.

