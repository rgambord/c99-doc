.. _9899_6.7.6:

6.7.6 Type names
^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.7.6p1:

.. container:: snum

   :ref:`1 <9899_6.7.6p1>`



.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            type-name
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            specifier-qualifier-list
     
   
         .. container:: syntax-nonterminal
   
            abstract-declarator
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            abstract-declarator
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pointer
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pointer
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            direct-abstract-declarator
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            direct-abstract-declarator
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            abstract-declarator
     
   
         .. container:: syntax-terminal
   
            )
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-abstract-declarator
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            [
     
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            assignment-expression
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            ]
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-abstract-declarator
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            [
     
   
         .. container:: syntax-terminal
   
            static
     
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            assignment-expression
     
   
         .. container:: syntax-terminal
   
            ]
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-abstract-declarator
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            [
     
   
         .. container:: syntax-nonterminal
   
            type-qualifier-list
     
   
         .. container:: syntax-terminal
   
            static
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            assignment-expression
     
   
         .. container:: syntax-terminal
   
            ]
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-abstract-declarator
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            [
     
   
         .. container:: syntax-terminal
   
            \*
     
   
         .. container:: syntax-terminal
   
            ]
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            direct-abstract-declarator
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            parameter-type-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            )

.. rubric:: Semantics

.. _9899_6.7.6p2:

.. container:: snum

   :ref:`2 <9899_6.7.6p2>`

In several contexts, it is necessary to specify a type. This is accomplished using a type name, which is syntactically a declaration for a function or an object of that type that omits the identifier.\ [#9899_note128]_

.. _9899_6.7.6p3:

.. container:: snum

   :ref:`3 <9899_6.7.6p3>`

EXAMPLE The constructions

.. code-block:: text

    (a)      int
    (b)      int   *
    (c)      int   *[3]
    (d)      int   (*)[3]
    (e)      int   (*)[*]
    (f)      int   *()
    (g)      int   (*)(void)
    (h)      int   (*const [])(unsigned int, ...)

name respectively the types (a) int, (b) pointer to int, (c) array of three pointers to int, (d) pointer to an array of three ints, (e) pointer to a variable length array of an unspecified number of ints, (f) function with no parameter specification returning a pointer to int, (g) pointer to function with no parameters returning an int, and (h) array of an unspecified number of constant pointers to functions, each with one parameter that has type unsigned int and an unspecified number of other parameters, returning an int.





.. rubric:: Footnotes

.. [#9899_note128] As indicated by the syntax, empty parentheses in a type name are interpreted as "function with no parameter specification", rather than redundant parentheses around the omitted identifier.
