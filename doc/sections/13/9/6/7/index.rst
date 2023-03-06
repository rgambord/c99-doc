.. _9899_F.9.6.7:

F.9.6.7 The lround and llround functions
''''''''''''''''''''''''''''''''''''''''

.. _9899_F.9.6.7p1:

.. container:: snum

   :ref:`1 <9899_F.9.6.7p1>`

The lround and llround functions differ from the lrint and llrint functions with the default rounding direction just in that the lround and llround functions round halfway cases away from zero and need not raise the "inexact" floating-point exception for non-integer arguments that round to within the range of the return type.

