.. _9899_G.6.3.1:

G.6.3.1 The cexp functions
''''''''''''''''''''''''''

.. _9899_G.6.3.1p1:

:ref:`1 <9899_G.6.3.1p1>`

-  cexp(conj(z)) = conj(cexp(z)).
-  cexp((+-)0 + i0) returns 1 + i0.
-  cexp(x + i (inf)) returns NaN + iNaN and raises the ''invalid'' floating-point exception, for finite x.
-  cexp(x + iNaN) returns NaN + iNaN and optionally raises the ''invalid'' floating- point exception, for finite x.
-  cexp(+(inf) + i0) returns +(inf) + i0.
-  cexp(-(inf) + iy) returns +0 cis(y), for finite y.
-  cexp(+(inf) + iy) returns +(inf) cis(y), for finite nonzero y.
-  cexp(-(inf) + i (inf)) returns (+-)0 (+-) i0 (where the signs of the real and imaginary parts of the result are unspecified).
-  cexp(+(inf) + i (inf)) returns (+-)(inf) + iNaN and raises the ''invalid'' floating-point exception (where the sign of the real part of the result is unspecified).
-  cexp(-(inf) + iNaN) returns (+-)0 (+-) i0 (where the signs of the real and imaginary parts of the result are unspecified).
-  cexp(+(inf) + iNaN) returns (+-)(inf) + iNaN (where the sign of the real part of the result is unspecified).
-  cexp(NaN + i0) returns NaN + i0.
-  cexp(NaN + iy) returns NaN + iNaN and optionally raises the ''invalid'' floating- point exception, for all nonzero numbers y.
-  cexp(NaN + iNaN) returns NaN + iNaN.

