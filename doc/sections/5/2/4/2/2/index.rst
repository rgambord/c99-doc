.. _9899_5.2.4.2.2:

5.2.4.2.2 Characteristics of floating types \<float.h>
""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. _9899_5.2.4.2.2p1:

.. container:: snum

   :ref:`1 <9899_5.2.4.2.2p1>`

The characteristics of floating types are defined in terms of a model that describes a representation of floating-point numbers and values that provide information about an implementation's floating-point arithmetic.\ [#9899_note16]_ The following parameters are used to define the model for each floating-point type:

.. code-block:: text

    s          sign ((+-)1)
    b          base or radix of exponent representation (an integer > 1)
    e          exponent (an integer between a minimum emin and a maximum emax )
    p          precision (the number of base-b digits in the significand)
    fk         nonnegative integers less than b (the significand digits)

.. _9899_5.2.4.2.2p2:

.. container:: snum

   :ref:`2 <9899_5.2.4.2.2p2>`

A floating-point number (x) is defined by the following model:

.. code-block:: text

    p
           x = s be  (Sum) fk b-k ,   emin <= e <= emax
                      k=1

.. _9899_5.2.4.2.2p3:

.. container:: snum

   :ref:`3 <9899_5.2.4.2.2p3>`

In addition to normalized floating-point numbers ( f\ :sub:`1` > 0 if x != 0), floating types may be able to contain other kinds of floating-point numbers, such as subnormal floating-point numbers (x != 0, e = emin , f\ :sub:`1` = 0) and unnormalized floating-point numbers (x != 0, e > emin , f\ :sub:`1` = 0), and values that are not floating-point numbers, such as infinities and NaNs. A NaN is an encoding signifying Not-a-Number. A quiet NaN propagates through almost every arithmetic operation without raising a floating-point exception; a signaling NaN generally raises a floating-point exception when occurring as an arithmetic operand.\ `17) <note17>`

.. _9899_5.2.4.2.2p4:

.. container:: snum

   :ref:`4 <9899_5.2.4.2.2p4>`

An implementation may give zero and non-numeric values (such as infinities and NaNs) a sign or may leave them unsigned. Wherever such values are unsigned, any requirement in this International Standard to retrieve the sign shall produce an unspecified sign, and any requirement to set the sign shall be ignored.

.. _9899_5.2.4.2.2p5:

.. container:: snum

   :ref:`5 <9899_5.2.4.2.2p5>`

The accuracy of the floating-point operations (+, -, \*, /) and of the library functions in :ref:`\<math.h> <9899_7.12>` and :ref:`\<complex.h> <9899_7.3>` that return floating-point results is implementation- defined, as is the accuracy of the conversion between floating-point internal representations and string representations performed by the library functions in :ref:`\<stdio.h> <9899_7.19>`, :ref:`\<stdlib.h> <9899_7.20>`, and :ref:`\<wchar.h> <9899_7.24>`. The implementation may state that the accuracy is unknown.

.. _9899_5.2.4.2.2p6:

.. container:: snum

   :ref:`6 <9899_5.2.4.2.2p6>`

All integer values in the :ref:`\<float.h> <9899_7.7>` header, except FLT_ROUNDS, shall be constant expressions suitable for use in `#if` preprocessing directives; all floating values shall be constant expressions. All except DECIMAL_DIG, FLT_EVAL_METHOD, FLT_RADIX, and FLT_ROUNDS have separate names for all three floating-point types. The floating-point model representation is provided for all values except FLT_EVAL_METHOD and FLT_ROUNDS.

.. _9899_5.2.4.2.2p7:

.. container:: snum

   :ref:`7 <9899_5.2.4.2.2p7>`

The rounding mode for floating-point addition is characterized by the implementation- defined value of FLT_ROUNDS:[#9899_note18]_

.. code-block:: text

    -1      indeterminable
     0      toward zero
     1      to nearest
     2      toward positive infinity
     3      toward negative infinity

All other values for FLT_ROUNDS characterize implementation-defined rounding behavior.

.. _9899_5.2.4.2.2p8:

.. container:: snum

   :ref:`8 <9899_5.2.4.2.2p8>`

Except for assignment and cast (which remove all extra range and precision), the values of operations with floating operands and values subject to the usual arithmetic conversions and of floating constants are evaluated to a format whose range and precision may be greater than required by the type. The use of evaluation formats is characterized by the implementation-defined value of FLT_EVAL_METHOD:[#9899_note19]_

.. code-block:: text

    -1        indeterminable;
     0        evaluate all operations and constants just to the range and precision of the
              type;
     1        evaluate operations and constants of type float and double to the
              range and precision of the double type, evaluate long double
              operations and constants to the range and precision of the long double
              type;
     2        evaluate all operations and constants to the range and precision of the
              long double type.

All other negative values for FLT_EVAL_METHOD characterize implementation-defined behavior.

.. _9899_5.2.4.2.2p9:

.. container:: snum

   :ref:`9 <9899_5.2.4.2.2p9>`

The values given in the following list shall be replaced by constant expressions with implementation-defined values that are greater or equal in magnitude (absolute value) to those shown, with the same sign:

-  radix of exponent representation, b

::

    FLT_RADIX                                                 2

-  number of base-FLT_RADIX digits in the floating-point significand, p

::

    FLT_MANT_DIG
    DBL_MANT_DIG
    LDBL_MANT_DIG

-  number of decimal digits, n, such that any floating-point number in the widest supported floating type with pmax radix b digits can be rounded to a floating-point number with n decimal digits and back again without change to the value,

.. code-block:: text

    { pmax log10 b       if b is a power of 10
    {
    { ⌈1 + pmax log10 b⌉ otherwise

::

    DECIMAL_DIG                                            10

-  number of decimal digits, q, such that any floating-point number with q decimal digits can be rounded into a floating-point number with p radix b digits and back again without change to the q decimal digits,

::

    { p log10 b          if b is a power of 10
    {
    { [_( p - 1) log10 b_] otherwise

.. code-block:: text

    FLT_DIG                                         6
    DBL_DIG                                        10
    LDBL_DIG                                       10

-  minimum negative integer such that FLT_RADIX raised to one less than that power is a normalized floating-point number, emin

::

    FLT_MIN_EXP
    DBL_MIN_EXP
    LDBL_MIN_EXP

-  minimum negative integer such that 10 raised to that power is in the range of normalized floating-point numbers, ⌈log10 b\ :sup:`emin -1`\ ⌉

::

    FLT_MIN_10_EXP                                 -37
    DBL_MIN_10_EXP                                 -37
    LDBL_MIN_10_EXP                                -37

-  maximum integer such that FLT_RADIX raised to one less than that power is a representable finite floating-point number, emax

::

    FLT_MAX_EXP
    DBL_MAX_EXP
    LDBL_MAX_EXP

-  maximum integer such that 10 raised to that power is in the range of representable finite floating-point numbers, ⌊log10 ((1 - b\ :sup:`-p`)b\ :sup:`emax`)⌋

::

    FLT_MAX_10_EXP                                 +37
    DBL_MAX_10_EXP                                 +37
    LDBL_MAX_10_EXP                                +37

.. _9899_5.2.4.2.2p10:

.. container:: snum

   :ref:`10 <9899_5.2.4.2.2p10>`

The values given in the following list shall be replaced by constant expressions with implementation-defined values that are greater than or equal to those shown:

-  maximum representable finite floating-point number, (1 - b\ :sup:`-p`)b\ :sup:`emax`

::

    FLT_MAX                                     1E+37
    DBL_MAX                                     1E+37
    LDBL_MAX                                    1E+37

.. _9899_5.2.4.2.2p11:

.. container:: snum

   :ref:`11 <9899_5.2.4.2.2p11>`

The values given in the following list shall be replaced by constant expressions with implementation-defined (positive) values that are less than or equal to those shown:

-  the difference between 1 and the least value greater than 1 that is representable in the given floating point type, b\ :sup:`1-p`

::

    FLT_EPSILON                                         1E-5
    DBL_EPSILON                                         1E-9
    LDBL_EPSILON                                        1E-9

-  minimum normalized positive floating-point number, b\ :sup:`emin -1`

::

    FLT_MIN                                            1E-37
    DBL_MIN                                            1E-37
    LDBL_MIN                                           1E-37

.. rubric:: Recommended practice

.. _9899_5.2.4.2.2p12:

.. container:: snum

   :ref:`12 <9899_5.2.4.2.2p12>`

Conversion from (at least) double to decimal with DECIMAL_DIG digits and back should be the identity function.

.. _9899_5.2.4.2.2p13:

.. container:: snum

   :ref:`13 <9899_5.2.4.2.2p13>`

EXAMPLE 1 The following describes an artificial floating-point representation that meets the minimum requirements of this International Standard, and the appropriate values in a :ref:`\<float.h> <9899_7.7>` header for type float:

.. code-block:: text

    6
          x = s 16e   (Sum) fk 16-k ,   -31 <= e <= +32
                      k=1

.. code-block:: text

    FLT_RADIX                                  16
    FLT_MANT_DIG                                6
    FLT_EPSILON                   9.53674316E-07F
    FLT_DIG                                     6
    FLT_MIN_EXP                               -31
    FLT_MIN                       2.93873588E-39F
    FLT_MIN_10_EXP                            -38
    FLT_MAX_EXP                               +32
    FLT_MAX                       3.40282347E+38F
    FLT_MAX_10_EXP                            +38

.. _9899_5.2.4.2.2p14:

.. container:: snum

   :ref:`14 <9899_5.2.4.2.2p14>`

EXAMPLE 2 The following describes floating-point representations that also meet the requirements for single-precision and double-precision normalized numbers in IEC 60559,\ [#9899_note20]_ and the appropriate values in a :ref:`\<float.h> <9899_7.7>` header for types float and double:

.. code-block:: text

    24
          xf = s 2e  (Sum) fk 2-k ,   -125 <= e <= +128
                      k=1

.. code-block:: text

    53
          xd = s 2e  (Sum) fk 2-k ,   -1021 <= e <= +1024
                      k=1

.. code-block:: text

    FLT_RADIX                                   2
    DECIMAL_DIG                                17
    FLT_MANT_DIG                               24
    FLT_EPSILON                   1.19209290E-07F // decimal constant
    FLT_EPSILON                          0X1P-23F // hex constant

.. code-block:: text

    FLT_DIG                           6
    FLT_MIN_EXP                    -125
    FLT_MIN             1.17549435E-38F               // decimal constant
    FLT_MIN                   0X1P-126F               // hex constant
    FLT_MIN_10_EXP                  -37
    FLT_MAX_EXP                    +128
    FLT_MAX             3.40282347E+38F               // decimal constant
    FLT_MAX             0X1.fffffeP127F               // hex constant
    FLT_MAX_10_EXP                  +38
    DBL_MANT_DIG                     53
    DBL_EPSILON 2.2204460492503131E-16                // decimal constant
    DBL_EPSILON                 0X1P-52               // hex constant
    DBL_DIG                          15
    DBL_MIN_EXP                   -1021
    DBL_MIN     2.2250738585072014E-308               // decimal constant
    DBL_MIN                   0X1P-1022               // hex constant
    DBL_MIN_10_EXP                 -307
    DBL_MAX_EXP                   +1024
    DBL_MAX     1.7976931348623157E+308               // decimal constant
    DBL_MAX      0X1.fffffffffffffP1023               // hex constant
    DBL_MAX_10_EXP                 +308

If a type wider than double were supported, then DECIMAL_DIG would be greater than 17. For example, if the widest type were to use the minimal-width IEC 60559 double-extended format (64 bits of precision), then DECIMAL_DIG would be 21.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.10.1`
   - :ref:`9899_7.3`
   - :ref:`9899_7.3`
   - :ref:`9899_7.24`
   - :ref:`9899_7.24`
   - :ref:`9899_7.6`
   - :ref:`9899_7.6`
   - :ref:`9899_7.20`
   - :ref:`9899_7.20`
   - :ref:`9899_7.19`
   - :ref:`9899_7.19`
   - :ref:`9899_7.12`
   - :ref:`9899_7.12`









.. rubric:: Footnotes

.. [#9899_note16] The floating-point model is intended to clarify the description of each floating-point characteristic and does not require the floating-point arithmetic of the implementation to be identical.
.. [#9899_note18] Evaluation of FLT_ROUNDS correctly reflects any execution-time change of rounding mode through the function fesetround in :ref:`\<fenv.h> <9899_7.6>`.
.. [#9899_note19] The evaluation method determines evaluation formats of expressions involving all floating types, not just real types. For example, if FLT_EVAL_METHOD is 1, then the product of two float \_Complex operands is represented in the double \_Complex format, and its parts are evaluated to double.
.. [#9899_note20] The floating-point model in that standard sums powers of b from zero, so the values of the exponent limits are one less than shown here.
