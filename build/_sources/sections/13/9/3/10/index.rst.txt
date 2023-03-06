.. _9899_F.9.3.10:

F.9.3.10 The log2 functions
'''''''''''''''''''''''''''

.. _9899_F.9.3.10p1:

.. container:: snum

   :ref:`1 <9899_F.9.3.10p1>`



-  log2((+-)0) returns -(inf) and raises the "divide-by-zero" floating-point exception.
-  log2(1) returns +0.
-  log2(x) returns a NaN and raises the "invalid" floating-point exception for x < 0.
-  log2(+(inf)) returns +(inf).

