.. _9899_F.9.4.4:

F.9.4.4 The pow functions
'''''''''''''''''''''''''

.. _9899_F.9.4.4p1:

:ref:`1 <9899_F.9.4.4p1>`

-  pow((+-)0, y) returns (+-)(inf) and raises the ''divide-by-zero'' floating-point exception for y an odd integer < 0.
-  pow((+-)0, y) returns +(inf) and raises the ''divide-by-zero'' floating-point exception for y < 0 and not an odd integer.
-  pow((+-)0, y) returns (+-)0 for y an odd integer > 0.
-  pow((+-)0, y) returns +0 for y > 0 and not an odd integer.
-  pow(-1, (+-)(inf)) returns 1.
-  pow(+1, y) returns 1 for any y, even a NaN.
-  pow(x, (+-)0) returns 1 for any x, even a NaN.
-  pow(x, y) returns a NaN and raises the ''invalid'' floating-point exception for finite x < 0 and finite non-integer y.
-  pow(x, -(inf)) returns +(inf) for \| x \| < 1.
-  pow(x, -(inf)) returns +0 for \| x \| > 1.
-  pow(x, +(inf)) returns +0 for \| x \| < 1.
-  pow(x, +(inf)) returns +(inf) for \| x \| > 1.
-  pow(-(inf), y) returns -0 for y an odd integer < 0.
-  pow(-(inf), y) returns +0 for y < 0 and not an odd integer.
-  pow(-(inf), y) returns -(inf) for y an odd integer > 0.
-  pow(-(inf), y) returns +(inf) for y > 0 and not an odd integer.
-  pow(+(inf), y) returns +0 for y < 0.
-  pow(+(inf), y) returns +(inf) for y > 0.

