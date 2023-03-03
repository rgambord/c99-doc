.. _9899_6.7.7:

6.7.7 Type definitions
^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.7.7p1:

:ref:`1 <9899_6.7.7p1>`

.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            typedef-name
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            identifier

.. rubric:: Constraints

.. _9899_6.7.7p2:

:ref:`2 <9899_6.7.7p2>` If a typedef name specifies a variably modified type then it shall have block scope.

.. rubric:: Semantics

.. _9899_6.7.7p3:

:ref:`3 <9899_6.7.7p3>` In a declaration whose storage-class specifier is typedef, each declarator defines an identifier to be a typedef name that denotes the type specified for the identifier in the way described in :ref:`6.7.5 <9899_6.7.5>`. Any array size expressions associated with variable length array declarators are evaluated each time the declaration of the typedef name is reached in the order of execution. A typedef declaration does not introduce a new type, only a synonym for the type so specified. That is, in the following declarations:

::

    typedef T type_ident;
    type_ident D;

type_ident is defined as a typedef name with the type specified by the declaration specifiers in T (known as T ), and the identifier in D has the type ''derived-declarator- type-list T '' where the derived-declarator-type-list is specified by the declarators of D. A typedef name shares the same name space as other identifiers declared in ordinary declarators.

.. _9899_6.7.7p4:

:ref:`4 <9899_6.7.7p4>` EXAMPLE 1 After

::

    typedef int MILES, KLICKSP();
    typedef struct { double hi, lo; } range;

the constructions

::

    MILES distance;
    extern KLICKSP *metricp;
    range x;
    range z, *zp;

are all valid declarations. The type of distance is int, that of metricp is ''pointer to function with no parameter specification returning int'', and that of x and z is the specified structure; zp is a pointer to such a structure. The object distance has a type compatible with any other int object.

.. _9899_6.7.7p5:

:ref:`5 <9899_6.7.7p5>` EXAMPLE 2 After the declarations

::

    typedef struct s1 { int x; } t1, *tp1;
    typedef struct s2 { int x; } t2, *tp2;

type t1 and the type pointed to by tp1 are compatible. Type t1 is also compatible with type struct s1, but not compatible with the types struct s2, t2, the type pointed to by tp2, or int.

.. _9899_6.7.7p6:

:ref:`6 <9899_6.7.7p6>` EXAMPLE 3 The following obscure constructions

::

    typedef signed int t;
    typedef int plain;
    struct tag {
          unsigned t:4;
          const t:5;
          plain r:5;
    };

declare a typedef name t with type signed int, a typedef name plain with type int, and a structure with three bit-field members, one named t that contains values in the range [0, 15], an unnamed const- qualified bit-field which (if it could be accessed) would contain values in either the range [-15, +15] or [-16, +15], and one named r that contains values in one of the ranges [0, 31], [-15, +15], or [-16, +15]. (The choice of range is implementation-defined.) The first two bit-field declarations differ in that unsigned is a type specifier (which forces t to be the name of a structure member), while const is a type qualifier (which modifies t which is still visible as a typedef name). If these declarations are followed in an inner scope by

::

    t f(t (t));
    long t;

then a function f is declared with type ''function returning signed int with one unnamed parameter with type pointer to function returning signed int with one unnamed parameter with type signed int'', and an identifier t with type long int.

.. _9899_6.7.7p7:

:ref:`7 <9899_6.7.7p7>` EXAMPLE 4 On the other hand, typedef names can be used to improve code readability. All three of the following declarations of the signal function specify exactly the same type, the first without making use of any typedef names.

::

    typedef void fv(int), (*pfv)(int);
    void (*signal(int, void (*)(int)))(int);
    fv *signal(int, fv *);
    pfv signal(int, pfv);

.. _9899_6.7.7p8:

:ref:`8 <9899_6.7.7p8>` EXAMPLE 5 If a typedef name denotes a variable length array type, the length of the array is fixed at the time the typedef name is defined, not each time it is used:

::

    void copyt(int n)
    {
          typedef int B[n];    //               B is n ints, n evaluated now
          n += 1;
          B a;                //                a is n ints, n without += 1
          int b[n];           //                a and b are different sizes
          for (int i = 1; i < n;                i++)
                a[i-1] = b[i];
    }

