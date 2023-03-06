.. _9899_F.9.4.3:

F.9.4.3 The hypot functions
'''''''''''''''''''''''''''

.. _9899_F.9.4.3p1:

.. container:: snum

   :ref:`1 <9899_F.9.4.3p1>`



-  hypot(x, y), hypot(y, x), and hypot(x, -y) are equivalent.
-  hypot(x, (+-)0) is equivalent to fabs(x).
-  hypot((+-)(inf), y) returns +(inf), even if y is a NaN.

