.. _9899_6.10.4:

6.10.4 Line control
^^^^^^^^^^^^^^^^^^^

.. rubric:: Constraints

.. _9899_6.10.4p1:

.. container:: snum

   :ref:`1 <9899_6.10.4p1>`

The string literal of a `#line` directive, if present, shall be a character string literal.

.. rubric:: Semantics

.. _9899_6.10.4p2:

.. container:: snum

   :ref:`2 <9899_6.10.4p2>`

The line number of the current source line is one greater than the number of new-line characters read or introduced in translation phase 1 (:ref:`5.1.1.2 <9899_5.1.1.2>`) while processing the source file to the current token.

.. _9899_6.10.4p3:

.. container:: snum

   :ref:`3 <9899_6.10.4p3>`

A preprocessing directive of the form

.. code-block:: text

    # line digit-sequence new-line

causes the implementation to behave as if the following sequence of source lines begins with a source line that has a line number as specified by the digit sequence (interpreted as a decimal integer). The digit sequence shall not specify zero, nor a number greater than 2147483647.

.. _9899_6.10.4p4:

.. container:: snum

   :ref:`4 <9899_6.10.4p4>`

A preprocessing directive of the form

.. code-block:: text

    # line digit-sequence "s-char-sequenceopt" new-line

sets the presumed line number similarly and changes the presumed name of the source file to be the contents of the character string literal.

.. _9899_6.10.4p5:

.. container:: snum

   :ref:`5 <9899_6.10.4p5>`

A preprocessing directive of the form

.. code-block:: text

    # line pp-tokens new-line

(that does not match one of the two previous forms) is permitted. The preprocessing tokens after line on the directive are processed just as in normal text (each identifier currently defined as a macro name is replaced by its replacement list of preprocessing tokens). The directive resulting after all replacements shall match one of the two previous forms and is then processed as appropriate.

