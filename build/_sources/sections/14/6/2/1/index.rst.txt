.. _9899_G.6.2.1:

G.6.2.1 The cacosh functions
''''''''''''''''''''''''''''

.. _9899_G.6.2.1p1:

.. container:: snum

   :ref:`1 <9899_G.6.2.1p1>`



-  cacosh(conj(z)) = conj(cacosh(z)).
-  cacosh((+-)0 + i0) returns +0 + ipi /2.
-  cacosh(x + i (inf)) returns +(inf) + ipi /2, for finite x.
-  cacosh(x + iNaN) returns NaN + iNaN and optionally raises the "invalid" floating-point exception, for finite x.
-  cacosh(-(inf) + iy) returns +(inf) + ipi , for positive-signed finite y.
-  cacosh(+(inf) + iy) returns +(inf) + i0, for positive-signed finite y.
-  cacosh(-(inf) + i (inf)) returns +(inf) + i3pi /4.
-  cacosh(+(inf) + i (inf)) returns +(inf) + ipi /4.
-  cacosh((+-)(inf) + iNaN) returns +(inf) + iNaN.
-  cacosh(NaN + iy) returns NaN + iNaN and optionally raises the "invalid" floating-point exception, for finite y.
-  cacosh(NaN + i (inf)) returns +(inf) + iNaN.
-  cacosh(NaN + iNaN) returns NaN + iNaN.

