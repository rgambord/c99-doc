.. _9899_6.7.8:

6.7.8 Initialization
^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.7.8p1:

:ref:`1 <9899_6.7.8p1>`

.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            initializer
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            assignment-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            {
     
   
         .. container:: syntax-nonterminal
   
            initializer-list
     
   
         .. container:: syntax-terminal
   
            }
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            {
     
   
         .. container:: syntax-nonterminal
   
            initializer-list
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-terminal
   
            }
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            initializer-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            designation
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            initializer
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            initializer-list
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-nonterminal
   
            designation
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            initializer
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            designation
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            designator-list
     
   
         .. container:: syntax-terminal
   
            =
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            designator-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            designator
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            designator-list
     
   
         .. container:: syntax-nonterminal
   
            designator
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            designator
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            [
     
   
         .. container:: syntax-nonterminal
   
            constant-expression
     
   
         .. container:: syntax-terminal
   
            ]
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            .
     
   
         .. container:: syntax-nonterminal
   
            identifier

.. rubric:: Constraints

.. _9899_6.7.8p2:

:ref:`2 <9899_6.7.8p2>` No initializer shall attempt to provide a value for an object not contained within the entity being initialized.

.. _9899_6.7.8p3:

:ref:`3 <9899_6.7.8p3>` The type of the entity to be initialized shall be an array of unknown size or an object type that is not a variable length array type.

.. _9899_6.7.8p4:

:ref:`4 <9899_6.7.8p4>` All the expressions in an initializer for an object that has static storage duration shall be constant expressions or string literals.

.. _9899_6.7.8p5:

:ref:`5 <9899_6.7.8p5>` If the declaration of an identifier has block scope, and the identifier has external or internal linkage, the declaration shall have no initializer for the identifier.

.. _9899_6.7.8p6:

:ref:`6 <9899_6.7.8p6>` If a designator has the form

.. code-block:: text

    [ constant-expression ]

then the current object (defined below) shall have array type and the expression shall be an integer constant expression. If the array is of unknown size, any nonnegative value is valid.

.. _9899_6.7.8p7:

:ref:`7 <9899_6.7.8p7>` If a designator has the form

.. code-block:: text

    . identifier

then the current object (defined below) shall have structure or union type and the identifier shall be the name of a member of that type.

.. rubric:: Semantics

.. _9899_6.7.8p8:

:ref:`8 <9899_6.7.8p8>` An initializer specifies the initial value stored in an object.

.. _9899_6.7.8p9:

:ref:`9 <9899_6.7.8p9>` Except where explicitly stated otherwise, for the purposes of this subclause unnamed members of objects of structure and union type do not participate in initialization. Unnamed members of structure objects have indeterminate value even after initialization.

.. _9899_6.7.8p10:

:ref:`10 <9899_6.7.8p10>` If an object that has automatic storage duration is not initialized explicitly, its value is indeterminate. If an object that has static storage duration is not initialized explicitly, then:

-  if it has pointer type, it is initialized to a null pointer;
-  if it has arithmetic type, it is initialized to (positive or unsigned) zero;
-  if it is an aggregate, every member is initialized (recursively) according to these rules;
-  if it is a union, the first named member is initialized (recursively) according to these rules.

.. _9899_6.7.8p11:

:ref:`11 <9899_6.7.8p11>` The initializer for a scalar shall be a single expression, optionally enclosed in braces. The initial value of the object is that of the expression (after conversion); the same type constraints and conversions as for simple assignment apply, taking the type of the scalar to be the unqualified version of its declared type.

.. _9899_6.7.8p12:

:ref:`12 <9899_6.7.8p12>` The rest of this subclause deals with initializers for objects that have aggregate or union type.

.. _9899_6.7.8p13:

:ref:`13 <9899_6.7.8p13>` The initializer for a structure or union object that has automatic storage duration shall be either an initializer list as described below, or a single expression that has compatible structure or union type. In the latter case, the initial value of the object, including unnamed members, is that of the expression.

.. _9899_6.7.8p14:

:ref:`14 <9899_6.7.8p14>` An array of character type may be initialized by a character string literal, optionally enclosed in braces. Successive characters of the character string literal (including the terminating null character if there is room or if the array is of unknown size) initialize the elements of the array.

.. _9899_6.7.8p15:

:ref:`15 <9899_6.7.8p15>` An array with element type compatible with wchar_t may be initialized by a wide string literal, optionally enclosed in braces. Successive wide characters of the wide string literal (including the terminating null wide character if there is room or if the array is of unknown size) initialize the elements of the array.

.. _9899_6.7.8p16:

:ref:`16 <9899_6.7.8p16>` Otherwise, the initializer for an object that has aggregate or union type shall be a brace- enclosed list of initializers for the elements or named members.

.. _9899_6.7.8p17:

:ref:`17 <9899_6.7.8p17>` Each brace-enclosed initializer list has an associated current object. When no designations are present, subobjects of the current object are initialized in order according to the type of the current object: array elements in increasing subscript order, structure members in declaration order, and the first named member of a union.\ [#9899_note129]_ In contrast, a designation causes the following initializer to begin initialization of the subobject described by the designator. Initialization then continues forward in order, beginning with the next subobject after that described by the designator.\ [#9899_note130]_

.. _9899_6.7.8p18:

:ref:`18 <9899_6.7.8p18>` Each designator list begins its description with the current object associated with the closest surrounding brace pair. Each item in the designator list (in order) specifies a particular member of its current object and changes the current object for the next designator (if any) to be that member.\ [#9899_note131]_ The current object that results at the end of the designator list is the subobject to be initialized by the following initializer.

.. _9899_6.7.8p19:

:ref:`19 <9899_6.7.8p19>` The initialization shall occur in initializer list order, each initializer provided for a particular subobject overriding any previously listed initializer for the same subobject;\ [#9899_note132]_ all subobjects that are not initialized explicitly shall be initialized implicitly the same as objects that have static storage duration.

.. _9899_6.7.8p20:

:ref:`20 <9899_6.7.8p20>` If the aggregate or union contains elements or members that are aggregates or unions, these rules apply recursively to the subaggregates or contained unions. If the initializer of a subaggregate or contained union begins with a left brace, the initializers enclosed by that brace and its matching right brace initialize the elements or members of the subaggregate or the contained union. Otherwise, only enough initializers from the list are taken to account for the elements or members of the subaggregate or the first member of the contained union; any remaining initializers are left to initialize the next element or member of the aggregate of which the current subaggregate or contained union is a part.

.. _9899_6.7.8p21:

:ref:`21 <9899_6.7.8p21>` If there are fewer initializers in a brace-enclosed list than there are elements or members of an aggregate, or fewer characters in a string literal used to initialize an array of known size than there are elements in the array, the remainder of the aggregate shall be initialized implicitly the same as objects that have static storage duration.

.. _9899_6.7.8p22:

:ref:`22 <9899_6.7.8p22>` If an array of unknown size is initialized, its size is determined by the largest indexed element with an explicit initializer. At the end of its initializer list, the array no longer has incomplete type.

.. _9899_6.7.8p23:

:ref:`23 <9899_6.7.8p23>` The order in which any side effects occur among the initialization list expressions is unspecified.\ [#9899_note133]_

.. _9899_6.7.8p24:

:ref:`24 <9899_6.7.8p24>` EXAMPLE 1 Provided that :ref:`\<complex.h> <9899_7.3>` has been #included, the declarations

::

    int i = 3.5;
    double complex c = 5 + 3 * I;

define and initialize i with the value 3 and c with the value 5.0 + i3.0.

.. _9899_6.7.8p25:

:ref:`25 <9899_6.7.8p25>` EXAMPLE 2 The declaration

::

    int x[] = { 1, 3, 5 };

defines and initializes x as a one-dimensional array object that has three elements, as no size was specified and there are three initializers.

.. _9899_6.7.8p26:

:ref:`26 <9899_6.7.8p26>` EXAMPLE 3 The declaration

::

    int y[4][3] =         {
          { 1, 3,         5 },
          { 2, 4,         6 },
          { 3, 5,         7 },
    };

is a definition with a fully bracketed initialization: 1, 3, and 5 initialize the first row of y (the array object y[0]), namely y[0][0], y[0][1], and y[0][2]. Likewise the next two lines initialize y[1] and y[2]. The initializer ends early, so y[3] is initialized with zeros. Precisely the same effect could have been achieved by

::

    int y[4][3] = {
          1, 3, 5, 2, 4, 6, 3, 5, 7
    };

The initializer for y[0] does not begin with a left brace, so three items from the list are used. Likewise the next three are taken successively for y[1] and y[2].

.. _9899_6.7.8p27:

:ref:`27 <9899_6.7.8p27>` EXAMPLE 4 The declaration

::

    int z[4][3] = {
          { 1 }, { 2 }, { 3 }, { 4 }
    };

initializes the first column of z as specified and initializes the rest with zeros.

.. _9899_6.7.8p28:

:ref:`28 <9899_6.7.8p28>` EXAMPLE 5 The declaration

::

    struct { int a[3], b; } w[] = { { 1 }, 2 };

is a definition with an inconsistently bracketed initialization. It defines an array with two element structures: w[0].a[0] is 1 and w[1].a[0] is 2; all the other elements are zero.

.. _9899_6.7.8p29:

:ref:`29 <9899_6.7.8p29>` EXAMPLE 6 The declaration

::

    short q[4][3][2] = {
          { 1 },
          { 2, 3 },
          { 4, 5, 6 }
    };

contains an incompletely but consistently bracketed initialization. It defines a three-dimensional array object: q[0][0][0] is 1, q[1][0][0] is 2, q[1][0][1] is 3, and 4, 5, and 6 initialize q[2][0][0], q[2][0][1], and q[2][1][0], respectively; all the rest are zero. The initializer for q[0][0] does not begin with a left brace, so up to six items from the current list may be used. There is only one, so the values for the remaining five elements are initialized with zero. Likewise, the initializers for q[1][0] and q[2][0] do not begin with a left brace, so each uses up to six items, initializing their respective two-dimensional subaggregates. If there had been more than six items in any of the lists, a diagnostic message would have been issued. The same initialization result could have been achieved by:

::

    short q[4][3][2] = {
          1, 0, 0, 0, 0, 0,
          2, 3, 0, 0, 0, 0,
          4, 5, 6
    };

or by:

::

    short q[4][3][2] = {
          {
                { 1 },
          },
          {
                { 2, 3 },
          },
          {
                { 4, 5 },
                { 6 },
          }
    };

in a fully bracketed form.

.. _9899_6.7.8p30:

:ref:`30 <9899_6.7.8p30>` Note that the fully bracketed and minimally bracketed forms of initialization are, in general, less likely to cause confusion.

.. _9899_6.7.8p31:

:ref:`31 <9899_6.7.8p31>` EXAMPLE 7 One form of initialization that completes array types involves typedef names. Given the declaration

::

    typedef int A[];          // OK - declared with block scope

the declaration

::

    A a = { 1, 2 }, b = { 3, 4, 5 };

is identical to

::

    int a[] = { 1, 2 }, b[] = { 3, 4, 5 };

due to the rules for incomplete types.

.. _9899_6.7.8p32:

:ref:`32 <9899_6.7.8p32>` EXAMPLE 8 The declaration

::

    char s[] = "abc", t[3] = "abc";

defines ''plain'' char array objects s and t whose elements are initialized with character string literals. This declaration is identical to

::

    char s[] = { 'a', 'b', 'c', '\0' },
         t[] = { 'a', 'b', 'c' };

The contents of the arrays are modifiable. On the other hand, the declaration

::

    char *p = "abc";

defines p with type ''pointer to char'' and initializes it to point to an object with type ''array of char'' with length 4 whose elements are initialized with a character string literal. If an attempt is made to use p to modify the contents of the array, the behavior is undefined.

.. _9899_6.7.8p33:

:ref:`33 <9899_6.7.8p33>` EXAMPLE 9 Arrays can be initialized to correspond to the elements of an enumeration by using designators:

::

    enum { member_one,           member_two };
    const char *nm[] =           {
          [member_two]           = "member two",
          [member_one]           = "member one",
    };

.. _9899_6.7.8p34:

:ref:`34 <9899_6.7.8p34>` EXAMPLE 10 Structure members can be initialized to nonzero values without depending on their order:

::

    div_t answer = { .quot = 2, .rem = -1 };

.. _9899_6.7.8p35:

:ref:`35 <9899_6.7.8p35>` EXAMPLE 11 Designators can be used to provide explicit initialization when unadorned initializer lists might be misunderstood:

::

    struct { int a[3], b; } w[] =
          { [0].a = {1}, [1].a[0] = 2 };

.. _9899_6.7.8p36:

:ref:`36 <9899_6.7.8p36>` EXAMPLE 12 Space can be ''allocated'' from both ends of an array by using a single designator:

::

    int a[MAX] = {
          1, 3, 5, 7, 9, [MAX-5] = 8, 6, 4, 2, 0
    };

.. _9899_6.7.8p37:

:ref:`37 <9899_6.7.8p37>` In the above, if MAX is greater than ten, there will be some zero-valued elements in the middle; if it is less than ten, some of the values provided by the first five initializers will be overridden by the second five.

.. _9899_6.7.8p38:

:ref:`38 <9899_6.7.8p38>` EXAMPLE 13 Any member of a union can be initialized:

::

    union { /* ... */ } u = { .any_member = 42 };

**Forward references**: common definitions :ref:`\<stddef.h> <9899_7.17>` (:ref:`7.17 <9899_7.17>`).









.. rubric:: Footnotes

.. [#9899_note129] If the initializer list for a subaggregate or contained union does not begin with a left brace, its subobjects are initialized as usual, but the subaggregate or contained union does not become the current object: current objects are associated only with brace-enclosed initializer lists.
.. [#9899_note130] After a union member is initialized, the next object is not the next member of the union; instead, it is the next subobject of an object containing the union.
.. [#9899_note131] Thus, a designator can only specify a strict subobject of the aggregate or union that is associated with the surrounding brace pair. Note, too, that each separate designator list is independent.
.. [#9899_note132] Any initializer for the subobject which is overridden and so not used to initialize that subobject might not be evaluated at all.
.. [#9899_note133] In particular, the evaluation order need not be the same as the order of subobject initialization.
