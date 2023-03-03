.. _9899_introduction-4:

7.24.1 Introduction
^^^^^^^^^^^^^^^^^^^

.. _9899_7.24.1p1:

:ref:`1 <9899_7.24.1p1>` The header :ref:`\<wchar.h> <9899_7.24>` declares four data types, one tag, four macros, and many functions.\ [#9899_note277]_

.. _9899_7.24.1p2:

:ref:`2 <9899_7.24.1p2>` The types declared are wchar_t and size_t (both described in :ref:`7.17 <9899_7.17>`);

::

    mbstate_t

which is an object type other than an array type that can hold the conversion state information necessary to convert between sequences of multibyte characters and wide characters;

::

    wint_t

which is an integer type unchanged by default argument promotions that can hold any value corresponding to members of the extended character set, as well as at least one value that does not correspond to any member of the extended character set (see WEOF below);\ [#9899_note278]_ and

::

    struct tm

which is declared as an incomplete structure type (the contents are described in :ref:`7.23.1 <9899_7.23.1>`).

.. _9899_7.24.1p3:

:ref:`3 <9899_7.24.1p3>` The macros defined are NULL (described in :ref:`7.17 <9899_7.17>`); WCHAR_MIN and WCHAR_MAX (described in :ref:`7.18.3 <9899_7.18.3>`); and

::

    WEOF

which expands to a constant expression of type wint_t whose value does not correspond to any member of the extended character set.\ [#9899_note279]_ It is accepted (and returned) by several functions in this subclause to indicate end-of-file, that is, no more input from a stream. It is also used as a wide character value that does not correspond to any member of the extended character set.

.. _9899_7.24.1p4:

:ref:`4 <9899_7.24.1p4>` The functions declared are grouped as follows:

-  Functions that perform input and output of wide characters, or multibyte characters, or both;
-  Functions that provide wide string numeric conversion;
-  Functions that perform general wide string manipulation;
-  Functions for wide string date and time conversion; and
-  Functions that provide extended capabilities for conversion between multibyte and wide character sequences.

.. _9899_7.24.1p5:

:ref:`5 <9899_7.24.1p5>` Unless explicitly stated otherwise, if the execution of a function described in this subclause causes copying to take place between objects that overlap, the behavior is undefined.







.. rubric:: Footnotes

.. [#9899_note277] See ''future library directions'' (:ref:`7.26.12 <9899_7.26.12>`).
.. [#9899_note278] wchar_t and wint_t can be the same integer type.
.. [#9899_note279] The value of the macro WEOF may differ from that of EOF and need not be negative.
