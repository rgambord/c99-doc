.. _9899_6.10.1:

6.10.1 Conditional inclusion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Constraints

.. _9899_6.10.1p1:

:ref:`1 <9899_6.10.1p1>` The expression that controls conditional inclusion shall be an integer constant expression except that: it shall not contain a cast; identifiers (including those lexically identical to keywords) are interpreted as described below;\ [#9899_note144]_ and it may contain unary operator expressions of the form

.. code-block:: text

    defined identifier

or

.. code-block:: text

    defined ( identifier )

which evaluate to 1 if the identifier is currently defined as a macro name (that is, if it is predefined or if it has been the subject of a #define preprocessing directive without an intervening #undef directive with the same subject identifier), 0 if it is not.

.. _9899_6.10.1p2:

:ref:`2 <9899_6.10.1p2>` Each preprocessing token that remains (in the list of preprocessing tokens that will become the controlling expression) after all macro replacements have occurred shall be in the lexical form of a token (:ref:`6.4 <9899_6.4>`).

.. rubric:: Semantics

.. _9899_6.10.1p3:

:ref:`3 <9899_6.10.1p3>` Preprocessing directives of the forms

.. code-block:: text

    # if   constant-expression new-line groupopt
    # elif constant-expression new-line groupopt

check whether the controlling constant expression evaluates to nonzero.

.. _9899_6.10.1p4:

:ref:`4 <9899_6.10.1p4>` Prior to evaluation, macro invocations in the list of preprocessing tokens that will become the controlling constant expression are replaced (except for those macro names modified by the defined unary operator), just as in normal text. If the token defined is generated as a result of this replacement process or use of the defined unary operator does not match one of the two specified forms prior to macro replacement, the behavior is undefined. After all replacements due to macro expansion and the defined unary operator have been performed, all remaining identifiers (including those lexically identical to keywords) are replaced with the pp-number 0, and then each preprocessing token is converted into a token. The resulting tokens compose the controlling constant expression which is evaluated according to the rules of :ref:`6.6 <9899_6.6>`. For the purposes of this token conversion and evaluation, all signed integer types and all unsigned integer types act as if they have the same representation as, respectively, the types intmax_t and uintmax_t defined in the header :ref:`\<stdint.h> <9899_7.18>`.\ [#9899_note145]_ This includes interpreting character constants, which may involve converting escape sequences into execution character set members. Whether the numeric value for these character constants matches the value obtained when an identical character constant occurs in an expression (other than within a #if or #elif directive) is implementation-defined.\ [#9899_note146]_ Also, whether a single-character character constant may have a negative value is implementation-defined.

.. _9899_6.10.1p5:

:ref:`5 <9899_6.10.1p5>` Preprocessing directives of the forms

.. code-block:: text

    # ifdef identifier new-line groupopt
    # ifndef identifier new-line groupopt

check whether the identifier is or is not currently defined as a macro name. Their conditions are equivalent to #if defined identifier and #if !defined identifier respectively.

.. _9899_6.10.1p6:

:ref:`6 <9899_6.10.1p6>` Each directive's condition is checked in order. If it evaluates to false (zero), the group that it controls is skipped: directives are processed only through the name that determines the directive in order to keep track of the level of nested conditionals; the rest of the directives' preprocessing tokens are ignored, as are the other preprocessing tokens in the group. Only the first group whose control condition evaluates to true (nonzero) is processed. If none of the conditions evaluates to true, and there is a #else directive, the group controlled by the #else is processed; lacking a #else directive, all the groups until the #endif are skipped.\ [#9899_note147]_

**Forward references**: macro replacement (:ref:`6.10.3 <9899_6.10.3>`), source file inclusion (:ref:`6.10.2 <9899_6.10.2>`), largest integer types (:ref:`7.18.1.5 <9899_7.18.1.5>`).





::

    #if 'z' - 'a' == 25
    if ('z' - 'a' == 25)




.. rubric:: Footnotes

.. [#9899_note144] Because the controlling constant expression is evaluated during translation phase 4, all identifiers either are or are not macro names -- there simply are no keywords, enumeration constants, etc.
.. [#9899_note145] Thus, on an implementation where INT_MAX is 0x7FFF and UINT_MAX is 0xFFFF, the constant 0x8000 is signed and positive within a #if expression even though it would be unsigned in translation phase 7.
.. [#9899_note146] Thus, the constant expression in the following #if directive and if statement is not guaranteed to evaluate to the same value in these two contexts.
.. [#9899_note147] As indicated by the syntax, a preprocessing token shall not follow a #else or #endif directive before the terminating new-line character. However, comments may appear anywhere in a source file, including within a preprocessing directive.
