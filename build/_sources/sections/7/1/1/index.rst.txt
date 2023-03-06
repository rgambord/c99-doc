.. _9899_7.1.1:

7.1.1 Definitions of terms
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_7.1.1p1:

.. container:: snum

   :ref:`1 <9899_7.1.1p1>`

A string is a contiguous sequence of characters terminated by and including the first null character. The term multibyte string is sometimes used instead to emphasize special processing given to multibyte characters contained in the string or to avoid confusion with a wide string. A pointer to a string is a pointer to its initial (lowest addressed) character. The length of a string is the number of bytes preceding the null character and the value of a string is the sequence of the values of the contained characters, in order.

.. _9899_7.1.1p2:

.. container:: snum

   :ref:`2 <9899_7.1.1p2>`

The decimal-point character is the character used by functions that convert floating-point numbers to or from character sequences to denote the beginning of the fractional part of such character sequences.\ [#9899_note157]_ It is represented in the text and examples by a period, but may be changed by the setlocale function.

.. _9899_7.1.1p3:

.. container:: snum

   :ref:`3 <9899_7.1.1p3>`

A null wide character is a wide character with code value zero.

.. _9899_7.1.1p4:

.. container:: snum

   :ref:`4 <9899_7.1.1p4>`

A wide string is a contiguous sequence of wide characters terminated by and including the first null wide character. A pointer to a wide string is a pointer to its initial (lowest addressed) wide character. The length of a wide string is the number of wide characters preceding the null wide character and the value of a wide string is the sequence of code values of the contained wide characters, in order.

.. _9899_7.1.1p5:

.. container:: snum

   :ref:`5 <9899_7.1.1p5>`

A shift sequence is a contiguous sequence of bytes within a multibyte string that (potentially) causes a change in shift state (see :ref:`5.2.1.2 <9899_5.2.1.2>`). A shift sequence shall not have a corresponding wide character; it is instead taken to be an adjunct to an adjacent multibyte character.\ [#9899_note158]_

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_7.4`
   - :ref:`9899_7.11.1.1`






.. rubric:: Footnotes

.. [#9899_note157] The functions that make use of the decimal-point character are the numeric conversion functions (:ref:`7.20.1 <9899_7.20.1>`, :ref:`7.24.4.1 <9899_7.24.4.1>`) and the formatted input/output functions (:ref:`7.19.6 <9899_7.19.6>`, :ref:`7.24.2 <9899_7.24.2>`).
.. [#9899_note158] For state-dependent encodings, the values for MB_CUR_MAX and MB_LEN_MAX shall thus be large enough to count all the bytes in any complete multibyte character plus at least one adjacent shift sequence of maximum length. Whether these counts provide for more than one shift sequence is the implementation's choice.
