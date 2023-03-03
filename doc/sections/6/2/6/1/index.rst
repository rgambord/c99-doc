.. _9899_6.2.6.1:

6.2.6.1 General
'''''''''''''''

.. _9899_6.2.6.1p1:

:ref:`1 <9899_6.2.6.1p1>` The representations of all types are unspecified except as stated in this subclause.

.. _9899_6.2.6.1p2:

:ref:`2 <9899_6.2.6.1p2>` Except for bit-fields, objects are composed of contiguous sequences of one or more bytes, the number, order, and encoding of which are either explicitly specified or implementation-defined.

.. _9899_6.2.6.1p3:

:ref:`3 <9899_6.2.6.1p3>` Values stored in unsigned bit-fields and objects of type unsigned char shall be represented using a pure binary notation.\ [#9899_note40]_

.. _9899_6.2.6.1p4:

:ref:`4 <9899_6.2.6.1p4>` Values stored in non-bit-field objects of any other object type consist of n x CHAR_BIT bits, where n is the size of an object of that type, in bytes. The value may be copied into an object of type unsigned char [n] (e.g., by memcpy); the resulting set of bytes is called the object representation of the value. Values stored in bit-fields consist of m bits, where m is the size specified for the bit-field. The object representation is the set of m bits the bit-field comprises in the addressable storage unit holding it. Two values (other than NaNs) with the same object representation compare equal, but values that compare equal may have different object representations.

.. _9899_6.2.6.1p5:

:ref:`5 <9899_6.2.6.1p5>` Certain object representations need not represent a value of the object type. If the stored value of an object has such a representation and is read by an lvalue expression that does not have character type, the behavior is undefined. If such a representation is produced by a side effect that modifies all or any part of the object by an lvalue expression that does not have character type, the behavior is undefined.\ [#9899_note41]_ Such a representation is called a trap representation.

.. _9899_6.2.6.1p6:

:ref:`6 <9899_6.2.6.1p6>` When a value is stored in an object of structure or union type, including in a member object, the bytes of the object representation that correspond to any padding bytes take unspecified values.\ [#9899_note42]_ The value of a structure or union object is never a trap representation, even though the value of a member of the structure or union object may be a trap representation.

.. _9899_6.2.6.1p7:

:ref:`7 <9899_6.2.6.1p7>` When a value is stored in a member of an object of union type, the bytes of the object representation that do not correspond to that member but do correspond to other members take unspecified values.

.. _9899_6.2.6.1p8:

:ref:`8 <9899_6.2.6.1p8>` Where an operator is applied to a value that has more than one object representation, which object representation is used shall not affect the value of the result.\ [#9899_note43]_ Where a value is stored in an object using a type that has more than one object representation for that value, it is unspecified which representation is used, but a trap representation shall not be generated.

**Forward references**: declarations (:ref:`6.7 <9899_6.7>`), expressions (:ref:`6.5 <9899_6.5>`), lvalues, arrays, and function designators (:ref:`6.3.2.1 <9899_6.3.2.1>`).








.. rubric:: Footnotes

.. [#9899_note40] A positional representation for integers that uses the binary digits 0 and 1, in which the values represented by successive bits are additive, begin with 1, and are multiplied by successive integral powers of 2, except perhaps the bit with the highest position. (Adapted from the American National Dictionary for Information Processing Systems.) A byte contains CHAR_BIT bits, and the values of type unsigned char range from 0 to 2\ :sup:`CHAR_BIT`- 1.
.. [#9899_note41] Thus, an automatic variable can be initialized to a trap representation without causing undefined behavior, but the value of the variable cannot be used until a proper value is stored in it.
.. [#9899_note42] Thus, for example, structure assignment need not copy any padding bits.
.. [#9899_note43] It is possible for objects x and y with the same effective type T to have the same value when they are accessed as objects of type T, but to have different values in other contexts. In particular, if == is defined for type T, then x == y does not imply that memcmp(&x, &y, sizeof (T)) == 0. Furthermore, x == y does not necessarily imply that x and y have the same value; other operations on values of type T may distinguish between them.
