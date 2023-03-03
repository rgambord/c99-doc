.. _9899_5.2.1.2:

5.2.1.2 Multibyte characters
''''''''''''''''''''''''''''

.. _9899_5.2.1.2p1:

:ref:`1 <9899_5.2.1.2p1>` The source character set may contain multibyte characters, used to represent members of the extended character set. The execution character set may also contain multibyte characters, which need not have the same encoding as for the source character set. For both character sets, the following shall hold:

-  The basic character set shall be present and each character shall be encoded as a single byte.
-  The presence, meaning, and representation of any additional members is locale- specific.
-  A multibyte character set may have a state-dependent encoding, wherein each sequence of multibyte characters begins in an initial shift state and enters other locale-specific shift states when specific multibyte characters are encountered in the sequence. While in the initial shift state, all single-byte characters retain their usual interpretation and do not alter the shift state. The interpretation for subsequent bytes in the sequence is a function of the current shift state.
-  A byte with all bits zero shall be interpreted as a null character independent of shift state. Such a byte shall not occur as part of any other multibyte character.

.. _9899_5.2.1.2p2:

:ref:`2 <9899_5.2.1.2p2>` For source files, the following shall hold:

-  An identifier, comment, string literal, character constant, or header name shall begin and end in the initial shift state.
-  An identifier, comment, string literal, character constant, or header name shall consist of a sequence of valid multibyte characters.

