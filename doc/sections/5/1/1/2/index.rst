.. _9899_5.1.1.2:

5.1.1.2 Translation phases
''''''''''''''''''''''''''

.. _9899_5.1.1.2p1:

:ref:`1 <9899_5.1.1.2p1>` The precedence among the syntax rules of translation is specified by the following phases.\ [#9899_note5]_

#. Physical source file multibyte characters are mapped, in an implementation- defined manner, to the source character set (introducing new-line characters for end-of-line indicators) if necessary. Trigraph sequences are replaced by corresponding single-character internal representations.
#. Each instance of a backslash character (\\) immediately followed by a new-line character is deleted, splicing physical source lines to form logical source lines. Only the last backslash on any physical source line shall be eligible for being part of such a splice. A source file that is not empty shall end in a new-line character, which shall not be immediately preceded by a backslash character before any such splicing takes place.
#. The source file is decomposed into preprocessing tokens\ [#9899_note6]_ and sequences of white-space characters (including comments). A source file shall not end in a partial preprocessing token or in a partial comment. Each comment is replaced by one space character. New-line characters are retained. Whether each nonempty sequence of white-space characters other than new-line is retained or replaced by one space character is implementation-defined.
#. Preprocessing directives are executed, macro invocations are expanded, and \_Pragma unary operator expressions are executed. If a character sequence that matches the syntax of a universal character name is produced by token concatenation (:ref:`6.10.3.3 <9899_6.10.3.3>`), the behavior is undefined. A #include preprocessing directive causes the named header or source file to be processed from phase 1 through phase 4, recursively. All preprocessing directives are then deleted.
#. Each source character set member and escape sequence in character constants and string literals is converted to the corresponding member of the execution character set; if there is no corresponding member, it is converted to an implementation- defined member other than the null (wide) character.\ [#9899_note7]_
#. Adjacent string literal tokens are concatenated.
#. White-space characters separating tokens are no longer significant. Each preprocessing token is converted into a token. The resulting tokens are syntactically and semantically analyzed and translated as a translation unit.
#. All external object and function references are resolved. Library components are linked to satisfy external references to functions and objects not defined in the current translation. All such translator output is collected into a program image which contains information needed for execution in its execution environment.

**Forward references**: universal character names (:ref:`6.4.3 <9899_6.4.3>`), lexical elements (:ref:`6.4 <9899_6.4>`), preprocessing directives (:ref:`6.10 <9899_6.10>`), trigraph sequences (:ref:`5.2.1.1 <9899_5.2.1.1>`), external definitions (:ref:`6.9 <9899_6.9>`).







.. rubric:: Footnotes

.. [#9899_note5] Implementations shall behave as if these separate phases occur, even though many are typically folded together in practice. Source files, translation units, and translated translation units need not necessarily be stored as files, nor need there be any one-to-one correspondence between these entities and any external representation. The description is conceptual only, and does not specify any particular implementation.
.. [#9899_note6] As described in :ref:`6.4 <9899_6.4>`, the process of dividing a source file's characters into preprocessing tokens is context-dependent. For example, see the handling of < within a #include preprocessing directive.
.. [#9899_note7] An implementation need not convert all non-corresponding source characters to the same execution character.
