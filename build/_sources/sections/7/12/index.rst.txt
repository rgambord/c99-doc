.. _9899_7.12:

7.12 Mathematics \<math.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index
   4/index
   5/index
   6/index
   7/index
   8/index
   9/index
   10/index
   11/index
   12/index
   13/index
   14/index


.. _9899_7.12p1:

.. container:: snum

   :ref:`1 <9899_7.12p1>`

The header :ref:`\<math.h> <9899_7.12>` declares two types and many mathematical functions and defines several macros. Most synopses specify a family of functions consisting of a principal function with one or more double parameters, a double return value, or both; and other functions with the same name but with f and l suffixes, which are corresponding functions with float and long double parameters, return values, or both.\ [#9899_note198]_ Integer arithmetic functions and conversion functions are discussed later.

.. _9899_7.12p2:

.. container:: snum

   :ref:`2 <9899_7.12p2>`

The types

::

    float_t
    double_t

are floating types at least as wide as float and double, respectively, and such that double_t is at least as wide as float_t. If FLT_EVAL_METHOD equals 0, float_t and double_t are float and double, respectively; if FLT_EVAL_METHOD equals 1, they are both double; if FLT_EVAL_METHOD equals 2, they are both long double; and for other values of FLT_EVAL_METHOD, they are otherwise implementation-defined.\ [#9899_note199]_

.. _9899_7.12p3:

.. container:: snum

   :ref:`3 <9899_7.12p3>`

The macro

::

    HUGE_VAL

expands to a positive double constant expression, not necessarily representable as a float. The macros

::

    HUGE_VALF
    HUGE_VALL

are respectively float and long double analogs of HUGE_VAL.\ [#9899_note200]_

.. _9899_7.12p4:

.. container:: snum

   :ref:`4 <9899_7.12p4>`

The macro

::

    INFINITY

expands to a constant expression of type float representing positive or unsigned infinity, if available; else to a positive constant of type float that overflows at translation time.\ [#9899_note201]_

.. _9899_7.12p5:

.. container:: snum

   :ref:`5 <9899_7.12p5>`

The macro

::

    NAN

is defined if and only if the implementation supports quiet NaNs for the float type. It expands to a constant expression of type float representing a quiet NaN.

.. _9899_7.12p6:

.. container:: snum

   :ref:`6 <9899_7.12p6>`

The number classification macros

::

    FP_INFINITE
    FP_NAN
    FP_NORMAL
    FP_SUBNORMAL
    FP_ZERO

represent the mutually exclusive kinds of floating-point values. They expand to integer constant expressions with distinct values. Additional implementation-defined floating- point classifications, with macro definitions beginning with FP\_ and an uppercase letter, may also be specified by the implementation.

.. _9899_7.12p7:

.. container:: snum

   :ref:`7 <9899_7.12p7>`

The macro

::

    FP_FAST_FMA

is optionally defined. If defined, it indicates that the fma function generally executes about as fast as, or faster than, a multiply and an add of double operands.\ [#9899_note202]_ The macros

::

    FP_FAST_FMAF
    FP_FAST_FMAL

are, respectively, float and long double analogs of FP_FAST_FMA. If defined, these macros expand to the integer constant 1.

.. _9899_7.12p8:

.. container:: snum

   :ref:`8 <9899_7.12p8>`

The macros

::

    FP_ILOGB0
    FP_ILOGBNAN

expand to integer constant expressions whose values are returned by ilogb(x) if x is zero or NaN, respectively. The value of FP_ILOGB0 shall be either INT_MIN or -INT_MAX. The value of FP_ILOGBNAN shall be either INT_MAX or INT_MIN.

.. _9899_7.12p9:

.. container:: snum

   :ref:`9 <9899_7.12p9>`

The macros

::

    MATH_ERRNO
    MATH_ERREXCEPT

expand to the integer constants 1 and 2, respectively; the macro

::

    math_errhandling

expands to an expression that has type int and the value MATH_ERRNO, MATH_ERREXCEPT, or the bitwise OR of both. The value of math_errhandling is constant for the duration of the program. It is unspecified whether math_errhandling is a macro or an identifier with external linkage. If a macro definition is suppressed or a program defines an identifier with the name math_errhandling, the behavior is undefined. If the expression math_errhandling & MATH_ERREXCEPT can be nonzero, the implementation shall define the macros FE_DIVBYZERO, FE_INVALID, and FE_OVERFLOW in :ref:`\<fenv.h> <9899_7.6>`.









.. rubric:: Footnotes

.. [#9899_note198] Particularly on systems with wide expression evaluation, a :ref:`\<math.h> <9899_7.12>` function might pass arguments and return values in wider format than the synopsis prototype indicates.
.. [#9899_note199] The types float_t and double_t are intended to be the implementation's most efficient types at least as wide as float and double, respectively. For FLT_EVAL_METHOD equal 0, 1, or 2, the type float_t is the narrowest type used by the implementation to evaluate floating expressions.
.. [#9899_note200] HUGE_VAL, HUGE_VALF, and HUGE_VALL can be positive infinities in an implementation that supports infinities.
.. [#9899_note201] In this case, using INFINITY will violate the constraint in :ref:`6.4.4 <9899_6.4.4>` and thus require a diagnostic.
.. [#9899_note202] Typically, the FP_FAST_FMA macro is defined if and only if the fma function is implemented directly with a hardware multiply-add instruction. Software implementations are expected to be substantially slower.
