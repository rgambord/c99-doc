.. _9899_6.8.4.2:

6.8.4.2 The switch statement
''''''''''''''''''''''''''''

.. rubric:: Constraints

.. _9899_6.8.4.2p1:

:ref:`1 <9899_6.8.4.2p1>` The controlling expression of a switch statement shall have integer type.

.. _9899_6.8.4.2p2:

:ref:`2 <9899_6.8.4.2p2>` If a switch statement has an associated case or default label within the scope of an identifier with a variably modified type, the entire switch statement shall be within the scope of that identifier.\ [#9899_note135]_

.. _9899_6.8.4.2p3:

:ref:`3 <9899_6.8.4.2p3>` The expression of each case label shall be an integer constant expression and no two of the case constant expressions in the same switch statement shall have the same value after conversion. There may be at most one default label in a switch statement. (Any enclosed switch statement may have a default label or case constant expressions with values that duplicate case constant expressions in the enclosing switch statement.)

.. rubric:: Semantics

.. _9899_6.8.4.2p4:

:ref:`4 <9899_6.8.4.2p4>` A switch statement causes control to jump to, into, or past the statement that is the switch body, depending on the value of a controlling expression, and on the presence of a default label and the values of any case labels on or in the switch body. A case or default label is accessible only within the closest enclosing switch statement.

.. _9899_6.8.4.2p5:

:ref:`5 <9899_6.8.4.2p5>` The integer promotions are performed on the controlling expression. The constant expression in each case label is converted to the promoted type of the controlling expression. If a converted value matches that of the promoted controlling expression, control jumps to the statement following the matched case label. Otherwise, if there is a default label, control jumps to the labeled statement. If no converted case constant expression matches and there is no default label, no part of the switch body is executed.

.. rubric:: Implementation limits

.. _9899_6.8.4.2p6:

:ref:`6 <9899_6.8.4.2p6>` As discussed in :ref:`5.2.4.1 <9899_5.2.4.1>`, the implementation may limit the number of case values in a switch statement.

.. _9899_6.8.4.2p7:

:ref:`7 <9899_6.8.4.2p7>` EXAMPLE In the artificial program fragment

::

    switch (expr)
    {
          int i = 4;
          f(i);
    case 0:
          i = 17;
          /* falls through into default code */
    default:
          printf("%d\n", i);
    }

the object whose identifier is i exists with automatic storage duration (within the block) but is never initialized, and thus if the controlling expression has a nonzero value, the call to the printf function will access an indeterminate value. Similarly, the call to the function f cannot be reached.





.. rubric:: Footnotes

.. [#9899_note135] That is, the declaration either precedes the switch statement, or it follows the last case or default label associated with the switch that is in the block containing the declaration.
