.. _9899_G.6.1.1:

G.6.1.1 The cacos functions
'''''''''''''''''''''''''''

.. _9899_G.6.1.1p1:

:ref:`1 <9899_G.6.1.1p1>`

-  cacos(conj(z)) = conj(cacos(z)).
-  cacos((+-)0 + i0) returns pi /2 - i0.
-  cacos((+-)0 + iNaN) returns pi /2 + iNaN.
-  cacos(x + i (inf)) returns pi /2 - i (inf), for finite x.
-  cacos(x + iNaN) returns NaN + iNaN and optionally raises the ''invalid'' floating- point exception, for nonzero finite x.
-  cacos(-(inf) + iy) returns pi - i (inf), for positive-signed finite y.
-  cacos(+(inf) + iy) returns +0 - i (inf), for positive-signed finite y.
-  cacos(-(inf) + i (inf)) returns 3pi /4 - i (inf).
-  cacos(+(inf) + i (inf)) returns pi /4 - i (inf).
-  cacos((+-)(inf) + iNaN) returns NaN (+-) i (inf) (where the sign of the imaginary part of the result is unspecified).
-  cacos(NaN + iy) returns NaN + iNaN and optionally raises the ''invalid'' floating- point exception, for finite y.
-  cacos(NaN + i (inf)) returns NaN - i (inf).
-  cacos(NaN + iNaN) returns NaN + iNaN.

