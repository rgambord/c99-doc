.. _9899_6.10.3.2:

6.10.3.2 The # operator
'''''''''''''''''''''''

.. rubric:: Constraints

.. _9899_6.10.3.2p1:

:ref:`1 <9899_6.10.3.2p1>` Each # preprocessing token in the replacement list for a function-like macro shall be followed by a parameter as the next preprocessing token in the replacement list.

.. rubric:: Semantics

.. _9899_6.10.3.2p2:

:ref:`2 <9899_6.10.3.2p2>` If, in the replacement list, a parameter is immediately preceded by a # preprocessing token, both are replaced by a single character string literal preprocessing token that contains the spelling of the preprocessing token sequence for the corresponding argument. Each occurrence of white space between the argument's preprocessing tokens becomes a single space character in the character string literal. White space before the first preprocessing token and after the last preprocessing token composing the argument is deleted. Otherwise, the original spelling of each preprocessing token in the argument is retained in the character string literal, except for special handling for producing the spelling of string literals and character constants: a \\ character is inserted before each " and \\ character of a character constant or string literal (including the delimiting " characters), except that it is implementation-defined whether a \\ character is inserted before the \\ character beginning a universal character name. If the replacement that results is not a valid character string literal, the behavior is undefined. The character string literal corresponding to an empty argument is "". The order of evaluation of # and ## operators is unspecified.

.. _9899_6.10.3.3:

