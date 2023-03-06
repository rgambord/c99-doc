.. _9899_7.24.6:

7.24.6 Extended multibyte/wide character conversion utilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index
   4/index


.. _9899_7.24.6p1:

.. container:: snum

   :ref:`1 <9899_7.24.6p1>`

The header :ref:`\<wchar.h> <9899_7.24>` declares an extended set of functions useful for conversion between multibyte characters and wide characters.

.. _9899_7.24.6p2:

.. container:: snum

   :ref:`2 <9899_7.24.6p2>`

Most of the following functions -- those that are listed as "restartable", :ref:`7.24.6.3 <9899_7.24.6.3>` and :ref:`7.24.6.4 <9899_7.24.6.4>` -- take as a last argument a pointer to an object of type mbstate_t that is used to describe the current conversion state from a particular multibyte character sequence to a wide character sequence (or the reverse) under the rules of a particular setting for the LC_CTYPE category of the current locale.

.. _9899_7.24.6p3:

.. container:: snum

   :ref:`3 <9899_7.24.6p3>`

The initial conversion state corresponds, for a conversion in either direction, to the beginning of a new multibyte character in the initial shift state. A zero-valued mbstate_t object is (at least) one way to describe an initial conversion state. A zero- valued mbstate_t object can be used to initiate conversion involving any multibyte character sequence, in any LC_CTYPE category setting. If an mbstate_t object has been altered by any of the functions described in this subclause, and is then used with a different multibyte character sequence, or in the other conversion direction, or with a different LC_CTYPE category setting than on earlier function calls, the behavior is undefined.\ [#9899_note299]_

.. _9899_7.24.6p4:

.. container:: snum

   :ref:`4 <9899_7.24.6p4>`

On entry, each function takes the described conversion state (either internal or pointed to by an argument) as current. The conversion state described by the pointed-to object is altered as needed to track the shift state, and the position within a multibyte character, for the associated multibyte character sequence.





.. rubric:: Footnotes

.. [#9899_note299] Thus, a particular mbstate_t object can be used, for example, with both the mbrtowc and mbsrtowcs functions as long as they are used to step sequentially through the same multibyte character string.
