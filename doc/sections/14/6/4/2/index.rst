.. _9899_G.6.4.2:

G.6.4.2 The csqrt functions
'''''''''''''''''''''''''''

.. _9899_G.6.4.2p1:

.. container:: snum

   :ref:`1 <9899_G.6.4.2p1>`



-  csqrt(conj(z)) = conj(csqrt(z)).
-  csqrt((+-)0 + i0) returns +0 + i0.
-  csqrt(x + i (inf)) returns +(inf) + i (inf), for all x (including NaN).
-  csqrt(x + iNaN) returns NaN + iNaN and optionally raises the "invalid" floating- point exception, for finite x.
-  csqrt(-(inf) + iy) returns +0 + i (inf), for finite positive-signed y.
-  csqrt(+(inf) + iy) returns +(inf) + i0, for finite positive-signed y.
-  csqrt(-(inf) + iNaN) returns NaN (+-) i (inf) (where the sign of the imaginary part of the result is unspecified).
-  csqrt(+(inf) + iNaN) returns +(inf) + iNaN.
-  csqrt(NaN + iy) returns NaN + iNaN and optionally raises the "invalid" floating- point exception, for finite y.
-  csqrt(NaN + iNaN) returns NaN + iNaN.

