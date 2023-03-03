.. _9899_6.7.5:

6.7.5 Declarators
^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index


.. rubric:: Syntax

.. _9899_6.7.5p1:

:ref:`1 <9899_6.7.5p1>`

.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            declarator
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pointer
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            direct-declarator
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            direct-declarator
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            identifier
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            declarator
     
   
         .. container:: syntax-terminal
   
            )
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-declarator
     
   
         .. container:: syntax-terminal
   
            [
     
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            assignment-expression
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            ]
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-declarator
     
   
         .. container:: syntax-terminal
   
            [
     
   
         .. container:: syntax-terminal
   
            static
     
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            assignment-expression
     
   
         .. container:: syntax-terminal
   
            ]
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-declarator
     
   
         .. container:: syntax-terminal
   
            [
     
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
     
   
         .. container:: syntax-terminal
   
            static
     
   
         .. container:: syntax-nonterminal
   
            assignment-expression
     
   
         .. container:: syntax-terminal
   
            ]
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-declarator
     
   
         .. container:: syntax-terminal
   
            [
     
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            \*
     
   
         .. container:: syntax-terminal
   
            ]
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-declarator
     
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            parameter-type-list
     
   
         .. container:: syntax-terminal
   
            )
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-declarator
     
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            identifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            )
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            pointer
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            \*
     
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            \*
     
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            pointer
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            type-qualifier
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
     
   
         .. container:: syntax-nonterminal
   
            type-qualifier
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            parameter-type-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            parameter-list
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            parameter-list
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-terminal
   
            \.\.\.
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            parameter-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            parameter-declaration
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            parameter-list
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-nonterminal
   
            parameter-declaration
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            parameter-declaration
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            declaration-specifiers
     
   
         .. container:: syntax-nonterminal
   
            declarator
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            declaration-specifiers
     
   
         .. container:: syntax-nonterminal
   
            abstract-declarator
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            identifier-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            identifier
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            identifier-list
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-nonterminal
   
            identifier

.. rubric:: Semantics

.. _9899_6.7.5p2:

:ref:`2 <9899_6.7.5p2>` Each declarator declares one identifier, and asserts that when an operand of the same form as the declarator appears in an expression, it designates a function or object with the scope, storage duration, and type indicated by the declaration specifiers.

.. _9899_6.7.5p3:

:ref:`3 <9899_6.7.5p3>` A full declarator is a declarator that is not part of another declarator. The end of a full declarator is a sequence point. If, in the nested sequence of declarators in a full declarator, there is a declarator specifying a variable length array type, the type specified by the full declarator is said to be variably modified. Furthermore, any type derived by declarator type derivation from a variably modified type is itself variably modified.

.. _9899_6.7.5p4:

:ref:`4 <9899_6.7.5p4>` In the following subclauses, consider a declaration

.. code-block:: text

    T D1

where T contains the declaration specifiers that specify a type T (such as int) and D1 is a declarator that contains an identifier ident. The type specified for the identifier ident in the various forms of declarator is described inductively using this notation.

.. _9899_6.7.5p5:

:ref:`5 <9899_6.7.5p5>` If, in the declaration ''T D1'', D1 has the form

.. code-block:: text

    identifier

then the type specified for ident is T .

.. _9899_6.7.5p6:

:ref:`6 <9899_6.7.5p6>` If, in the declaration ''T D1'', D1 has the form

.. code-block:: text

    ( D )

then ident has the type specified by the declaration ''T D''. Thus, a declarator in parentheses is identical to the unparenthesized declarator, but the binding of complicated declarators may be altered by parentheses.

.. rubric:: Implementation limits

.. _9899_6.7.5p7:

:ref:`7 <9899_6.7.5p7>` As discussed in :ref:`5.2.4.1 <9899_5.2.4.1>`, an implementation may limit the number of pointer, array, and function declarators that modify an arithmetic, structure, union, or incomplete type, either directly or via one or more typedefs.

**Forward references**: array declarators (:ref:`6.7.5.2 <9899_6.7.5.2>`), type definitions (:ref:`6.7.7 <9899_6.7.7>`).

