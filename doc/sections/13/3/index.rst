.. _9899_F.3:

F.3 Operators and functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _9899_F.3p1:

.. container:: snum

   :ref:`1 <9899_F.3p1>`

C operators and functions provide IEC 60559 required and recommended facilities as listed below.

-  The +, -, \*, and / operators provide the IEC 60559 add, subtract, multiply, and divide operations.
-  The sqrt functions in :ref:`\<math.h> <9899_7.12>` provide the IEC 60559 square root operation.
-  The remainder functions in :ref:`\<math.h> <9899_7.12>` provide the IEC 60559 remainder operation. The remquo functions in :ref:`\<math.h> <9899_7.12>` provide the same operation but with additional information.
-  The rint functions in :ref:`\<math.h> <9899_7.12>` provide the IEC 60559 operation that rounds a floating-point number to an integer value (in the same precision). The nearbyint functions in :ref:`\<math.h> <9899_7.12>` provide the nearbyinteger function recommended in the Appendix to ANSI/IEEE 854.
-  The conversions for floating types provide the IEC 60559 conversions between floating-point precisions.
-  The conversions from integer to floating types provide the IEC 60559 conversions from integer to floating point.
-  The conversions from floating to integer types provide IEC 60559-like conversions but always round toward zero.
-  The lrint and llrint functions in :ref:`\<math.h> <9899_7.12>` provide the IEC 60559 conversions, which honor the directed rounding mode, from floating point to the long int and long long int integer formats. The lrint and llrint functions can be used to implement IEC 60559 conversions from floating to other integer formats.
-  The translation time conversion of floating constants and the strtod, strtof, strtold, fprintf, fscanf, and related library functions in :ref:`\<stdlib.h> <9899_7.20>`, :ref:`\<stdio.h> <9899_7.19>`, and :ref:`\<wchar.h> <9899_7.24>` provide IEC 60559 binary-decimal conversions. The strtold function in :ref:`\<stdlib.h> <9899_7.20>` provides the conv function recommended in the Appendix to ANSI/IEEE 854.
-  The relational and equality operators provide IEC 60559 comparisons. IEC 60559 identifies a need for additional comparison predicates to facilitate writing code that accounts for NaNs. The comparison macros (isgreater, isgreaterequal, isless, islessequal, islessgreater, and isunordered) in :ref:`\<math.h> <9899_7.12>` supplement the language operators to address this need. The islessgreater and isunordered macros provide respectively a quiet version of the <> predicate and the unordered predicate recommended in the Appendix to IEC 60559.
-  The feclearexcept, feraiseexcept, and fetestexcept functions in :ref:`\<fenv.h> <9899_7.6>` provide the facility to test and alter the IEC 60559 floating-point exception status flags. The fegetexceptflag and fesetexceptflag functions in :ref:`\<fenv.h> <9899_7.6>` provide the facility to save and restore all five status flags at one time. These functions are used in conjunction with the type fexcept_t and the floating-point exception macros (FE_INEXACT, FE_DIVBYZERO, FE_UNDERFLOW, FE_OVERFLOW, FE_INVALID) also in :ref:`\<fenv.h> <9899_7.6>`.
-  The fegetround and fesetround functions in :ref:`\<fenv.h> <9899_7.6>` provide the facility to select among the IEC 60559 directed rounding modes represented by the rounding direction macros in :ref:`\<fenv.h> <9899_7.6>` (FE_TONEAREST, FE_UPWARD, FE_DOWNWARD, FE_TOWARDZERO) and the values 0, 1, 2, and 3 of FLT_ROUNDS are the IEC 60559 directed rounding modes.
-  The fegetenv, feholdexcept, fesetenv, and feupdateenv functions in :ref:`\<fenv.h> <9899_7.6>` provide a facility to manage the floating-point environment, comprising the IEC 60559 status flags and control modes.
-  The copysign functions in :ref:`\<math.h> <9899_7.12>` provide the copysign function recommended in the Appendix to IEC 60559.
-  The unary minus (-) operator provides the minus (-) operation recommended in the Appendix to IEC 60559.
-  The scalbn and scalbln functions in :ref:`\<math.h> <9899_7.12>` provide the scalb function recommended in the Appendix to IEC 60559.
-  The logb functions in :ref:`\<math.h> <9899_7.12>` provide the logb function recommended in the Appendix to IEC 60559, but following the newer specifications in ANSI/IEEE 854.
-  The nextafter and nexttoward functions in :ref:`\<math.h> <9899_7.12>` provide the nextafter function recommended in the Appendix to IEC 60559 (but with a minor change to better handle signed zeros).
-  The isfinite macro in :ref:`\<math.h> <9899_7.12>` provides the finite function recommended in the Appendix to IEC 60559.
-  The isnan macro in :ref:`\<math.h> <9899_7.12>` provides the isnan function recommended in the Appendix to IEC 60559.
-  The signbit macro and the fpclassify macro in :ref:`\<math.h> <9899_7.12>`, used in conjunction with the number classification macros (FP_NAN, FP_INFINITE, FP_NORMAL, FP_SUBNORMAL, FP_ZERO), provide the facility of the class function recommended in the Appendix to IEC 60559 (except that the classification macros defined in :ref:`7.12.3 <9899_7.12.3>` do not distinguish signaling from quiet NaNs).

