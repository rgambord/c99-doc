.. _9899_G.6.3.2:

G.6.3.2 The clog functions
''''''''''''''''''''''''''

.. _9899_G.6.3.2p1:

:ref:`1 <9899_G.6.3.2p1>`

-  clog(conj(z)) = conj(clog(z)).
-  clog(-0 + i0) returns -(inf) + ipi and raises the ''divide-by-zero'' floating-point exception.
-  clog(+0 + i0) returns -(inf) + i0 and raises the ''divide-by-zero'' floating-point exception.
-  clog(x + i (inf)) returns +(inf) + ipi /2, for finite x.
-  clog(x + iNaN) returns NaN + iNaN and optionally raises the ''invalid'' floating- point exception, for finite x.
-  clog(-(inf) + iy) returns +(inf) + ipi , for finite positive-signed y.
-  clog(+(inf) + iy) returns +(inf) + i0, for finite positive-signed y.
-  clog(-(inf) + i (inf)) returns +(inf) + i3pi /4.
-  clog(+(inf) + i (inf)) returns +(inf) + ipi /4.
-  clog((+-)(inf) + iNaN) returns +(inf) + iNaN.
-  clog(NaN + iy) returns NaN + iNaN and optionally raises the ''invalid'' floating- point exception, for finite y.
-  clog(NaN + i (inf)) returns +(inf) + iNaN.
-  clog(NaN + iNaN) returns NaN + iNaN.

