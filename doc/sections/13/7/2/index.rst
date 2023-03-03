.. _9899_F.7.2:

F.7.2 Translation
^^^^^^^^^^^^^^^^^

.. _9899_F.7.2p1:

:ref:`1 <9899_F.7.2p1>` During translation the IEC 60559 default modes are in effect:

-  The rounding direction mode is rounding to nearest.
-  The rounding precision mode (if supported) is set so that results are not shortened.
-  Trapping or stopping (if supported) is disabled on all floating-point exceptions.

.. rubric:: Recommended practice

.. _9899_F.7.2p2:

:ref:`2 <9899_F.7.2p2>` The implementation should produce a diagnostic message for each translation-time floating-point exception, other than ''inexact'';\ [#9899_note314]_ the implementation should then proceed with the translation of the program.





.. rubric:: Footnotes

.. [#9899_note314] As floating constants are converted to appropriate internal representations at translation time, their conversion is subject to default rounding modes and raises no execution-time floating-point exceptions (even where the state of the FENV_ACCESS pragma is ''on''). Library functions, for example strtod, provide execution-time conversion of numeric strings.
