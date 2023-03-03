.. _9899_F.9.3.8:

F.9.3.8 The log10 functions
'''''''''''''''''''''''''''

.. _9899_F.9.3.8p1:

:ref:`1 <9899_F.9.3.8p1>`

-  log10((+-)0) returns -(inf) and raises the ''divide-by-zero'' floating-point exception.
-  log10(1) returns +0.
-  log10(x) returns a NaN and raises the ''invalid'' floating-point exception for x < 0.
-  log10(+(inf)) returns +(inf).

