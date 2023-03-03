.. _9899_6.7.2.2:

6.7.2.2 Enumeration specifiers
''''''''''''''''''''''''''''''

.. rubric:: Syntax

.. _9899_6.7.2.2p1:

:ref:`1 <9899_6.7.2.2p1>`

.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            enum-specifier
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            enum
     
   
         .. container:: syntax-nonterminal
   
            identifier
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            {
     
   
         .. container:: syntax-nonterminal
   
            enumerator-list
     
   
         .. container:: syntax-terminal
   
            }
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            enum
     
   
         .. container:: syntax-nonterminal
   
            identifier
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            {
     
   
         .. container:: syntax-nonterminal
   
            enumerator-list
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-terminal
   
            }
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            enum
     
   
         .. container:: syntax-nonterminal
   
            identifier
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            enumerator-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            enumerator
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            enumerator-list
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-nonterminal
   
            enumerator
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            enumerator
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            enumeration-constant
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            enumeration-constant
     
   
         .. container:: syntax-terminal
   
            =
     
   
         .. container:: syntax-nonterminal
   
            constant-expression

.. rubric:: Constraints

.. _9899_6.7.2.2p2:

:ref:`2 <9899_6.7.2.2p2>` The expression that defines the value of an enumeration constant shall be an integer constant expression that has a value representable as an int.

.. rubric:: Semantics

.. _9899_6.7.2.2p3:

:ref:`3 <9899_6.7.2.2p3>` The identifiers in an enumerator list are declared as constants that have type int and may appear wherever such are permitted.\ [#9899_note109]_ An enumerator with = defines its enumeration constant as the value of the constant expression. If the first enumerator has no =, the value of its enumeration constant is 0. Each subsequent enumerator with no = defines its enumeration constant as the value of the constant expression obtained by adding 1 to the value of the previous enumeration constant. (The use of enumerators with = may produce enumeration constants with values that duplicate other values in the same enumeration.) The enumerators of an enumeration are also known as its members.

.. _9899_6.7.2.2p4:

:ref:`4 <9899_6.7.2.2p4>` Each enumerated type shall be compatible with char, a signed integer type, or an unsigned integer type. The choice of type is implementation-defined,\ [#9899_note110]_ but shall be capable of representing the values of all the members of the enumeration. The enumerated type is incomplete until after the } that terminates the list of enumerator declarations.

.. _9899_6.7.2.2p5:

:ref:`5 <9899_6.7.2.2p5>` EXAMPLE The following fragment:

::

    enum hue { chartreuse, burgundy, claret=20, winedark };
    enum hue col, *cp;
    col = claret;
    cp = &col;
    if (*cp != burgundy)
          /* ... */

makes hue the tag of an enumeration, and then declares col as an object that has that type and cp as a pointer to an object that has that type. The enumerated values are in the set { 0, 1, 20, 21 }.

**Forward references**: tags (:ref:`6.7.2.3 <9899_6.7.2.3>`).






.. rubric:: Footnotes

.. [#9899_note109] Thus, the identifiers of enumeration constants declared in the same scope shall all be distinct from each other and from other identifiers declared in ordinary declarators.
.. [#9899_note110] An implementation may delay the choice of which integer type until all enumeration constants have been seen.
