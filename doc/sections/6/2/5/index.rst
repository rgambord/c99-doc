.. _9899_6.2.5:

6.2.5 Types
^^^^^^^^^^^

.. _9899_6.2.5p1:

.. container:: snum

   :ref:`1 <9899_6.2.5p1>`

The meaning of a value stored in an object or returned by a function is determined by the type of the expression used to access it. (An identifier declared to be an object is the simplest such expression; the type is specified in the declaration of the identifier.) Types are partitioned into object types (types that fully describe objects), function types (types that describe functions), and incomplete types (types that describe objects but lack information needed to determine their sizes).

.. _9899_6.2.5p2:

.. container:: snum

   :ref:`2 <9899_6.2.5p2>`

An object declared as type \_Bool is large enough to store the values 0 and 1.

.. _9899_6.2.5p3:

.. container:: snum

   :ref:`3 <9899_6.2.5p3>`

An object declared as type char is large enough to store any member of the basic execution character set. If a member of the basic execution character set is stored in a char object, its value is guaranteed to be nonnegative. If any other character is stored in a char object, the resulting value is implementation-defined but shall be within the range of values that can be represented in that type.

.. _9899_6.2.5p4:

.. container:: snum

   :ref:`4 <9899_6.2.5p4>`

There are five standard signed integer types, designated as signed char, short int, int, long int, and long long int. (These and other types may be designated in several additional ways, as described in :ref:`6.7.2 <9899_6.7.2>`.) There may also be implementation-defined extended signed integer types.\ [#9899_note28]_ The standard and extended signed integer types are collectively called signed integer types.\ [#9899_note29]_

.. _9899_6.2.5p5:

.. container:: snum

   :ref:`5 <9899_6.2.5p5>`

An object declared as type signed char occupies the same amount of storage as a "plain" char object. A "plain" int object has the natural size suggested by the architecture of the execution environment (large enough to contain any value in the range INT_MIN to INT_MAX as defined in the header :ref:`\<limits.h> <9899_7.10>`).

.. _9899_6.2.5p6:

.. container:: snum

   :ref:`6 <9899_6.2.5p6>`

For each of the signed integer types, there is a corresponding (but different) unsigned integer type (designated with the keyword unsigned) that uses the same amount of storage (including sign information) and has the same alignment requirements. The type \_Bool and the unsigned integer types that correspond to the standard signed integer types are the standard unsigned integer types. The unsigned integer types that correspond to the extended signed integer types are the extended unsigned integer types. The standard and extended unsigned integer types are collectively called unsigned integer types.\ [#9899_note30]_

.. _9899_6.2.5p7:

.. container:: snum

   :ref:`7 <9899_6.2.5p7>`

The standard signed integer types and standard unsigned integer types are collectively called the standard integer types, the extended signed integer types and extended unsigned integer types are collectively called the extended integer types.

.. _9899_6.2.5p8:

.. container:: snum

   :ref:`8 <9899_6.2.5p8>`

For any two integer types with the same signedness and different integer conversion rank (see :ref:`6.3.1.1 <9899_6.3.1.1>`), the range of values of the type with smaller integer conversion rank is a subrange of the values of the other type.

.. _9899_6.2.5p9:

.. container:: snum

   :ref:`9 <9899_6.2.5p9>`

The range of nonnegative values of a signed integer type is a subrange of the corresponding unsigned integer type, and the representation of the same value in each type is the same.\ [#9899_note31]_ A computation involving unsigned operands can never overflow, because a result that cannot be represented by the resulting unsigned integer type is reduced modulo the number that is one greater than the largest value that can be represented by the resulting type.

.. _9899_6.2.5p10:

.. container:: snum

   :ref:`10 <9899_6.2.5p10>`

There are three real floating types, designated as float, double, and long double.\ [#9899_note32]_ The set of values of the type float is a subset of the set of values of the type double; the set of values of the type double is a subset of the set of values of the type long double.

.. _9899_6.2.5p11:

.. container:: snum

   :ref:`11 <9899_6.2.5p11>`

There are three complex types, designated as float \_Complex, double \_Complex, and long double \_Complex.\ [#9899_note33]_ The real floating and complex types are collectively called the floating types.

.. _9899_6.2.5p12:

.. container:: snum

   :ref:`12 <9899_6.2.5p12>`

For each floating type there is a corresponding real type, which is always a real floating type. For real floating types, it is the same type. For complex types, it is the type given by deleting the keyword \_Complex from the type name.

.. _9899_6.2.5p13:

.. container:: snum

   :ref:`13 <9899_6.2.5p13>`

Each complex type has the same representation and alignment requirements as an array type containing exactly two elements of the corresponding real type; the first element is equal to the real part, and the second element to the imaginary part, of the complex number.

.. _9899_6.2.5p14:

.. container:: snum

   :ref:`14 <9899_6.2.5p14>`

The type char, the signed and unsigned integer types, and the floating types are collectively called the basic types. Even if the implementation defines two or more basic types to have the same representation, they are nevertheless different types.\ [#9899_note34]_

.. _9899_6.2.5p15:

.. container:: snum

   :ref:`15 <9899_6.2.5p15>`

The three types char, signed char, and unsigned char are collectively called the character types. The implementation shall define char to have the same range, representation, and behavior as either signed char or unsigned char.\ [#9899_note35]_

.. _9899_6.2.5p16:

.. container:: snum

   :ref:`16 <9899_6.2.5p16>`

An enumeration comprises a set of named integer constant values. Each distinct enumeration constitutes a different enumerated type.

.. _9899_6.2.5p17:

.. container:: snum

   :ref:`17 <9899_6.2.5p17>`

The type char, the signed and unsigned integer types, and the enumerated types are collectively called integer types. The integer and real floating types are collectively called real types.

.. _9899_6.2.5p18:

.. container:: snum

   :ref:`18 <9899_6.2.5p18>`

Integer and floating types are collectively called arithmetic types. Each arithmetic type belongs to one type domain: the real type domain comprises the real types, the complex type domain comprises the complex types.

.. _9899_6.2.5p19:

.. container:: snum

   :ref:`19 <9899_6.2.5p19>`

The void type comprises an empty set of values; it is an incomplete type that cannot be completed.

.. _9899_6.2.5p20:

.. container:: snum

   :ref:`20 <9899_6.2.5p20>`

Any number of derived types can be constructed from the object, function, and incomplete types, as follows:

-  An array type describes a contiguously allocated nonempty set of objects with a particular member object type, called the element type.\ [#9899_note36]_ Array types are characterized by their element type and by the number of elements in the array. An array type is said to be derived from its element type, and if its element type is T , the array type is sometimes called "array of T ''. The construction of an array type from an element type is called "array type derivation".
-  A structure type describes a sequentially allocated nonempty set of member objects (and, in certain circumstances, an incomplete array), each of which has an optionally specified name and possibly distinct type.
-  A union type describes an overlapping nonempty set of member objects, each of which has an optionally specified name and possibly distinct type.
-  A function type describes a function with specified return type. A function type is characterized by its return type and the number and types of its parameters. A function type is said to be derived from its return type, and if its return type is T , the function type is sometimes called "function returning T ''. The construction of a function type from a return type is called "function type derivation".
-  A pointer type may be derived from a function type, an object type, or an incomplete type, called the referenced type. A pointer type describes an object whose value provides a reference to an entity of the referenced type. A pointer type derived from the referenced type T is sometimes called "pointer to T ''. The construction of a pointer type from a referenced type is called "pointer type derivation".

These methods of constructing derived types can be applied recursively.

.. _9899_6.2.5p21:

.. container:: snum

   :ref:`21 <9899_6.2.5p21>`

Arithmetic types and pointer types are collectively called scalar types. Array and structure types are collectively called aggregate types.\ [#9899_note37]_

.. _9899_6.2.5p22:

.. container:: snum

   :ref:`22 <9899_6.2.5p22>`

An array type of unknown size is an incomplete type. It is completed, for an identifier of that type, by specifying the size in a later declaration (with internal or external linkage). A structure or union type of unknown content (as described in :ref:`6.7.2.3 <9899_6.7.2.3>`) is an incomplete type. It is completed, for all declarations of that type, by declaring the same structure or union tag with its defining content later in the same scope.

.. _9899_6.2.5p23:

.. container:: snum

   :ref:`23 <9899_6.2.5p23>`

A type has known constant size if the type is not incomplete and is not a variable length array type.

.. _9899_6.2.5p24:

.. container:: snum

   :ref:`24 <9899_6.2.5p24>`

Array, function, and pointer types are collectively called derived declarator types. A declarator type derivation from a type T is the construction of a derived declarator type from T by the application of an array-type, a function-type, or a pointer-type derivation to T.

.. _9899_6.2.5p25:

.. container:: snum

   :ref:`25 <9899_6.2.5p25>`

A type is characterized by its type category, which is either the outermost derivation of a derived type (as noted above in the construction of derived types), or the type itself if the type consists of no derived types.

.. _9899_6.2.5p26:

.. container:: snum

   :ref:`26 <9899_6.2.5p26>`

Any type so far mentioned is an unqualified type. Each unqualified type has several qualified versions of its type,\ [#9899_note38]_ corresponding to the combinations of one, two, or all three of the const, volatile, and restrict qualifiers. The qualified or unqualified versions of a type are distinct types that belong to the same type category and have the same representation and alignment requirements.\ [#9899_note39]_ A derived type is not qualified by the qualifiers (if any) of the type from which it is derived.

.. _9899_6.2.5p27:

.. container:: snum

   :ref:`27 <9899_6.2.5p27>`

A pointer to void shall have the same representation and alignment requirements as a pointer to a character type.\ [#9899_note39]_ Similarly, pointers to qualified or unqualified versions of compatible types shall have the same representation and alignment requirements. All pointers to structure types shall have the same representation and alignment requirements as each other. All pointers to union types shall have the same representation and alignment requirements as each other. Pointers to other types need not have the same representation or alignment requirements.

.. _9899_6.2.5p28:

.. container:: snum

   :ref:`28 <9899_6.2.5p28>`

EXAMPLE 1 The type designated as "float \*'' has type "pointer to float". Its type category is pointer, not a floating type. The const-qualified version of this type is designated as "float \* const" whereas the type designated as "const float \*'' is not a qualified type -- its type is "pointer to const- qualified float" and is a pointer to a qualified type.

.. _9899_6.2.5p29:

.. container:: snum

   :ref:`29 <9899_6.2.5p29>`

EXAMPLE 2 The type designated as "struct tag (\*[5])(float)'' has type "array of pointer to function returning struct tag". The array has length five and the function has a single parameter of type float. Its type category is array.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.2.7`
   - :ref:`9899_6.7`
















.. rubric:: Footnotes

.. [#9899_note28] Implementation-defined keywords shall have the form of an identifier reserved for any use as described in :ref:`7.1.3 <9899_7.1.3>`.
.. [#9899_note29] Therefore, any statement in this Standard about signed integer types also applies to the extended signed integer types.
.. [#9899_note30] Therefore, any statement in this Standard about unsigned integer types also applies to the extended unsigned integer types.
.. [#9899_note31] The same representation and alignment requirements are meant to imply interchangeability as arguments to functions, return values from functions, and members of unions.
.. [#9899_note32] See "future language directions" (:ref:`6.11.1 <9899_6.11.1>`).
.. [#9899_note33] A specification for imaginary types is in informative :ref:`annex G <9899_G>`.
.. [#9899_note34] An implementation may define new keywords that provide alternative ways to designate a basic (or any other) type; this does not violate the requirement that all basic types be different. Implementation-defined keywords shall have the form of an identifier reserved for any use as described in :ref:`7.1.3 <9899_7.1.3>`.
.. [#9899_note35] CHAR_MIN, defined in :ref:`\<limits.h> <9899_7.10>`, will have one of the values 0 or SCHAR_MIN, and this can be used to distinguish the two options. Irrespective of the choice made, char is a separate type from the other two and is not compatible with either.
.. [#9899_note36] Since object types do not include incomplete types, an array of incomplete type cannot be constructed.
.. [#9899_note37] Note that aggregate type does not include union type because an object with union type can only contain one member at a time.
.. [#9899_note38] See :ref:`6.7.3 <9899_6.7.3>` regarding qualified array and function types.
.. [#9899_note39] The same representation and alignment requirements are meant to imply interchangeability as arguments to functions, return values from functions, and members of unions.
