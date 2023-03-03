.. _9899_6.10.3:

6.10.3 Macro replacement
^^^^^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index
   4/index
   5/index


.. rubric:: Constraints

.. _9899_6.10.3p1:

:ref:`1 <9899_6.10.3p1>` Two replacement lists are identical if and only if the preprocessing tokens in both have the same number, ordering, spelling, and white-space separation, where all white-space separations are considered identical.

.. _9899_6.10.3p2:

:ref:`2 <9899_6.10.3p2>` An identifier currently defined as an object-like macro shall not be redefined by another #define preprocessing directive unless the second definition is an object-like macro definition and the two replacement lists are identical. Likewise, an identifier currently defined as a function-like macro shall not be redefined by another #define preprocessing directive unless the second definition is a function-like macro definition that has the same number and spelling of parameters, and the two replacement lists are identical.

.. _9899_6.10.3p3:

:ref:`3 <9899_6.10.3p3>` There shall be white-space between the identifier and the replacement list in the definition of an object-like macro.

.. _9899_6.10.3p4:

:ref:`4 <9899_6.10.3p4>` If the identifier-list in the macro definition does not end with an ellipsis, the number of arguments (including those arguments consisting of no preprocessing tokens) in an invocation of a function-like macro shall equal the number of parameters in the macro definition. Otherwise, there shall be more arguments in the invocation than there are parameters in the macro definition (excluding the \.\.\.). There shall exist a ) preprocessing token that terminates the invocation.

.. _9899_6.10.3p5:

:ref:`5 <9899_6.10.3p5>` The identifier \__VA_ARGS\_\_ shall occur only in the replacement-list of a function-like macro that uses the ellipsis notation in the parameters.

.. _9899_6.10.3p6:

:ref:`6 <9899_6.10.3p6>` A parameter identifier in a function-like macro shall be uniquely declared within its scope.

.. rubric:: Semantics

.. _9899_6.10.3p7:

:ref:`7 <9899_6.10.3p7>` The identifier immediately following the define is called the macro name. There is one name space for macro names. Any white-space characters preceding or following the replacement list of preprocessing tokens are not considered part of the replacement list for either form of macro.

.. _9899_6.10.3p8:

:ref:`8 <9899_6.10.3p8>` If a # preprocessing token, followed by an identifier, occurs lexically at the point at which a preprocessing directive could begin, the identifier is not subject to macro replacement.

.. _9899_6.10.3p9:

:ref:`9 <9899_6.10.3p9>` A preprocessing directive of the form

.. code-block:: text

    # define identifier replacement-list new-line

defines an object-like macro that causes each subsequent instance of the macro name\ [#9899_note149]_ to be replaced by the replacement list of preprocessing tokens that constitute the remainder of the directive. The replacement list is then rescanned for more macro names as specified below.

.. _9899_6.10.3p10:

:ref:`10 <9899_6.10.3p10>` A preprocessing directive of the form

.. code-block:: text

    # define identifier lparen identifier-listopt ) replacement-list new-line
    # define identifier lparen ... ) replacement-list new-line
    # define identifier lparen identifier-list , ... ) replacement-list new-line

defines a function-like macro with parameters, whose use is similar syntactically to a function call. The parameters are specified by the optional list of identifiers, whose scope extends from their declaration in the identifier list until the new-line character that terminates the #define preprocessing directive. Each subsequent instance of the function-like macro name followed by a ( as the next preprocessing token introduces the sequence of preprocessing tokens that is replaced by the replacement list in the definition (an invocation of the macro). The replaced sequence of preprocessing tokens is terminated by the matching ) preprocessing token, skipping intervening matched pairs of left and right parenthesis preprocessing tokens. Within the sequence of preprocessing tokens making up an invocation of a function-like macro, new-line is considered a normal white-space character.

.. _9899_6.10.3p11:

:ref:`11 <9899_6.10.3p11>` The sequence of preprocessing tokens bounded by the outside-most matching parentheses forms the list of arguments for the function-like macro. The individual arguments within the list are separated by comma preprocessing tokens, but comma preprocessing tokens between matching inner parentheses do not separate arguments. If there are sequences of preprocessing tokens within the list of arguments that would otherwise act as preprocessing directives,\ [#9899_note150]_ the behavior is undefined.

.. _9899_6.10.3p12:

:ref:`12 <9899_6.10.3p12>` If there is a \.\.\. in the identifier-list in the macro definition, then the trailing arguments, including any separating comma preprocessing tokens, are merged to form a single item: the variable arguments. The number of arguments so combined is such that, following merger, the number of arguments is one more than the number of parameters in the macro definition (excluding the \.\.\.).






.. rubric:: Footnotes

.. [#9899_note149] Since, by macro-replacement time, all character constants and string literals are preprocessing tokens, not sequences possibly containing identifier-like subsequences (see :ref:`5.1.1.2 <9899_5.1.1.2>`, translation phases), they are never scanned for macro names or parameters.
.. [#9899_note150] Despite the name, a non-directive is a preprocessing directive.
