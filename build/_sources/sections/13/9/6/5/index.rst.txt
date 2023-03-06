.. _9899_F.9.6.5:

F.9.6.5 The lrint and llrint functions
''''''''''''''''''''''''''''''''''''''

.. _9899_F.9.6.5p1:

.. container:: snum

   :ref:`1 <9899_F.9.6.5p1>`

The lrint and llrint functions provide floating-to-integer conversion as prescribed by IEC 60559. They round according to the current rounding direction. If the rounded value is outside the range of the return type, the numeric result is unspecified and the "invalid" floating-point exception is raised. When they raise no other floating-point exception and the result differs from the argument, they raise the "inexact" floating-point exception.

