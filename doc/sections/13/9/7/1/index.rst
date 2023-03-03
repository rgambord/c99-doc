.. _9899_F.9.7.1:

F.9.7.1 The fmod functions
''''''''''''''''''''''''''

.. _9899_F.9.7.1p1:

:ref:`1 <9899_F.9.7.1p1>`

-  fmod((+-)0, y) returns (+-)0 for y not zero.
-  fmod(x, y) returns a NaN and raises the ''invalid'' floating-point exception for x infinite or y zero.
-  fmod(x, (+-)(inf)) returns x for x not infinite.

.. _9899_F.9.7.1p2:

:ref:`2 <9899_F.9.7.1p2>` The double version of fmod behaves as though implemented by

::

    #include <math.h>
    #include <fenv.h>
    #pragma STDC FENV_ACCESS ON
    double fmod(double x, double y)
    {
         double result;
         result = remainder(fabs(x), (y = fabs(y)));
         if (signbit(result)) result += y;
         return copysign(result, x);
    }

