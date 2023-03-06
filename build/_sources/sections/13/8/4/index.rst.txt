.. _9899_F.8.4:

F.8.4 Constant arithmetic
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_F.8.4p1:

.. container:: snum

   :ref:`1 <9899_F.8.4p1>`

The implementation shall honor floating-point exceptions raised by execution-time constant arithmetic wherever the state of the FENV_ACCESS pragma is "on". (See :ref:`F.7.4 <9899_F.7.4>` and :ref:`F.7.5 <9899_F.7.5>`.) An operation on constants that raises no floating-point exception can be folded during translation, except, if the state of the FENV_ACCESS pragma is "on", a further check is required to assure that changing the rounding direction to downward does not alter the sign of the result,\ [#9899_note319]_ and implementations that support dynamic rounding precision modes shall assure further that the result of the operation raises no floating- point exception when converted to the semantic type of the operation.





.. rubric:: Footnotes

.. [#9899_note319] 0 - 0 yields -0 instead of +0 just when the rounding direction is downward.
