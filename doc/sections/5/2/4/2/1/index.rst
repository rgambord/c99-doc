.. _9899_5.2.4.2.1:

5.2.4.2.1 Sizes of integer types \<limits.h>
""""""""""""""""""""""""""""""""""""""""""""

.. _9899_5.2.4.2.1p1:

.. container:: snum

   :ref:`1 <9899_5.2.4.2.1p1>`

The values given below shall be replaced by constant expressions suitable for use in `#if` preprocessing directives. Moreover, except for CHAR_BIT and MB_LEN_MAX, the following shall be replaced by expressions that have the same type as would an expression that is an object of the corresponding type converted according to the integer promotions. Their implementation-defined values shall be equal or greater in magnitude (absolute value) to those shown, with the same sign.

-  number of bits for smallest object that is not a bit-field (byte)

::

    CHAR_BIT                                            8

-  minimum value for an object of type signed char

::

    SCHAR_MIN                                -127 // -(27 - 1)

-  maximum value for an object of type signed char

::

    SCHAR_MAX                                +127 // 27 - 1

-  maximum value for an object of type unsigned char

::

    UCHAR_MAX                                 255 // 28 - 1

-  minimum value for an object of type char

::

    CHAR_MIN                               see below

-  maximum value for an object of type char

::

    CHAR_MAX                              see below

-  maximum number of bytes in a multibyte character, for any supported locale

::

    MB_LEN_MAX                                    1

-  minimum value for an object of type short int

::

    SHRT_MIN                               -32767 // -(215 - 1)

-  maximum value for an object of type short int

::

    SHRT_MAX                               +32767 // 215 - 1

-  maximum value for an object of type unsigned short int

::

    USHRT_MAX                               65535 // 216 - 1

-  minimum value for an object of type int

::

    INT_MIN                                 -32767 // -(215 - 1)

-  maximum value for an object of type int

::

    INT_MAX                                +32767 // 215 - 1

-  maximum value for an object of type unsigned int

::

    UINT_MAX                                65535 // 216 - 1

-  minimum value for an object of type long int

::

    LONG_MIN                         -2147483647 // -(231 - 1)

-  maximum value for an object of type long int

::

    LONG_MAX                         +2147483647 // 231 - 1

-  maximum value for an object of type unsigned long int

::

    ULONG_MAX                         4294967295 // 232 - 1

-  minimum value for an object of type long long int

::

    LLONG_MIN          -9223372036854775807 // -(263 - 1)

-  maximum value for an object of type long long int

::

    LLONG_MAX          +9223372036854775807 // 263 - 1

-  maximum value for an object of type unsigned long long int

::

    ULLONG_MAX         18446744073709551615 // 264 - 1

.. _9899_5.2.4.2.1p2:

.. container:: snum

   :ref:`2 <9899_5.2.4.2.1p2>`

If the value of an object of type char is treated as a signed integer when used in an expression, the value of CHAR_MIN shall be the same as that of SCHAR_MIN and the value of CHAR_MAX shall be the same as that of SCHAR_MAX. Otherwise, the value of CHAR_MIN shall be 0 and the value of CHAR_MAX shall be the same as that of UCHAR_MAX.\ [#9899_note15]_ The value UCHAR_MAX shall equal 2\ :sup:`CHAR_BIT` - 1.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.2.6`
   - :ref:`9899_6.10.1`





.. rubric:: Footnotes

.. [#9899_note15] See :ref:`6.2.5 <9899_6.2.5>`.
