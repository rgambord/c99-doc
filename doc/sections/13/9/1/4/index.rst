.. _9899_F.9.1.4:

F.9.1.4 The atan2 functions
'''''''''''''''''''''''''''

.. _9899_F.9.1.4p1:

:ref:`1 <9899_F.9.1.4p1>`

-  atan2((+-)0, -0) returns (+-)pi .\ [#9899_note322]_
-  atan2((+-)0, +0) returns (+-)0.
-  atan2((+-)0, x) returns (+-)pi for x < 0.
-  atan2((+-)0, x) returns (+-)0 for x > 0.
-  atan2(y, (+-)0) returns -pi /2 for y < 0.
-  atan2(y, (+-)0) returns pi /2 for y > 0.
-  atan2((+-)y, -(inf)) returns (+-)pi for finite y > 0.
-  atan2((+-)y, +(inf)) returns (+-)0 for finite y > 0.
-  atan2((+-)(inf), x) returns (+-)pi /2 for finite x.
-  atan2((+-)(inf), -(inf)) returns (+-)3pi /4.
-  atan2((+-)(inf), +(inf)) returns (+-)pi /4.





.. rubric:: Footnotes

.. [#9899_note322] atan2(0, 0) does not raise the ''invalid'' floating-point exception, nor does atan2( y , 0) raise the ''divide-by-zero'' floating-point exception.
