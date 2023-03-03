.. _9899_F.9.6.1:

F.9.6.1 The ceil functions
''''''''''''''''''''''''''

.. _9899_F.9.6.1p1:

:ref:`1 <9899_F.9.6.1p1>`

-  ceil((+-)0) returns (+-)0.
-  ceil((+-)(inf)) returns (+-)(inf).

.. _9899_F.9.6.1p2:

:ref:`2 <9899_F.9.6.1p2>` The double version of ceil behaves as though implemented by

::

    #include <math.h>
    #include <fenv.h>
    #pragma STDC FENV_ACCESS ON
    double ceil(double x)
    {
         double result;
         int save_round = fegetround();
         fesetround(FE_UPWARD);
         result = rint(x); // or nearbyint instead of rint
         fesetround(save_round);
         return result;
    }

