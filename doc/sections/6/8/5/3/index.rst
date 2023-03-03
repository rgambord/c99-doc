.. _9899_6.8.5.3:

6.8.5.3 The for statement
'''''''''''''''''''''''''

.. _9899_6.8.5.3p1:

:ref:`1 <9899_6.8.5.3p1>` The statement

::

    for ( clause-1 ; expression-2 ; expression-3 ) statement

behaves as follows: The expression expression-2 is the controlling expression that is evaluated before each execution of the loop body. The expression expression-3 is evaluated as a void expression after each execution of the loop body. If clause-1 is a declaration, the scope of any identifiers it declares is the remainder of the declaration and the entire loop, including the other two expressions; it is reached in the order of execution before the first evaluation of the controlling expression. If clause-1 is an expression, it is evaluated as a void expression before the first evaluation of the controlling expression.\ [#9899_note137]_

.. _9899_6.8.5.3p2:

:ref:`2 <9899_6.8.5.3p2>` Both clause-1 and expression-3 can be omitted. An omitted expression-2 is replaced by a nonzero constant.





.. rubric:: Footnotes

.. [#9899_note137] Thus, clause-1 specifies initialization for the loop, possibly declaring one or more variables for use in the loop; the controlling expression, expression-2, specifies an evaluation made before each iteration, such that execution of the loop continues until the expression compares equal to 0; and expression-3 specifies an operation (such as incrementing) that is performed after each iteration.
