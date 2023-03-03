.. _9899_6.7.5.3:

6.7.5.3 Function declarators (including prototypes)
'''''''''''''''''''''''''''''''''''''''''''''''''''

.. rubric:: Constraints

.. _9899_6.7.5.3p1:

:ref:`1 <9899_6.7.5.3p1>` A function declarator shall not specify a return type that is a function type or an array type.

.. _9899_6.7.5.3p2:

:ref:`2 <9899_6.7.5.3p2>` The only storage-class specifier that shall occur in a parameter declaration is register.

.. _9899_6.7.5.3p3:

:ref:`3 <9899_6.7.5.3p3>` An identifier list in a function declarator that is not part of a definition of that function shall be empty.

.. _9899_6.7.5.3p4:

:ref:`4 <9899_6.7.5.3p4>` After adjustment, the parameters in a parameter type list in a function declarator that is part of a definition of that function shall not have incomplete type.

.. rubric:: Semantics

.. _9899_6.7.5.3p5:

:ref:`5 <9899_6.7.5.3p5>` If, in the declaration ''T D1'', D1 has the form

.. code-block:: text

    D( parameter-type-list )

or

.. code-block:: text

    D( identifier-listopt )

and the type specified for ident in the declaration ''T D'' is ''derived-declarator-type-list T '', then the type specified for ident is ''derived-declarator-type-list function returning T ''.

.. _9899_6.7.5.3p6:

:ref:`6 <9899_6.7.5.3p6>` A parameter type list specifies the types of, and may declare identifiers for, the parameters of the function.

.. _9899_6.7.5.3p7:

:ref:`7 <9899_6.7.5.3p7>` A declaration of a parameter as ''array of type'' shall be adjusted to ''qualified pointer to type'', where the type qualifiers (if any) are those specified within the [ and ] of the array type derivation. If the keyword static also appears within the [ and ] of the array type derivation, then for each call to the function, the value of the corresponding actual argument shall provide access to the first element of an array with at least as many elements as specified by the size expression.

.. _9899_6.7.5.3p8:

:ref:`8 <9899_6.7.5.3p8>` A declaration of a parameter as ''function returning type'' shall be adjusted to ''pointer to function returning type'', as in :ref:`6.3.2.1 <9899_6.3.2.1>`.

.. _9899_6.7.5.3p9:

:ref:`9 <9899_6.7.5.3p9>` If the list terminates with an ellipsis (, \.\.\.), no information about the number or types of the parameters after the comma is supplied.\ [#9899_note125]_

.. _9899_6.7.5.3p10:

:ref:`10 <9899_6.7.5.3p10>` The special case of an unnamed parameter of type void as the only item in the list specifies that the function has no parameters.

.. _9899_6.7.5.3p11:

:ref:`11 <9899_6.7.5.3p11>` If, in a parameter declaration, an identifier can be treated either as a typedef name or as a parameter name, it shall be taken as a typedef name.

.. _9899_6.7.5.3p12:

:ref:`12 <9899_6.7.5.3p12>` If the function declarator is not part of a definition of that function, parameters may have incomplete type and may use the [\*] notation in their sequences of declarator specifiers to specify variable length array types.

.. _9899_6.7.5.3p13:

:ref:`13 <9899_6.7.5.3p13>` The storage-class specifier in the declaration specifiers for a parameter declaration, if present, is ignored unless the declared parameter is one of the members of the parameter type list for a function definition.

.. _9899_6.7.5.3p14:

:ref:`14 <9899_6.7.5.3p14>` An identifier list declares only the identifiers of the parameters of the function. An empty list in a function declarator that is part of a definition of that function specifies that the function has no parameters. The empty list in a function declarator that is not part of a definition of that function specifies that no information about the number or types of the parameters is supplied.\ [#9899_note126]_

.. _9899_6.7.5.3p15:

:ref:`15 <9899_6.7.5.3p15>` For two function types to be compatible, both shall specify compatible return types.\ [#9899_note127]_ Moreover, the parameter type lists, if both are present, shall agree in the number of parameters and in use of the ellipsis terminator; corresponding parameters shall have compatible types. If one type has a parameter type list and the other type is specified by a function declarator that is not part of a function definition and that contains an empty identifier list, the parameter list shall not have an ellipsis terminator and the type of each parameter shall be compatible with the type that results from the application of the default argument promotions. If one type has a parameter type list and the other type is specified by a function definition that contains a (possibly empty) identifier list, both shall agree in the number of parameters, and the type of each prototype parameter shall be compatible with the type that results from the application of the default argument promotions to the type of the corresponding identifier. (In the determination of type compatibility and of a composite type, each parameter declared with function or array type is taken as having the adjusted type and each parameter declared with qualified type is taken as having the unqualified version of its declared type.)

.. _9899_6.7.5.3p16:

:ref:`16 <9899_6.7.5.3p16>` EXAMPLE 1 The declaration

::

    int f(void), *fip(), (*pfi)();

declares a function f with no parameters returning an int, a function fip with no parameter specification returning a pointer to an int, and a pointer pfi to a function with no parameter specification returning an int. It is especially useful to compare the last two. The binding of \*fip() is \*(fip()), so that the declaration suggests, and the same construction in an expression requires, the calling of a function fip, and then using indirection through the pointer result to yield an int. In the declarator (\*pfi)(), the extra parentheses are necessary to indicate that indirection through a pointer to a function yields a function designator, which is then used to call the function; it returns an int.

.. _9899_6.7.5.3p17:

:ref:`17 <9899_6.7.5.3p17>` If the declaration occurs outside of any function, the identifiers have file scope and external linkage. If the declaration occurs inside a function, the identifiers of the functions f and fip have block scope and either internal or external linkage (depending on what file scope declarations for these identifiers are visible), and the identifier of the pointer pfi has block scope and no linkage.

.. _9899_6.7.5.3p18:

:ref:`18 <9899_6.7.5.3p18>` EXAMPLE 2 The declaration

::

    int (*apfi[3])(int *x, int *y);

declares an array apfi of three pointers to functions returning int. Each of these functions has two parameters that are pointers to int. The identifiers x and y are declared for descriptive purposes only and go out of scope at the end of the declaration of apfi.

.. _9899_6.7.5.3p19:

:ref:`19 <9899_6.7.5.3p19>` EXAMPLE 3 The declaration

::

    int (*fpfi(int (*)(long), int))(int, ...);

declares a function fpfi that returns a pointer to a function returning an int. The function fpfi has two parameters: a pointer to a function returning an int (with one parameter of type long int), and an int. The pointer returned by fpfi points to a function that has one int parameter and accepts zero or more additional arguments of any type.

.. _9899_6.7.5.3p20:

:ref:`20 <9899_6.7.5.3p20>` EXAMPLE 4 The following prototype has a variably modified parameter.

::

    void addscalar(int n, int m,
          double a[n][n*m+300], double x);
    int main()
    {
          double b[4][308];
          addscalar(4, 2, b, 2.17);
          return 0;
    }
    void addscalar(int n, int m,
          double a[n][n*m+300], double x)
    {
          for (int i = 0; i < n; i++)
                for (int j = 0, k = n*m+300; j < k; j++)
                      // a is a pointer to a VLA with n*m+300 elements
                      a[i][j] += x;
    }

.. _9899_6.7.5.3p21:

:ref:`21 <9899_6.7.5.3p21>` EXAMPLE 5 The following are all compatible function prototype declarators.

::

    double    maximum(int       n,   int   m,   double   a[n][m]);
    double    maximum(int       n,   int   m,   double   a[*][*]);
    double    maximum(int       n,   int   m,   double   a[ ][*]);
    double    maximum(int       n,   int   m,   double   a[ ][m]);

as are:

::

    void   f(double     (* restrict a)[5]);
    void   f(double     a[restrict][5]);
    void   f(double     a[restrict 3][5]);
    void   f(double     a[restrict static 3][5]);

(Note that the last declaration also specifies that the argument corresponding to a in any call to f must be a non-null pointer to the first of at least three arrays of 5 doubles, which the others do not.)

**Forward references**: function definitions (:ref:`6.9.1 <9899_6.9.1>`), type names (:ref:`6.7.6 <9899_6.7.6>`).







.. rubric:: Footnotes

.. [#9899_note125] The macros defined in the :ref:`\<stdarg.h> <9899_7.15>` header (:ref:`7.15 <9899_7.15>`) may be used to access arguments that correspond to the ellipsis.
.. [#9899_note126] See ''future language directions'' (:ref:`6.11.6 <9899_6.11.6>`).
.. [#9899_note127] If both function types are ''old style'', parameter types are not compared.
