.. _9899_F.9.10.1:

F.9.10.1 The fma functions
''''''''''''''''''''''''''

.. _9899_F.9.10.1p1:

:ref:`1 <9899_F.9.10.1p1>`

-  fma(x, y, z) computes xy + z, correctly rounded once.
-  fma(x, y, z) returns a NaN and optionally raises the ''invalid'' floating-point exception if one of x and y is infinite, the other is zero, and z is a NaN.
-  fma(x, y, z) returns a NaN and raises the ''invalid'' floating-point exception if one of x and y is infinite, the other is zero, and z is not a NaN.
-  fma(x, y, z) returns a NaN and raises the ''invalid'' floating-point exception if x times y is an exact infinity and z is also an infinity but with the opposite sign.

