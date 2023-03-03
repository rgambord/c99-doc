.. _9899_F.9.3.9:

F.9.3.9 The log1p functions
'''''''''''''''''''''''''''

.. _9899_F.9.3.9p1:

:ref:`1 <9899_F.9.3.9p1>`

-  log1p((+-)0) returns (+-)0.
-  log1p(-1) returns -(inf) and raises the ''divide-by-zero'' floating-point exception.
-  log1p(x) returns a NaN and raises the ''invalid'' floating-point exception for x < -1.
-  log1p(+(inf)) returns +(inf).

