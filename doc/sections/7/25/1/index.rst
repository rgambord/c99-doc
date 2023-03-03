.. _9899_introduction-5:

7.25.1 Introduction
^^^^^^^^^^^^^^^^^^^

.. _9899_7.25.1p1:

:ref:`1 <9899_7.25.1p1>` The header :ref:`\<wctype.h> <9899_7.25>` declares three data types, one macro, and many functions.\ [#9899_note303]_

.. _9899_7.25.1p2:

:ref:`2 <9899_7.25.1p2>` The types declared are

::

    wint_t

described in :ref:`7.24.1 <9899_7.24.1>`;

::

    wctrans_t

which is a scalar type that can hold values which represent locale-specific character mappings; and

::

    wctype_t

which is a scalar type that can hold values which represent locale-specific character classifications.

.. _9899_7.25.1p3:

:ref:`3 <9899_7.25.1p3>` The macro defined is WEOF (described in :ref:`7.24.1 <9899_7.24.1>`).

.. _9899_7.25.1p4:

:ref:`4 <9899_7.25.1p4>` The functions declared are grouped as follows:

-  Functions that provide wide character classification;
-  Extensible functions that provide wide character classification;
-  Functions that provide wide character case mapping;
-  Extensible functions that provide wide character mapping.

.. _9899_7.25.1p5:

:ref:`5 <9899_7.25.1p5>` For all functions described in this subclause that accept an argument of type wint_t, the value shall be representable as a wchar_t or shall equal the value of the macro WEOF. If this argument has any other value, the behavior is undefined.

.. _9899_7.25.1p6:

:ref:`6 <9899_7.25.1p6>` The behavior of these functions is affected by the LC_CTYPE category of the current locale.





.. rubric:: Footnotes

.. [#9899_note303] See ''future library directions'' (:ref:`7.26.13 <9899_7.26.13>`).
