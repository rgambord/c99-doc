.. _9899_6.2.7:

6.2.7 Compatible type and composite type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_6.2.7p1:

.. container:: snum

   :ref:`1 <9899_6.2.7p1>`

Two types have compatible type if their types are the same. Additional rules for determining whether two types are compatible are described in :ref:`6.7.2 <9899_6.7.2>` for type specifiers, in :ref:`6.7.3 <9899_6.7.3>` for type qualifiers, and in :ref:`6.7.5 <9899_6.7.5>` for declarators.\ [#9899_note46]_ Moreover, two structure, union, or enumerated types declared in separate translation units are compatible if their tags and members satisfy the following requirements: If one is declared with a tag, the other shall be declared with the same tag. If both are complete types, then the following additional requirements apply: there shall be a one-to-one correspondence between their members such that each pair of corresponding members are declared with compatible types, and such that if one member of a corresponding pair is declared with a name, the other member is declared with the same name. For two structures, corresponding members shall be declared in the same order. For two structures or unions, corresponding bit-fields shall have the same widths. For two enumerations, corresponding members shall have the same values.

.. _9899_6.2.7p2:

.. container:: snum

   :ref:`2 <9899_6.2.7p2>`

All declarations that refer to the same object or function shall have compatible type; otherwise, the behavior is undefined.

.. _9899_6.2.7p3:

.. container:: snum

   :ref:`3 <9899_6.2.7p3>`

A composite type can be constructed from two types that are compatible; it is a type that is compatible with both of the two types and satisfies the following conditions:

-  If one type is an array of known constant size, the composite type is an array of that size; otherwise, if one type is a variable length array, the composite type is that type.
-  If only one type is a function type with a parameter type list (a function prototype), the composite type is a function prototype with the parameter type list.
-  If both types are function types with parameter type lists, the type of each parameter in the composite parameter type list is the composite type of the corresponding parameters.

These rules apply recursively to the types from which the two types are derived.

.. _9899_6.2.7p4:

.. container:: snum

   :ref:`4 <9899_6.2.7p4>`

For an identifier with internal or external linkage declared in a scope in which a prior declaration of that identifier is visible,\ [#9899_note47]_ if the prior declaration specifies internal or external linkage, the type of the identifier at the later declaration becomes the composite type.

.. _9899_6.2.7p5:

.. container:: snum

   :ref:`5 <9899_6.2.7p5>`

EXAMPLE Given the following two file scope declarations:

::

    int f(int (*)(), double (*)[3]);
    int f(int (*)(char *), double (*)[]);

The resulting composite type for the function is:

::

    int f(int (*)(char *), double (*)[3]);






.. rubric:: Footnotes

.. [#9899_note46] Two types need not be identical to be compatible.
.. [#9899_note47] As specified in :ref:`6.2.1 <9899_6.2.1>`, the later declaration might hide the prior declaration.
