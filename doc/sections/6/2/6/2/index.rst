.. _9899_6.2.6.2:

6.2.6.2 Integer types
'''''''''''''''''''''

.. _9899_6.2.6.2p1:

:ref:`1 <9899_6.2.6.2p1>` For unsigned integer types other than unsigned char, the bits of the object representation shall be divided into two groups: value bits and padding bits (there need not be any of the latter). If there are N value bits, each bit shall represent a different power of 2 between 1 and :math:`2\ :sup:`N-1` , so that objects of that type shall be capable of representing values from 0 to 2\ :sup:`N` - 1 using a pure binary representation; this shall be known as the value representation. The values of any padding bits are unspecified.\ `44) <note44>`

.. _9899_6.2.6.2p2:

:ref:`2 <9899_6.2.6.2p2>` For signed integer types, the bits of the object representation shall be divided into three groups: value bits, padding bits, and the sign bit. There need not be any padding bits; there shall be exactly one sign bit. Each bit that is a value bit shall have the same value as the same bit in the object representation of the corresponding unsigned type (if there are M value bits in the signed type and N in the unsigned type, then M <= N ). If the sign bit is zero, it shall not affect the resulting value. If the sign bit is one, the value shall be modified in one of the following ways:

-  the corresponding value with sign bit 0 is negated (sign and magnitude);
-  the sign bit has the value -(2\ :sup:`N` ) (two's complement);
-  the sign bit has the value -(2\ :sup:`N` - 1) (ones' complement ).

Which of these applies is implementation-defined, as is whether the value with sign bit 1 and all value bits zero (for the first two), or with sign bit and all value bits 1 (for ones' complement), is a trap representation or a normal value. In the case of sign and magnitude and ones' complement, if this representation is a normal value it is called a negative zero.

.. _9899_6.2.6.2p3:

:ref:`3 <9899_6.2.6.2p3>` If the implementation supports negative zeros, they shall be generated only by:

-  the &, \|, ^, ~, <<, and >> operators with arguments that produce such a value;
-  the +, -, \*, /, and % operators where one argument is a negative zero and the result is zero;
-  compound assignment operators based on the above cases.

It is unspecified whether these cases actually generate a negative zero or a normal zero, and whether a negative zero becomes a normal zero when stored in an object.

.. _9899_6.2.6.2p4:

:ref:`4 <9899_6.2.6.2p4>` If the implementation does not support negative zeros, the behavior of the &, \|, ^, ~, <<, and >> operators with arguments that would produce such a value is undefined.

.. _9899_6.2.6.2p5:

:ref:`5 <9899_6.2.6.2p5>` The values of any padding bits are unspecified.\ [#9899_note45]_ A valid (non-trap) object representation of a signed integer type where the sign bit is zero is a valid object representation of the corresponding unsigned type, and shall represent the same value. For any integer type, the object representation where all the bits are zero shall be a representation of the value zero in that type.

.. _9899_6.2.6.2p6:

:ref:`6 <9899_6.2.6.2p6>` The precision of an integer type is the number of bits it uses to represent values, excluding any sign and padding bits. The width of an integer type is the same but including any sign bit; thus for unsigned integer types the two values are the same, while for signed integer types the width is one greater than the precision.






.. rubric:: Footnotes

.. [#9899_note45] Some combinations of padding bits might generate trap representations, for example, if one padding bit is a parity bit. Regardless, no arithmetic operation on valid values can generate a trap representation other than as part of an exceptional condition such as an overflow. All other combinations of padding bits are alternative object representations of the value specified by the value bits.
