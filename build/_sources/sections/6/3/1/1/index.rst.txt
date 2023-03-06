.. _9899_6.3.1.1:

6.3.1.1 Boolean, characters, and integers
'''''''''''''''''''''''''''''''''''''''''

.. _9899_6.3.1.1p1:

.. container:: snum

   :ref:`1 <9899_6.3.1.1p1>`

Every integer type has an integer conversion rank defined as follows:

-  No two signed integer types shall have the same rank, even if they have the same representation.
-  The rank of a signed integer type shall be greater than the rank of any signed integer type with less precision.
-  The rank of long long int shall be greater than the rank of long int, which shall be greater than the rank of int, which shall be greater than the rank of short int, which shall be greater than the rank of signed char.
-  The rank of any unsigned integer type shall equal the rank of the corresponding signed integer type, if any.
-  The rank of any standard integer type shall be greater than the rank of any extended integer type with the same width.
-  The rank of char shall equal the rank of signed char and unsigned char.
-  The rank of \_Bool shall be less than the rank of all other standard integer types.
-  The rank of any enumerated type shall equal the rank of the compatible integer type (see :ref:`6.7.2.2 <9899_6.7.2.2>`).
-  The rank of any extended signed integer type relative to another extended signed integer type with the same precision is implementation-defined, but still subject to the other rules for determining the integer conversion rank.
-  For all integer types T1, T2, and T3, if T1 has greater rank than T2 and T2 has greater rank than T3, then T1 has greater rank than T3.

.. _9899_6.3.1.1p2:

.. container:: snum

   :ref:`2 <9899_6.3.1.1p2>`

The following may be used in an expression wherever an int or unsigned int may be used:

-  An object or expression with an integer type whose integer conversion rank is less than or equal to the rank of int and unsigned int.
-  A bit-field of type \_Bool, int, signed int, or unsigned int.

If an int can represent all values of the original type, the value is converted to an int; otherwise, it is converted to an unsigned int. These are called the integer promotions.\ [#9899_note48]_ All other types are unchanged by the integer promotions.

.. _9899_6.3.1.1p3:

.. container:: snum

   :ref:`3 <9899_6.3.1.1p3>`

The integer promotions preserve value including sign. As discussed earlier, whether a "plain" char is treated as signed is implementation-defined.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.7.2.2`
   - :ref:`9899_6.7.2.1`





.. rubric:: Footnotes

.. [#9899_note48] The integer promotions are applied only: as part of the usual arithmetic conversions, to certain argument expressions, to the operands of the unary +, -, and ~ operators, and to both operands of the shift operators, as specified by their respective subclauses.
