.. _9899_F.9.5.4:

F.9.5.4 The tgamma functions
''''''''''''''''''''''''''''

.. _9899_F.9.5.4p1:

.. container:: snum

   :ref:`1 <9899_F.9.5.4p1>`



-  tgamma((+-)0) returns (+-)(inf) and raises the "divide-by-zero" floating-point exception.
-  tgamma(x) returns a NaN and raises the "invalid" floating-point exception for x a negative integer.
-  tgamma(-(inf)) returns a NaN and raises the "invalid" floating-point exception.
-  tgamma(+(inf)) returns +(inf).

