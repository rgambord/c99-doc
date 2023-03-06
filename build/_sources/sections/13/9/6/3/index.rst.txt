.. _9899_F.9.6.3:

F.9.6.3 The nearbyint functions
'''''''''''''''''''''''''''''''

.. _9899_F.9.6.3p1:

.. container:: snum

   :ref:`1 <9899_F.9.6.3p1>`

The nearbyint functions use IEC 60559 rounding according to the current rounding direction. They do not raise the "inexact" floating-point exception if the result differs in value from the argument.

-  nearbyint((+-)0) returns (+-)0 (for all rounding directions).
-  nearbyint((+-)(inf)) returns (+-)(inf) (for all rounding directions).

