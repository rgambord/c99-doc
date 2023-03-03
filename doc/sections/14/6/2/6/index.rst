.. _9899_G.6.2.6:

G.6.2.6 The ctanh functions
'''''''''''''''''''''''''''

.. _9899_G.6.2.6p1:

:ref:`1 <9899_G.6.2.6p1>`

-  ctanh(conj(z)) = conj(ctanh(z))and ctanh is odd.
-  ctanh(+0 + i0) returns +0 + i0.
-  ctanh(x + i (inf)) returns NaN + iNaN and raises the ''invalid'' floating-point exception, for finite x.
-  ctanh(x + iNaN) returns NaN + iNaN and optionally raises the ''invalid'' floating- point exception, for finite x.
-  ctanh(+(inf) + iy) returns 1 + i0 sin(2y), for positive-signed finite y.
-  ctanh(+(inf) + i (inf)) returns 1 (+-) i0 (where the sign of the imaginary part of the result is unspecified).
-  ctanh(+(inf) + iNaN) returns 1 (+-) i0 (where the sign of the imaginary part of the result is unspecified).
-  ctanh(NaN + i0) returns NaN + i0.
-  ctanh(NaN + iy) returns NaN + iNaN and optionally raises the ''invalid'' floating- point exception, for all nonzero numbers y.
-  ctanh(NaN + iNaN) returns NaN + iNaN.

