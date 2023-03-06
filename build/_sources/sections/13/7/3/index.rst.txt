.. _9899_F.7.3:

F.7.3 Execution
^^^^^^^^^^^^^^^

.. _9899_F.7.3p1:

.. container:: snum

   :ref:`1 <9899_F.7.3p1>`

At program startup the floating-point environment is initialized as prescribed by IEC 60559:

-  All floating-point exception status flags are cleared.
-  The rounding direction mode is rounding to nearest.
-  The dynamic rounding precision mode (if supported) is set so that results are not shortened.
-  Trapping or stopping (if supported) is disabled on all floating-point exceptions.

