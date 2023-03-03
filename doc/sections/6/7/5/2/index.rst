.. _9899_6.7.5.2:

6.7.5.2 Array declarators
'''''''''''''''''''''''''

.. rubric:: Constraints

.. _9899_6.7.5.2p1:

:ref:`1 <9899_6.7.5.2p1>` In addition to optional type qualifiers and the keyword static, the [ and ] may delimit an expression or \*. If they delimit an expression (which specifies the size of an array), the expression shall have an integer type. If the expression is a constant expression, it shall have a value greater than zero. The element type shall not be an incomplete or function type. The optional type qualifiers and the keyword static shall appear only in a declaration of a function parameter with an array type, and then only in the outermost array type derivation.

.. _9899_6.7.5.2p2:

:ref:`2 <9899_6.7.5.2p2>` An ordinary identifier (as defined in :ref:`6.2.3 <9899_6.2.3>`) that has a variably modified type shall have either block scope and no linkage or function prototype scope. If an identifier is declared to be an object with static storage duration, it shall not have a variable length array type.

.. rubric:: Semantics

.. _9899_6.7.5.2p3:

:ref:`3 <9899_6.7.5.2p3>` If, in the declaration ''T D1'', D1 has one of the forms:

.. code-block:: text

    D[ type-qualifier-listopt assignment-expressionopt ]
    D[ static type-qualifier-listopt assignment-expression ]
    D[ type-qualifier-list static assignment-expression ]
    D[ type-qualifier-listopt * ]

and the type specified for ident in the declaration ''T D'' is ''derived-declarator-type-list T '', then the type specified for ident is ''derived-declarator-type-list array of T ''.\ [#9899_note123]_ (See :ref:`6.7.5.3 <9899_6.7.5.3>` for the meaning of the optional type qualifiers and the keyword static.)

.. _9899_6.7.5.2p4:

:ref:`4 <9899_6.7.5.2p4>` If the size is not present, the array type is an incomplete type. If the size is \* instead of being an expression, the array type is a variable length array type of unspecified size, which can only be used in declarations with function prototype scope;\ [#9899_note124]_ such arrays are nonetheless complete types. If the size is an integer constant expression and the element type has a known constant size, the array type is not a variable length array type; otherwise, the array type is a variable length array type.

.. _9899_6.7.5.2p5:

:ref:`5 <9899_6.7.5.2p5>` If the size is an expression that is not an integer constant expression: if it occurs in a declaration at function prototype scope, it is treated as if it were replaced by \*; otherwise, each time it is evaluated it shall have a value greater than zero. The size of each instance of a variable length array type does not change during its lifetime. Where a size expression is part of the operand of a sizeof operator and changing the value of the size expression would not affect the result of the operator, it is unspecified whether or not the size expression is evaluated.

.. _9899_6.7.5.2p6:

:ref:`6 <9899_6.7.5.2p6>` For two array types to be compatible, both shall have compatible element types, and if both size specifiers are present, and are integer constant expressions, then both size specifiers shall have the same constant value. If the two array types are used in a context which requires them to be compatible, it is undefined behavior if the two size specifiers evaluate to unequal values.

.. _9899_6.7.5.2p7:

:ref:`7 <9899_6.7.5.2p7>` EXAMPLE 1

::

    float fa[11], *afp[17];

declares an array of float numbers and an array of pointers to float numbers.

.. _9899_6.7.5.2p8:

:ref:`8 <9899_6.7.5.2p8>` EXAMPLE 2 Note the distinction between the declarations

::

    extern int *x;
    extern int y[];

The first declares x to be a pointer to int; the second declares y to be an array of int of unspecified size (an incomplete type), the storage for which is defined elsewhere.

.. _9899_6.7.5.2p9:

:ref:`9 <9899_6.7.5.2p9>` EXAMPLE 3 The following declarations demonstrate the compatibility rules for variably modified types.

::

    extern int n;
    extern int m;
    void fcompat(void)
    {
          int a[n][6][m];
          int (*p)[4][n+1];
          int c[n][n][6][m];
          int (*r)[n][n][n+1];
          p = a;      // invalid: not compatible because 4 != 6
          r = c;      // compatible, but defined behavior only if
                      // n == 6 and m == n+1
    }

.. _9899_6.7.5.2p10:

:ref:`10 <9899_6.7.5.2p10>` EXAMPLE 4 All declarations of variably modified (VM) types have to be at either block scope or function prototype scope. Array objects declared with the static or extern storage-class specifier cannot have a variable length array (VLA) type. However, an object declared with the static storage- class specifier can have a VM type (that is, a pointer to a VLA type). Finally, all identifiers declared with a VM type have to be ordinary identifiers and cannot, therefore, be members of structures or unions.

::

    extern int n;
    int A[n];                                             // invalid: file scope VLA
    extern int (*p2)[n];                                  // invalid: file scope VM
    int B[100];                                           // valid: file scope but not VM
    void fvla(int m, int C[m][m]);                        // valid: VLA with prototype scope
    void fvla(int m, int C[m][m])                         // valid: adjusted to auto pointer to VLA
    {
          typedef int VLA[m][m];                          // valid: block scope typedef VLA
             struct tag {
                   int (*y)[n];                           // invalid: y not ordinary identifier
                   int z[n];                              // invalid: z not ordinary identifier
             };
             int D[m];                                    //   valid: auto VLA
             static int E[m];                             //   invalid: static block scope VLA
             extern int F[m];                             //   invalid: F has linkage and is VLA
             int (*s)[m];                                 //   valid: auto pointer to VLA
             extern int (*r)[m];                          //   invalid: r has linkage and points to VLA
             static int (*q)[m] = &B;                     //   valid: q is a static block pointer to VLA
    }

**Forward references**: function declarators (:ref:`6.7.5.3 <9899_6.7.5.3>`), function definitions (:ref:`6.9.1 <9899_6.9.1>`), initialization (:ref:`6.7.8 <9899_6.7.8>`).






.. rubric:: Footnotes

.. [#9899_note123] When several ''array of'' specifications are adjacent, a multidimensional array is declared.
.. [#9899_note124] Thus, \* can be used only in function declarations that are not definitions (see :ref:`6.7.5.3 <9899_6.7.5.3>`).
