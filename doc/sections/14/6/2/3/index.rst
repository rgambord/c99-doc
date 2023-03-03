.. _9899_G.6.2.3:

G.6.2.3 The catanh functions
''''''''''''''''''''''''''''

.. _9899_G.6.2.3p1:

:ref:`1 <9899_G.6.2.3p1>`

-  catanh(conj(z)) = conj(catanh(z)) and catanh is odd.
-  catanh(+0 + i0) returns +0 + i0.
-  catanh(+0 + iNaN) returns +0 + iNaN.
-  catanh(+1 + i0) returns +(inf) + i0 and raises the ''divide-by-zero'' floating-point exception.
-  catanh(x + i (inf)) returns +0 + ipi /2, for finite positive-signed x.
-  catanh(x + iNaN) returns NaN + iNaN and optionally raises the ''invalid'' floating-point exception, for nonzero finite x.
-  catanh(+(inf) + iy) returns +0 + ipi /2, for finite positive-signed y.
-  catanh(+(inf) + i (inf)) returns +0 + ipi /2.
-  catanh(+(inf) + iNaN) returns +0 + iNaN.
-  catanh(NaN + iy) returns NaN + iNaN and optionally raises the ''invalid'' floating-point exception, for finite y.
-  catanh(NaN + i (inf)) returns (+-)0 + ipi /2 (where the sign of the real part of the result is unspecified).
-  catanh(NaN + iNaN) returns NaN + iNaN.

