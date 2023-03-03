.. _9899_F.2.1:

F.2.1 Infinities, signed zeros, and NaNs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_F.2.1p1:

:ref:`1 <9899_F.2.1p1>` This specification does not define the behavior of signaling NaNs.\ [#9899_note309]_ It generally uses the term NaN to denote quiet NaNs. The NAN and INFINITY macros and the nan functions in :ref:`\<math.h> <9899_7.12>` provide designations for IEC 60559 NaNs and infinities.





.. rubric:: Footnotes

.. [#9899_note309] Since NaNs created by IEC 60559 operations are always quiet, quiet NaNs (along with infinities) are sufficient for closure of the arithmetic.
