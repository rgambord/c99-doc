.. _9899_G.6.2.2:

G.6.2.2 The casinh functions
''''''''''''''''''''''''''''

.. _9899_G.6.2.2p1:

.. container:: snum

   :ref:`1 <9899_G.6.2.2p1>`



-  casinh(conj(z)) = conj(casinh(z)) and casinh is odd.
-  casinh(+0 + i0) returns 0 + i0.
-  casinh(x + i (inf)) returns +(inf) + ipi /2 for positive-signed finite x.
-  casinh(x + iNaN) returns NaN + iNaN and optionally raises the "invalid" floating-point exception, for finite x.
-  casinh(+(inf) + iy) returns +(inf) + i0 for positive-signed finite y.
-  casinh(+(inf) + i (inf)) returns +(inf) + ipi /4.
-  casinh(+(inf) + iNaN) returns +(inf) + iNaN.
-  casinh(NaN + i0) returns NaN + i0.
-  casinh(NaN + iy) returns NaN + iNaN and optionally raises the "invalid" floating-point exception, for finite nonzero y.
-  casinh(NaN + i (inf)) returns (+-)(inf) + iNaN (where the sign of the real part of the result is unspecified).
-  casinh(NaN + iNaN) returns NaN + iNaN.

