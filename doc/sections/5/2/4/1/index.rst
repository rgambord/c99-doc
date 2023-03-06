.. _9899_5.2.4.1:

5.2.4.1 Translation limits
''''''''''''''''''''''''''

.. _9899_5.2.4.1p1:

.. container:: snum

   :ref:`1 <9899_5.2.4.1p1>`

The implementation shall be able to translate and execute at least one program that contains at least one instance of every one of the following limits:[#9899_note13]_

-  127 nesting levels of blocks
-  63 nesting levels of conditional inclusion
-  12 pointer, array, and function declarators (in any combinations) modifying an arithmetic, structure, union, or incomplete type in a declaration
-  63 nesting levels of parenthesized declarators within a full declarator
-  63 nesting levels of parenthesized expressions within a full expression
-  63 significant initial characters in an internal identifier or a macro name (each universal character name or extended source character is considered a single character)
-  31 significant initial characters in an external identifier (each universal character name specifying a short identifier of 0000FFFF or less is considered 6 characters, each universal character name specifying a short identifier of 00010000 or more is considered 10 characters, and each extended source character is considered the same number of characters as the corresponding universal character name, if any)\ [#9899_note14]_
-  4095 external identifiers in one translation unit
-  511 identifiers with block scope declared in one block
-  4095 macro identifiers simultaneously defined in one preprocessing translation unit
-  127 parameters in one function definition
-  127 arguments in one function call
-  127 parameters in one macro definition
-  127 arguments in one macro invocation
-  4095 characters in a logical source line
-  4095 characters in a character string literal or wide string literal (after concatenation)
-  65535 bytes in an object (in a hosted environment only)
-  15 nesting levels for `#included` files
-  1023 case labels for a switch statement (excluding those for any nested switch statements)
-  1023 members in a single structure or union
-  1023 enumeration constants in a single enumeration
-  63 levels of nested structure or union definitions in a single struct-declaration-list






.. rubric:: Footnotes

.. [#9899_note13] Implementations should avoid imposing fixed translation limits whenever possible.
.. [#9899_note14] See "future language directions" (:ref:`6.11.3 <9899_6.11.3>`).
