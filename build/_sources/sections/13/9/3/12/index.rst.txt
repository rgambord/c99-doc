.. _9899_F.9.3.12:

F.9.3.12 The modf functions
'''''''''''''''''''''''''''

.. _9899_F.9.3.12p1:

.. container:: snum

   :ref:`1 <9899_F.9.3.12p1>`



-  modf((+-)x, iptr) returns a result with the same sign as x.
-  modf((+-)(inf), iptr) returns (+-)0 and stores (+-)(inf) in the object pointed to by iptr.
-  modf(NaN, iptr) stores a NaN in the object pointed to by iptr (and returns a NaN).

.. _9899_F.9.3.12p2:

.. container:: snum

   :ref:`2 <9899_F.9.3.12p2>`

modf behaves as though implemented by

::

    #include <math.h>
    #include <fenv.h>
    #pragma STDC FENV_ACCESS ON
    double modf(double value, double *iptr)
    {
         int save_round = fegetround();
         fesetround(FE_TOWARDZERO);
         *iptr = nearbyint(value);
         fesetround(save_round);
         return copysign(
              isinf(value) ? 0.0 :
                   value - (*iptr), value);
    }

