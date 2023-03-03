.. _9899_6.7.2.1:

6.7.2.1 Structure and union specifiers
''''''''''''''''''''''''''''''''''''''

.. rubric:: Syntax

.. _9899_6.7.2.1p1:

:ref:`1 <9899_6.7.2.1p1>`

.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            struct-or-union-specifier
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            struct-or-union
     
   
         .. container:: syntax-nonterminal
   
            identifier
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            {
     
   
         .. container:: syntax-nonterminal
   
            struct-declaration-list
     
   
         .. container:: syntax-terminal
   
            }
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            struct-or-union
     
   
         .. container:: syntax-nonterminal
   
            identifier
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            struct-or-union
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            struct
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            union
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            struct-declaration-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            struct-declaration
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            struct-declaration-list
     
   
         .. container:: syntax-nonterminal
   
            struct-declaration
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            struct-declaration
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            specifier-qualifier-list
     
   
         .. container:: syntax-nonterminal
   
            struct-declarator-list
     
   
         .. container:: syntax-terminal
   
            ;
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            specifier-qualifier-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            type-specifier
     
   
         .. container:: syntax-nonterminal
   
            specifier-qualifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            type-qualifier
     
   
         .. container:: syntax-nonterminal
   
            specifier-qualifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            struct-declarator-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            struct-declarator
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            struct-declarator-list
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-nonterminal
   
            struct-declarator
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            struct-declarator
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            declarator
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            declarator
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            :
     
   
         .. container:: syntax-nonterminal
   
            constant-expression

.. rubric:: Constraints

.. _9899_6.7.2.1p2:

:ref:`2 <9899_6.7.2.1p2>` A structure or union shall not contain a member with incomplete or function type (hence, a structure shall not contain an instance of itself, but may contain a pointer to an instance of itself), except that the last member of a structure with more than one named member may have incomplete array type; such a structure (and any union containing, possibly recursively, a member that is such a structure) shall not be a member of a structure or an element of an array.

.. _9899_6.7.2.1p3:

:ref:`3 <9899_6.7.2.1p3>` The expression that specifies the width of a bit-field shall be an integer constant expression with a nonnegative value that does not exceed the width of an object of the type that would be specified were the colon and expression omitted. If the value is zero, the declaration shall have no declarator.

.. _9899_6.7.2.1p4:

:ref:`4 <9899_6.7.2.1p4>` A bit-field shall have a type that is a qualified or unqualified version of \_Bool, signed int, unsigned int, or some other implementation-defined type.

.. rubric:: Semantics

.. _9899_6.7.2.1p5:

:ref:`5 <9899_6.7.2.1p5>` As discussed in :ref:`6.2.5 <9899_6.2.5>`, a structure is a type consisting of a sequence of members, whose storage is allocated in an ordered sequence, and a union is a type consisting of a sequence of members whose storage overlap.

.. _9899_6.7.2.1p6:

:ref:`6 <9899_6.7.2.1p6>` Structure and union specifiers have the same form. The keywords struct and union indicate that the type being specified is, respectively, a structure type or a union type.

.. _9899_6.7.2.1p7:

:ref:`7 <9899_6.7.2.1p7>` The presence of a struct-declaration-list in a struct-or-union-specifier declares a new type, within a translation unit. The struct-declaration-list is a sequence of declarations for the members of the structure or union. If the struct-declaration-list contains no named members, the behavior is undefined. The type is incomplete until after the } that terminates the list.

.. _9899_6.7.2.1p8:

:ref:`8 <9899_6.7.2.1p8>` A member of a structure or union may have any object type other than a variably modified type.\ [#9899_note105]_ In addition, a member may be declared to consist of a specified number of bits (including a sign bit, if any). Such a member is called a bit-field;\ [#9899_note106]_ its width is preceded by a colon.

.. _9899_6.7.2.1p9:

:ref:`9 <9899_6.7.2.1p9>` A bit-field is interpreted as a signed or unsigned integer type consisting of the specified number of bits.\ [#9899_note107]_ If the value 0 or 1 is stored into a nonzero-width bit-field of type \_Bool, the value of the bit-field shall compare equal to the value stored.

.. _9899_6.7.2.1p10:

:ref:`10 <9899_6.7.2.1p10>` An implementation may allocate any addressable storage unit large enough to hold a bit- field. If enough space remains, a bit-field that immediately follows another bit-field in a structure shall be packed into adjacent bits of the same unit. If insufficient space remains, whether a bit-field that does not fit is put into the next unit or overlaps adjacent units is implementation-defined. The order of allocation of bit-fields within a unit (high-order to low-order or low-order to high-order) is implementation-defined. The alignment of the addressable storage unit is unspecified.

.. _9899_6.7.2.1p11:

:ref:`11 <9899_6.7.2.1p11>` A bit-field declaration with no declarator, but only a colon and a width, indicates an unnamed bit-field.\ [#9899_note108]_ As a special case, a bit-field structure member with a width of 0 indicates that no further bit-field is to be packed into the unit in which the previous bit- field, if any, was placed.

.. _9899_6.7.2.1p12:

:ref:`12 <9899_6.7.2.1p12>` Each non-bit-field member of a structure or union object is aligned in an implementation- defined manner appropriate to its type.

.. _9899_6.7.2.1p13:

:ref:`13 <9899_6.7.2.1p13>` Within a structure object, the non-bit-field members and the units in which bit-fields reside have addresses that increase in the order in which they are declared. A pointer to a structure object, suitably converted, points to its initial member (or if that member is a bit-field, then to the unit in which it resides), and vice versa. There may be unnamed padding within a structure object, but not at its beginning.

.. _9899_6.7.2.1p14:

:ref:`14 <9899_6.7.2.1p14>` The size of a union is sufficient to contain the largest of its members. The value of at most one of the members can be stored in a union object at any time. A pointer to a union object, suitably converted, points to each of its members (or if a member is a bit- field, then to the unit in which it resides), and vice versa.

.. _9899_6.7.2.1p15:

:ref:`15 <9899_6.7.2.1p15>` There may be unnamed padding at the end of a structure or union.

.. _9899_6.7.2.1p16:

:ref:`16 <9899_6.7.2.1p16>` As a special case, the last element of a structure with more than one named member may have an incomplete array type; this is called a flexible array member. In most situations, the flexible array member is ignored. In particular, the size of the structure is as if the flexible array member were omitted except that it may have more trailing padding than the omission would imply. However, when a . (or ->) operator has a left operand that is (a pointer to) a structure with a flexible array member and the right operand names that member, it behaves as if that member were replaced with the longest array (with the same element type) that would not make the structure larger than the object being accessed; the offset of the array shall remain that of the flexible array member, even if this would differ from that of the replacement array. If this array would have no elements, it behaves as if it had one element but the behavior is undefined if any attempt is made to access that element or to generate a pointer one past it.

.. _9899_6.7.2.1p17:

:ref:`17 <9899_6.7.2.1p17>` EXAMPLE After the declaration:

::

    struct s { int n; double d[]; };

the structure struct s has a flexible array member d. A typical way to use this is:

::

    int m = /* some value */;
    struct s *p = malloc(sizeof (struct s) + sizeof (double [m]));

and assuming that the call to malloc succeeds, the object pointed to by p behaves, for most purposes, as if p had been declared as:

::

    struct { int n; double d[m]; } *p;

(there are circumstances in which this equivalence is broken; in particular, the offsets of member d might not be the same).

.. _9899_6.7.2.1p18:

:ref:`18 <9899_6.7.2.1p18>` Following the above declaration:

::

    struct s t1 = { 0 };                        //   valid
    struct s t2 = { 1, { 4.2 }};                //   invalid
    t1.n = 4;                                   //   valid
    t1.d[0] = 4.2;                              //   might be undefined behavior

The initialization of t2 is invalid (and violates a constraint) because struct s is treated as if it did not contain member d. The assignment to t1.d[0] is probably undefined behavior, but it is possible that

::

    sizeof (struct s) >= offsetof(struct s, d) + sizeof (double)

in which case the assignment would be legitimate. Nevertheless, it cannot appear in strictly conforming code.

.. _9899_6.7.2.1p19:

:ref:`19 <9899_6.7.2.1p19>` After the further declaration:

::

    struct ss { int n; };

the expressions:

::

    sizeof (struct s) >= sizeof (struct ss)
    sizeof (struct s) >= offsetof(struct s, d)

are always equal to 1.

.. _9899_6.7.2.1p20:

:ref:`20 <9899_6.7.2.1p20>` If sizeof (double) is 8, then after the following code is executed:

::

    struct s *s1;
    struct s *s2;
    s1 = malloc(sizeof (struct s) + 64);
    s2 = malloc(sizeof (struct s) + 46);

and assuming that the calls to malloc succeed, the objects pointed to by s1 and s2 behave, for most purposes, as if the identifiers had been declared as:

::

    struct { int n; double d[8]; } *s1;
    struct { int n; double d[5]; } *s2;

.. _9899_6.7.2.1p21:

:ref:`21 <9899_6.7.2.1p21>` Following the further successful assignments:

::

    s1 = malloc(sizeof (struct s) + 10);
    s2 = malloc(sizeof (struct s) + 6);

they then behave as if the declarations were:

::

    struct { int n; double d[1]; } *s1, *s2;

and:

::

    double *dp;
    dp = &(s1->d[0]);           //   valid
    *dp = 42;                   //   valid
    dp = &(s2->d[0]);           //   valid
    *dp = 42;                   //   undefined behavior

.. _9899_6.7.2.1p22:

:ref:`22 <9899_6.7.2.1p22>` The assignment:

::

    *s1 = *s2;

only copies the member n; if any of the array elements are within the first sizeof (struct s) bytes of the structure, they might be copied or simply overwritten with indeterminate values.

**Forward references**: tags (:ref:`6.7.2.3 <9899_6.7.2.3>`).








.. rubric:: Footnotes

.. [#9899_note105] A structure or union can not contain a member with a variably modified type because member names are not ordinary identifiers as defined in :ref:`6.2.3 <9899_6.2.3>`.
.. [#9899_note106] The unary & (address-of) operator cannot be applied to a bit-field object; thus, there are no pointers to or arrays of bit-field objects.
.. [#9899_note107] As specified in :ref:`6.7.2 <9899_6.7.2>` above, if the actual type specifier used is int or a typedef-name defined as int, then it is implementation-defined whether the bit-field is signed or unsigned.
.. [#9899_note108] An unnamed bit-field structure member is useful for padding to conform to externally imposed layouts.
