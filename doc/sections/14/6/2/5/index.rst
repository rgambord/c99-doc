.. _9899_G.6.2.5:

G.6.2.5 The csinh functions
'''''''''''''''''''''''''''

.. _9899_G.6.2.5p1:

:ref:`1 <9899_G.6.2.5p1>`

-  csinh(conj(z)) = conj(csinh(z)) and csinh is odd.
-  csinh(+0 + i0) returns +0 + i0.
-  csinh(+0 + i (inf)) returns (+-)0 + iNaN (where the sign of the real part of the result is unspecified) and raises the ''invalid'' floating-point exception.
-  csinh(+0 + iNaN) returns (+-)0 + iNaN (where the sign of the real part of the result is unspecified).
-  csinh(x + i (inf)) returns NaN + iNaN and raises the ''invalid'' floating-point exception, for positive finite x.
-  csinh(x + iNaN) returns NaN + iNaN and optionally raises the ''invalid'' floating- point exception, for finite nonzero x.
-  csinh(+(inf) + i0) returns +(inf) + i0.
-  csinh(+(inf) + iy) returns +(inf) cis(y), for positive finite y.
-  csinh(+(inf) + i (inf)) returns (+-)(inf) + iNaN (where the sign of the real part of the result is unspecified) and raises the ''invalid'' floating-point exception.
-  csinh(+(inf) + iNaN) returns (+-)(inf) + iNaN (where the sign of the real part of the result is unspecified).
-  csinh(NaN + i0) returns NaN + i0.
-  csinh(NaN + iy) returns NaN + iNaN and optionally raises the ''invalid'' floating- point exception, for all nonzero numbers y.
-  csinh(NaN + iNaN) returns NaN + iNaN.

