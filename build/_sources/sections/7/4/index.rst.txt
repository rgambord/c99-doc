.. _9899_7.4:

7.4 Character handling \<ctype.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. toctree::
   :maxdepth: 2

   1/index
   2/index


.. _9899_7.4p1:

.. container:: snum

   :ref:`1 <9899_7.4p1>`

The header :ref:`\<ctype.h> <9899_7.4>` declares several functions useful for classifying and mapping characters.\ [#9899_note172]_ In all cases the argument is an int, the value of which shall be representable as an unsigned char or shall equal the value of the macro EOF. If the argument has any other value, the behavior is undefined.

.. _9899_7.4p2:

.. container:: snum

   :ref:`2 <9899_7.4p2>`

The behavior of these functions is affected by the current locale. Those functions that have locale-specific aspects only when not in the "C" locale are noted below.

.. _9899_7.4p3:

.. container:: snum

   :ref:`3 <9899_7.4p3>`

The term printing character refers to a member of a locale-specific set of characters, each of which occupies one printing position on a display device; the term control character refers to a member of a locale-specific set of characters that are not printing characters.\ [#9899_note173]_ All letters and digits are printing characters.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_7.19.1`
   - :ref:`9899_7.11`






.. rubric:: Footnotes

.. [#9899_note172] See "future library directions" (:ref:`7.26.2 <9899_7.26.2>`).
.. [#9899_note173] In an implementation that uses the seven-bit US ASCII character set, the printing characters are those whose values lie from 0x20 (space) through 0x7E (tilde); the control characters are those whose values lie from 0 (NUL) through 0x1F (US), and the character 0x7F (DEL).
