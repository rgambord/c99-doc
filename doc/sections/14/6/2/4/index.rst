.. _9899_G.6.2.4:

G.6.2.4 The ccosh functions
'''''''''''''''''''''''''''

.. _9899_G.6.2.4p1:

.. container:: snum

   :ref:`1 <9899_G.6.2.4p1>`



-  ccosh(conj(z)) = conj(ccosh(z)) and ccosh is even.
-  ccosh(+0 + i0) returns 1 + i0.
-  ccosh(+0 + i (inf)) returns NaN (+-) i0 (where the sign of the imaginary part of the result is unspecified) and raises the "invalid" floating-point exception.
-  ccosh(+0 + iNaN) returns NaN (+-) i0 (where the sign of the imaginary part of the result is unspecified).
-  ccosh(x + i (inf)) returns NaN + iNaN and raises the "invalid" floating-point exception, for finite nonzero x.
-  ccosh(x + iNaN) returns NaN + iNaN and optionally raises the "invalid" floating- point exception, for finite nonzero x.
-  ccosh(+(inf) + i0) returns +(inf) + i0.
-  ccosh(+(inf) + iy) returns +(inf) cis(y), for finite nonzero y.
-  ccosh(+(inf) + i (inf)) returns (+-)(inf) + iNaN (where the sign of the real part of the result is unspecified) and raises the "invalid" floating-point exception.
-  ccosh(+(inf) + iNaN) returns +(inf) + iNaN.
-  ccosh(NaN + i0) returns NaN (+-) i0 (where the sign of the imaginary part of the result is unspecified).
-  ccosh(NaN + iy) returns NaN + iNaN and optionally raises the "invalid" floating- point exception, for all nonzero numbers y.
-  ccosh(NaN + iNaN) returns NaN + iNaN.

