.. _9899_6.10.3.4:

6.10.3.4 Rescanning and further replacement
'''''''''''''''''''''''''''''''''''''''''''

.. _9899_6.10.3.4p1:

:ref:`1 <9899_6.10.3.4p1>` After all parameters in the replacement list have been substituted and # and ## processing has taken place, all placemarker preprocessing tokens are removed. Then, the resulting preprocessing token sequence is rescanned, along with all subsequent preprocessing tokens of the source file, for more macro names to replace.

.. _9899_6.10.3.4p2:

:ref:`2 <9899_6.10.3.4p2>` If the name of the macro being replaced is found during this scan of the replacement list (not including the rest of the source file's preprocessing tokens), it is not replaced. Furthermore, if any nested replacements encounter the name of the macro being replaced, it is not replaced. These nonreplaced macro name preprocessing tokens are no longer available for further replacement even if they are later (re)examined in contexts in which that macro name preprocessing token would otherwise have been replaced.

.. _9899_6.10.3.4p3:

:ref:`3 <9899_6.10.3.4p3>` The resulting completely macro-replaced preprocessing token sequence is not processed as a preprocessing directive even if it resembles one, but all pragma unary operator expressions within it are then processed as specified in :ref:`6.10.9 <9899_6.10.9>` below.

