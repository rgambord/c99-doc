.. _9899_5.2.1.1:

5.2.1.1 Trigraph sequences
''''''''''''''''''''''''''

.. _9899_5.2.1.1p1:

:ref:`1 <9899_5.2.1.1p1>` Before any other processing takes place, each occurrence of one of the following sequences of three characters (called trigraph sequences\ [#9899_note12]_) is replaced with the corresponding single character.

.. code-block:: text

    ??=      #                       ??)      ]                       ??!     |
    ??(      [                       ??'      ^                       ??>     }
    ??/      \                       ??<      {                       ??-     ~

No other trigraph sequences exist. Each ? that does not begin one of the trigraphs listed above is not changed.

.. _9899_5.2.1.1p2:

:ref:`2 <9899_5.2.1.1p2>` EXAMPLE 1

::

    ??=define arraycheck(a, b) a??(b??) ??!??! b??(a??)

becomes

::

    #define arraycheck(a, b) a[b] || b[a]

.. _9899_5.2.1.1p3:

:ref:`3 <9899_5.2.1.1p3>` EXAMPLE 2 The following source line

::

    printf("Eh???/n");

becomes (after replacement of the trigraph sequence ??/)

::

    printf("Eh?\n");





.. rubric:: Footnotes

.. [#9899_note12] The trigraph sequences enable the input of characters that are not defined in the Invariant Code Set as described in ISO/IEC 646, which is a subset of the seven-bit US ASCII code set.
