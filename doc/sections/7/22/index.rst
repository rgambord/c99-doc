.. _9899_7.22:

7.22 Type-generic math \<tgmath.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _9899_7.22p1:

:ref:`1 <9899_7.22p1>` The header :ref:`\<tgmath.h> <9899_7.22>` includes the headers :ref:`\<math.h> <9899_7.12>` and :ref:`\<complex.h> <9899_7.3>` and defines several type-generic macros.

.. _9899_7.22p2:

:ref:`2 <9899_7.22p2>` Of the :ref:`\<math.h> <9899_7.12>` and :ref:`\<complex.h> <9899_7.3>` functions without an f (float) or l (long double) suffix, several have one or more parameters whose corresponding real type is double. For each such function, except modf, there is a corresponding type-generic macro.\ [#9899_note272]_ The parameters whose corresponding real type is double in the function synopsis are generic parameters. Use of the macro invokes a function whose corresponding real type and type domain are determined by the arguments for the generic parameters.\ [#9899_note273]_

.. _9899_7.22p3:

:ref:`3 <9899_7.22p3>` Use of the macro invokes a function whose generic parameters have the corresponding real type determined as follows:

-  First, if any argument for generic parameters has type long double, the type determined is long double.
-  Otherwise, if any argument for generic parameters has type double or is of integer type, the type determined is double.
-  Otherwise, the type determined is float.

.. _9899_7.22p4:

:ref:`4 <9899_7.22p4>` For each unsuffixed function in :ref:`\<math.h> <9899_7.12>` for which there is a function in :ref:`\<complex.h> <9899_7.3>` with the same name except for a c prefix, the corresponding type- generic macro (for both functions) has the same name as the function in :ref:`\<math.h> <9899_7.12>`. The corresponding type-generic macro for fabs and cabs is fabs.

.. code-block:: text

    <math.h>          <complex.h>           type-generic
    function          function              macro

    acos              cacos                 acos
    asin              casin                 asin
    atan              catan                 atan
    acosh             cacosh                acosh
    asinh             casinh                asinh
    atanh             catanh                atanh
    cos               ccos                  cos
    sin               csin                  sin
    tan               ctan                  tan
    cosh              ccosh                 cosh
    sinh              csinh                 sinh
    tanh              ctanh                 tanh
    exp               cexp                  exp
    log               clog                  log
    pow               cpow                  pow
    sqrt              csqrt                 sqrt
    fabs              cabs                  fabs

If at least one argument for a generic parameter is complex, then use of the macro invokes a complex function; otherwise, use of the macro invokes a real function.

.. _9899_7.22p5:

:ref:`5 <9899_7.22p5>` For each unsuffixed function in :ref:`\<math.h> <9899_7.12>` without a c-prefixed counterpart in :ref:`\<complex.h> <9899_7.3>` (except modf), the corresponding type-generic macro has the same name as the function. These type-generic macros are:

::

    atan2                fma                  llround              remainder
    cbrt                 fmax                 log10                remquo
    ceil                 fmin                 log1p                rint
    copysign             fmod                 log2                 round
    erf                  frexp                logb                 scalbn
    erfc                 hypot                lrint                scalbln
    exp2                 ilogb                lround               tgamma
    expm1                ldexp                nearbyint            trunc
    fdim                 lgamma               nextafter
    floor                llrint               nexttoward

If all arguments for generic parameters are real, then use of the macro invokes a real function; otherwise, use of the macro results in undefined behavior.

.. _9899_7.22p6:

:ref:`6 <9899_7.22p6>` For each unsuffixed function in :ref:`\<complex.h> <9899_7.3>` that is not a c-prefixed counterpart to a function in :ref:`\<math.h> <9899_7.12>`, the corresponding type-generic macro has the same name as the function. These type-generic macros are:

::

    carg                    conj                     creal
    cimag                   cproj

Use of the macro with any real or complex argument invokes a complex function.

.. _9899_7.22p7:

:ref:`7 <9899_7.22p7>` EXAMPLE With the declarations

::

    #include <tgmath.h>
    int n;
    float f;
    double d;
    long double ld;
    float complex fc;
    double complex dc;
    long double complex ldc;

functions invoked by use of type-generic macros are shown in the following table:

.. code-block:: text

    macro use                                  invokes

                exp(n)                              exp(n), the function
                acosh(f)                            acoshf(f)
                sin(d)                              sin(d), the function
                atan(ld)                            atanl(ld)
                log(fc)                             clogf(fc)
                sqrt(dc)                            csqrt(dc)
                pow(ldc, f)                         cpowl(ldc, f)
                remainder(n, n)                     remainder(n, n), the function
                nextafter(d, f)                     nextafter(d, f), the function
                nexttoward(f, ld)                   nexttowardf(f, ld)
                copysign(n, ld)                     copysignl(n, ld)
                ceil(fc)                            undefined behavior
                rint(dc)                            undefined behavior
                fmax(ldc, ld)                       undefined behavior
                carg(n)                             carg(n), the function
                cproj(f)                            cprojf(f)
                creal(d)                            creal(d), the function
                cimag(ld)                           cimagl(ld)
                fabs(fc)                            cabsf(fc)
                carg(dc)                            carg(dc), the function
                cproj(ldc)                          cprojl(ldc)






.. rubric:: Footnotes

.. [#9899_note272] Like other function-like macros in Standard libraries, each type-generic macro can be suppressed to make available the corresponding ordinary function.
.. [#9899_note273] If the type of the argument is not compatible with the type of the parameter for the selected function, the behavior is undefined.
