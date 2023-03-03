.. _9899_F.9.6.6:

F.9.6.6 The round functions
'''''''''''''''''''''''''''

.. _9899_F.9.6.6p1:

:ref:`1 <9899_F.9.6.6p1>`

-  round((+-)0) returns (+-)0.
-  round((+-)(inf)) returns (+-)(inf).

.. _9899_F.9.6.6p2:

:ref:`2 <9899_F.9.6.6p2>` The double version of round behaves as though implemented by

::

    #include <math.h>
    #include <fenv.h>
    #pragma STDC FENV_ACCESS ON
    double round(double x)
    {
         double result;
         fenv_t save_env;
         feholdexcept(&save_env);
         result = rint(x);
         if (fetestexcept(FE_INEXACT)) {
              fesetround(FE_TOWARDZERO);
              result = rint(copysign(0.5 + fabs(x), x));
         }
         feupdateenv(&save_env);
         return result;
    }

The round functions may, but are not required to, raise the ''inexact'' floating-point exception for non-integer numeric arguments, as this implementation does.

