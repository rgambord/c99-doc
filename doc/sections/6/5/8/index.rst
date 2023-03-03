.. _9899_6.5.8:

6.5.8 Relational operators
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.5.8p1:

:ref:`1 <9899_6.5.8p1>`

.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            relational-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            shift-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            relational-expression
     
   
         .. container:: syntax-terminal
   
            <
     
   
         .. container:: syntax-nonterminal
   
            shift-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            relational-expression
     
   
         .. container:: syntax-terminal
   
            >
     
   
         .. container:: syntax-nonterminal
   
            shift-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            relational-expression
     
   
         .. container:: syntax-terminal
   
            <=
     
   
         .. container:: syntax-nonterminal
   
            shift-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            relational-expression
     
   
         .. container:: syntax-terminal
   
            >=
     
   
         .. container:: syntax-nonterminal
   
            shift-expression

.. rubric:: Constraints

.. _9899_6.5.8p2:

:ref:`2 <9899_6.5.8p2>` One of the following shall hold:

-  both operands have real type;
-  both operands are pointers to qualified or unqualified versions of compatible object types; or
-  both operands are pointers to qualified or unqualified versions of compatible incomplete types.

.. rubric:: Semantics

.. _9899_6.5.8p3:

:ref:`3 <9899_6.5.8p3>` If both of the operands have arithmetic type, the usual arithmetic conversions are performed.

.. _9899_6.5.8p4:

:ref:`4 <9899_6.5.8p4>` For the purposes of these operators, a pointer to an object that is not an element of an array behaves the same as a pointer to the first element of an array of length one with the type of the object as its element type.

.. _9899_6.5.8p5:

:ref:`5 <9899_6.5.8p5>` When two pointers are compared, the result depends on the relative locations in the address space of the objects pointed to. If two pointers to object or incomplete types both point to the same object, or both point one past the last element of the same array object, they compare equal. If the objects pointed to are members of the same aggregate object, pointers to structure members declared later compare greater than pointers to members declared earlier in the structure, and pointers to array elements with larger subscript values compare greater than pointers to elements of the same array with lower subscript values. All pointers to members of the same union object compare equal. If the expression P points to an element of an array object and the expression Q points to the last element of the same array object, the pointer expression Q+1 compares greater than P. In all other cases, the behavior is undefined.

.. _9899_6.5.8p6:

:ref:`6 <9899_6.5.8p6>` Each of the operators \< (less than), > (greater than), <= (less than or equal to), and >= (greater than or equal to) shall yield 1 if the specified relation is true and 0 if it is false.\ [#9899_note92]_ The result has type int.





.. rubric:: Footnotes

.. [#9899_note92] The expression a<b<c is not interpreted as in ordinary mathematics. As the syntax indicates, it means (a<b)<c; in other words, ''if a is less than b, compare 1 to c; otherwise, compare 0 to c''.
