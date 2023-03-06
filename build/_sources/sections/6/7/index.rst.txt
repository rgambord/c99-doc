.. _9899_6.7:

6.7 Declarations
~~~~~~~~~~~~~~~~


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index
   4/index
   5/index
   6/index
   7/index
   8/index


.. rubric:: Syntax

.. _9899_6.7p1:

.. container:: snum

   :ref:`1 <9899_6.7p1>`



.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            declaration
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            declaration-specifiers
     
   
         .. container:: syntax-nonterminal
   
            init-declarator-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            ;
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            declaration-specifiers
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            storage-class-specifier
     
   
         .. container:: syntax-nonterminal
   
            declaration-specifiers
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            type-specifier
     
   
         .. container:: syntax-nonterminal
   
            declaration-specifiers
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            type-qualifier
     
   
         .. container:: syntax-nonterminal
   
            declaration-specifiers
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            function-specifier
     
   
         .. container:: syntax-nonterminal
   
            declaration-specifiers
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            init-declarator-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            init-declarator
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            init-declarator-list
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-nonterminal
   
            init-declarator
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            init-declarator
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            declarator
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            declarator
     
   
         .. container:: syntax-terminal
   
            =
     
   
         .. container:: syntax-nonterminal
   
            initializer

.. rubric:: Constraints

.. _9899_6.7p2:

.. container:: snum

   :ref:`2 <9899_6.7p2>`

A declaration shall declare at least a declarator (other than the parameters of a function or the members of a structure or union), a tag, or the members of an enumeration.

.. _9899_6.7p3:

.. container:: snum

   :ref:`3 <9899_6.7p3>`

If an identifier has no linkage, there shall be no more than one declaration of the identifier (in a declarator or type specifier) with the same scope and in the same name space, except for tags as specified in :ref:`6.7.2.3 <9899_6.7.2.3>`.

.. _9899_6.7p4:

.. container:: snum

   :ref:`4 <9899_6.7p4>`

All declarations in the same scope that refer to the same object or function shall specify compatible types.

.. rubric:: Semantics

.. _9899_6.7p5:

.. container:: snum

   :ref:`5 <9899_6.7p5>`

A declaration specifies the interpretation and attributes of a set of identifiers. A definition of an identifier is a declaration for that identifier that:

-  for an object, causes storage to be reserved for that object;
-  for a function, includes the function body;\ [#9899_note101]_
-  for an enumeration constant or typedef name, is the (only) declaration of the identifier.

.. _9899_6.7p6:

.. container:: snum

   :ref:`6 <9899_6.7p6>`

The declaration specifiers consist of a sequence of specifiers that indicate the linkage, storage duration, and part of the type of the entities that the declarators denote. The init- declarator-list is a comma-separated sequence of declarators, each of which may have additional type information, or an initializer, or both. The declarators contain the identifiers (if any) being declared.

.. _9899_6.7p7:

.. container:: snum

   :ref:`7 <9899_6.7p7>`

If an identifier for an object is declared with no linkage, the type for the object shall be complete by the end of its declarator, or by the end of its init-declarator if it has an initializer; in the case of function parameters (including in prototypes), it is the adjusted type (see :ref:`6.7.5.3 <9899_6.7.5.3>`) that is required to be complete.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.7.5`
   - :ref:`9899_6.7.2.2`
   - :ref:`9899_6.7.8`





.. rubric:: Footnotes

.. [#9899_note101] Function definitions have a different syntax, described in :ref:`6.9.1 <9899_6.9.1>`.
