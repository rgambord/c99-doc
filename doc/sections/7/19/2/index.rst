.. _9899_7.19.2:

7.19.2 Streams
^^^^^^^^^^^^^^

.. _9899_7.19.2p1:

:ref:`1 <9899_7.19.2p1>` Input and output, whether to or from physical devices such as terminals and tape drives, or whether to or from files supported on structured storage devices, are mapped into logical data streams, whose properties are more uniform than their various inputs and outputs. Two forms of mapping are supported, for text streams and for binary streams.\ [#9899_note232]_

.. _9899_7.19.2p2:

:ref:`2 <9899_7.19.2p2>` A text stream is an ordered sequence of characters composed into lines, each line consisting of zero or more characters plus a terminating new-line character. Whether the last line requires a terminating new-line character is implementation-defined. Characters may have to be added, altered, or deleted on input and output to conform to differing conventions for representing text in the host environment. Thus, there need not be a one- to-one correspondence between the characters in a stream and those in the external representation. Data read in from a text stream will necessarily compare equal to the data that were earlier written out to that stream only if: the data consist only of printing characters and the control characters horizontal tab and new-line; no new-line character is immediately preceded by space characters; and the last character is a new-line character. Whether space characters that are written out immediately before a new-line character appear when read in is implementation-defined.

.. _9899_7.19.2p3:

:ref:`3 <9899_7.19.2p3>` A binary stream is an ordered sequence of characters that can transparently record internal data. Data read in from a binary stream shall compare equal to the data that were earlier written out to that stream, under the same implementation. Such a stream may, however, have an implementation-defined number of null characters appended to the end of the stream.

.. _9899_7.19.2p4:

:ref:`4 <9899_7.19.2p4>` Each stream has an orientation. After a stream is associated with an external file, but before any operations are performed on it, the stream is without orientation. Once a wide character input/output function has been applied to a stream without orientation, the stream becomes a wide-oriented stream. Similarly, once a byte input/output function has been applied to a stream without orientation, the stream becomes a byte-oriented stream. Only a call to the freopen function or the fwide function can otherwise alter the orientation of a stream. (A successful call to freopen removes any orientation.)\ [#9899_note233]_

.. _9899_7.19.2p5:

:ref:`5 <9899_7.19.2p5>` Byte input/output functions shall not be applied to a wide-oriented stream and wide character input/output functions shall not be applied to a byte-oriented stream. The remaining stream operations do not affect, and are not affected by, a stream's orientation, except for the following additional restrictions:

-  Binary wide-oriented streams have the file-positioning restrictions ascribed to both text and binary streams.
-  For wide-oriented streams, after a successful call to a file-positioning function that leaves the file position indicator prior to the end-of-file, a wide character output function can overwrite a partial multibyte character; any file contents beyond the byte(s) written are henceforth indeterminate.

.. _9899_7.19.2p6:

:ref:`6 <9899_7.19.2p6>` Each wide-oriented stream has an associated mbstate_t object that stores the current parse state of the stream. A successful call to fgetpos stores a representation of the value of this mbstate_t object as part of the value of the fpos_t object. A later successful call to fsetpos using the same stored fpos_t value restores the value of the associated mbstate_t object as well as the position within the controlled stream.

.. rubric:: Environmental limits

.. _9899_7.19.2p7:

:ref:`7 <9899_7.19.2p7>` An implementation shall support text files with lines containing at least 254 characters, including the terminating new-line character. The value of the macro BUFSIZ shall be at least 256.

**Forward references**: the freopen function (:ref:`7.19.5.4 <9899_7.19.5.4>`), the fwide function (:ref:`7.24.3.5 <9899_7.24.3.5>`), mbstate_t (:ref:`7.25.1 <9899_7.25.1>`), the fgetpos function (:ref:`7.19.9.1 <9899_7.19.9.1>`), the fsetpos function (:ref:`7.19.9.3 <9899_7.19.9.3>`).






.. rubric:: Footnotes

.. [#9899_note232] An implementation need not distinguish between text streams and binary streams. In such an implementation, there need be no new-line characters in a text stream nor any limit to the length of a line.
.. [#9899_note233] The three predefined streams stdin, stdout, and stderr are unoriented at program startup.
