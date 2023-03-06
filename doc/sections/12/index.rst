.. _9899_E:

Annex E
-------

(informative)

Implementation limits

.. _9899_Ep1:

.. container:: snum

   :ref:`1 <9899_Ep1>`

The contents of the header :ref:`\<limits.h> <9899_7.10>` are given below, in alphabetical order. The minimum magnitudes shown shall be replaced by implementation-defined magnitudes with the same sign. The values shall all be constant expressions suitable for use in `#if` preprocessing directives. The components are described further in :ref:`5.2.4.2.1 <9899_5.2.4.2.1>`.

::

    #define     CHAR_BIT                               8
    #define     CHAR_MAX          UCHAR_MAX or SCHAR_MAX
    #define     CHAR_MIN                  0 or SCHAR_MIN
    #define     INT_MAX                           +32767
    #define     INT_MIN                           -32767
    #define     LONG_MAX                     +2147483647
    #define     LONG_MIN                     -2147483647
    #define     LLONG_MAX           +9223372036854775807
    #define     LLONG_MIN           -9223372036854775807
    #define     MB_LEN_MAX                             1
    #define     SCHAR_MAX                           +127
    #define     SCHAR_MIN                           -127
    #define     SHRT_MAX                          +32767
    #define     SHRT_MIN                          -32767
    #define     UCHAR_MAX                            255
    #define     USHRT_MAX                          65535
    #define     UINT_MAX                           65535
    #define     ULONG_MAX                     4294967295
    #define     ULLONG_MAX          18446744073709551615

.. _9899_Ep2:

.. container:: snum

   :ref:`2 <9899_Ep2>`

The contents of the header :ref:`\<float.h> <9899_7.7>` are given below. All integer values, except FLT_ROUNDS, shall be constant expressions suitable for use in `#if` preprocessing directives; all floating values shall be constant expressions. The components are described further in :ref:`5.2.4.2.2 <9899_5.2.4.2.2>`.

.. _9899_Ep3:

.. container:: snum

   :ref:`3 <9899_Ep3>`

The values given in the following list shall be replaced by implementation-defined expressions:

::

    #define FLT_EVAL_METHOD
    #define FLT_ROUNDS

.. _9899_Ep4:

.. container:: snum

   :ref:`4 <9899_Ep4>`

The values given in the following list shall be replaced by implementation-defined constant expressions that are greater or equal in magnitude (absolute value) to those shown, with the same sign:

::

    #define    DBL_DIG                                        10
    #define    DBL_MANT_DIG
    #define    DBL_MAX_10_EXP                               +37
    #define    DBL_MAX_EXP
    #define    DBL_MIN_10_EXP                               -37
    #define    DBL_MIN_EXP
    #define    DECIMAL_DIG                                    10
    #define    FLT_DIG                                         6
    #define    FLT_MANT_DIG
    #define    FLT_MAX_10_EXP                               +37
    #define    FLT_MAX_EXP
    #define    FLT_MIN_10_EXP                               -37
    #define    FLT_MIN_EXP
    #define    FLT_RADIX                                       2
    #define    LDBL_DIG                                       10
    #define    LDBL_MANT_DIG
    #define    LDBL_MAX_10_EXP                              +37
    #define    LDBL_MAX_EXP
    #define    LDBL_MIN_10_EXP                              -37
    #define    LDBL_MIN_EXP

.. _9899_Ep5:

.. container:: snum

   :ref:`5 <9899_Ep5>`

The values given in the following list shall be replaced by implementation-defined constant expressions with values that are greater than or equal to those shown:

::

    #define DBL_MAX                                      1E+37
    #define FLT_MAX                                      1E+37
    #define LDBL_MAX                                     1E+37

.. _9899_Ep6:

.. container:: snum

   :ref:`6 <9899_Ep6>`

The values given in the following list shall be replaced by implementation-defined constant expressions with (positive) values that are less than or equal to those shown:

::

    #define    DBL_EPSILON                                1E-9
    #define    DBL_MIN                                   1E-37
    #define    FLT_EPSILON                                1E-5
    #define    FLT_MIN                                   1E-37
    #define    LDBL_EPSILON                               1E-9
    #define    LDBL_MIN                                  1E-37

