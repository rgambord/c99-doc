.. _9899_6.9.1:

6.9.1 Function definitions
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.9.1p1:

:ref:`1 <9899_6.9.1p1>`

.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            function-definition
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            declaration-specifiers
     
   
         .. container:: syntax-nonterminal
   
            declarator
     
   
         .. container:: syntax-nonterminal
   
            declaration-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            compound-statement
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            declaration-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            declaration
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            declaration-list
     
   
         .. container:: syntax-nonterminal
   
            declaration

.. rubric:: Constraints

.. _9899_6.9.1p2:

:ref:`2 <9899_6.9.1p2>` The identifier declared in a function definition (which is the name of the function) shall have a function type, as specified by the declarator portion of the function definition.\ [#9899_note141]_

.. _9899_6.9.1p3:

:ref:`3 <9899_6.9.1p3>` The return type of a function shall be void or an object type other than array type.

.. _9899_6.9.1p4:

:ref:`4 <9899_6.9.1p4>` The storage-class specifier, if any, in the declaration specifiers shall be either extern or static.

.. _9899_6.9.1p5:

:ref:`5 <9899_6.9.1p5>` If the declarator includes a parameter type list, the declaration of each parameter shall include an identifier, except for the special case of a parameter list consisting of a single parameter of type void, in which case there shall not be an identifier. No declaration list shall follow.

.. _9899_6.9.1p6:

:ref:`6 <9899_6.9.1p6>` If the declarator includes an identifier list, each declaration in the declaration list shall have at least one declarator, those declarators shall declare only identifiers from the identifier list, and every identifier in the identifier list shall be declared. An identifier declared as a typedef name shall not be redeclared as a parameter. The declarations in the declaration list shall contain no storage-class specifier other than register and no initializations.

.. rubric:: Semantics

.. _9899_6.9.1p7:

:ref:`7 <9899_6.9.1p7>` The declarator in a function definition specifies the name of the function being defined and the identifiers of its parameters. If the declarator includes a parameter type list, the list also specifies the types of all the parameters; such a declarator also serves as a function prototype for later calls to the same function in the same translation unit. If the declarator includes an identifier list,\ [#9899_note142]_ the types of the parameters shall be declared in a following declaration list. In either case, the type of each parameter is adjusted as described in :ref:`6.7.5.3 <9899_6.7.5.3>` for a parameter type list; the resulting type shall be an object type.

.. _9899_6.9.1p8:

:ref:`8 <9899_6.9.1p8>` If a function that accepts a variable number of arguments is defined without a parameter type list that ends with the ellipsis notation, the behavior is undefined.

.. _9899_6.9.1p9:

:ref:`9 <9899_6.9.1p9>` Each parameter has automatic storage duration. Its identifier is an lvalue, which is in effect declared at the head of the compound statement that constitutes the function body (and therefore cannot be redeclared in the function body except in an enclosed block). The layout of the storage for parameters is unspecified.

.. _9899_6.9.1p10:

:ref:`10 <9899_6.9.1p10>` On entry to the function, the size expressions of each variably modified parameter are evaluated and the value of each argument expression is converted to the type of the corresponding parameter as if by assignment. (Array expressions and function designators as arguments were converted to pointers before the call.)

.. _9899_6.9.1p11:

:ref:`11 <9899_6.9.1p11>` After all parameters have been assigned, the compound statement that constitutes the body of the function definition is executed.

.. _9899_6.9.1p12:

:ref:`12 <9899_6.9.1p12>` If the } that terminates a function is reached, and the value of the function call is used by the caller, the behavior is undefined.

.. _9899_6.9.1p13:

:ref:`13 <9899_6.9.1p13>` EXAMPLE 1 In the following:

::

    extern int max(int a, int b)
    {
          return a > b ? a : b;
    }

extern is the storage-class specifier and int is the type specifier; max(int a, int b) is the function declarator; and

::

    { return a > b ? a : b; }

is the function body. The following similar definition uses the identifier-list form for the parameter declarations:

::

    extern int max(a, b)
    int a, b;
    {
          return a > b ? a : b;
    }

Here int a, b; is the declaration list for the parameters. The difference between these two definitions is that the first form acts as a prototype declaration that forces conversion of the arguments of subsequent calls to the function, whereas the second form does not.

.. _9899_6.9.1p14:

:ref:`14 <9899_6.9.1p14>` EXAMPLE 2 To pass one function to another, one might say

::

    int f(void);
    /* ... */
    g(f);

Then the definition of g might read

::

    void g(int (*funcp)(void))
    {
          /* ... */
          (*funcp)(); /* or funcp(); ...                    */
    }

or, equivalently,

::

    void g(int func(void))
    {
          /* ... */
          func(); /* or (*func)(); ...                   */
    }



::

    typedef int F(void);                          //   type F is ''function with no parameters
                                                  //                  returning int''
    F f, g;                                       //   f and g both have type compatible with F
    F f { /* ... */ }                             //   WRONG: syntax/constraint error
    F g() { /* ... */ }                           //   WRONG: declares that g returns a function
    int f(void) { /* ... */ }                     //   RIGHT: f has type compatible with F
    int g() { /* ... */ }                         //   RIGHT: g has type compatible with F
    F *e(void) { /* ... */ }                      //   e returns a pointer to a function
    F *((e))(void) { /* ... */ }                  //   same: parentheses irrelevant
    int (*fp)(void);                              //   fp points to a function that has type F
    F *Fp;                                        //   Fp points to a function that has type F




.. rubric:: Footnotes

.. [#9899_note141] The intent is that the type category in a function definition cannot be inherited from a typedef:
.. [#9899_note142] See ''future language directions'' (:ref:`6.11.7 <9899_6.11.7>`).
