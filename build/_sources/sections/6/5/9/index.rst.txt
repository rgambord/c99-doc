.. _9899_6.5.9:

6.5.9 Equality operators
^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.5.9p1:

.. container:: snum

   :ref:`1 <9899_6.5.9p1>`



.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            equality-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            relational-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            equality-expression
     
   
         .. container:: syntax-terminal
   
            ==
     
   
         .. container:: syntax-nonterminal
   
            relational-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            equality-expression
     
   
         .. container:: syntax-terminal
   
            !=
     
   
         .. container:: syntax-nonterminal
   
            relational-expression

.. rubric:: Constraints

.. _9899_6.5.9p2:

.. container:: snum

   :ref:`2 <9899_6.5.9p2>`

One of the following shall hold:

-  both operands have arithmetic type;
-  both operands are pointers to qualified or unqualified versions of compatible types;
-  one operand is a pointer to an object or incomplete type and the other is a pointer to a qualified or unqualified version of void; or
-  one operand is a pointer and the other is a null pointer constant.

.. rubric:: Semantics

.. _9899_6.5.9p3:

.. container:: snum

   :ref:`3 <9899_6.5.9p3>`

The == (equal to) and != (not equal to) operators are analogous to the relational operators except for their lower precedence.\ [#9899_note93]_ Each of the operators yields 1 if the specified relation is true and 0 if it is false. The result has type int. For any pair of operands, exactly one of the relations is true.

.. _9899_6.5.9p4:

.. container:: snum

   :ref:`4 <9899_6.5.9p4>`

If both of the operands have arithmetic type, the usual arithmetic conversions are performed. Values of complex types are equal if and only if both their real parts are equal and also their imaginary parts are equal. Any two values of arithmetic types from different type domains are equal if and only if the results of their conversions to the (complex) result type determined by the usual arithmetic conversions are equal.

.. _9899_6.5.9p5:

.. container:: snum

   :ref:`5 <9899_6.5.9p5>`

Otherwise, at least one operand is a pointer. If one operand is a pointer and the other is a null pointer constant, the null pointer constant is converted to the type of the pointer. If one operand is a pointer to an object or incomplete type and the other is a pointer to a qualified or unqualified version of void, the former is converted to the type of the latter.

.. _9899_6.5.9p6:

.. container:: snum

   :ref:`6 <9899_6.5.9p6>`

Two pointers compare equal if and only if both are null pointers, both are pointers to the same object (including a pointer to an object and a subobject at its beginning) or function, both are pointers to one past the last element of the same array object, or one is a pointer to one past the end of one array object and the other is a pointer to the start of a different array object that happens to immediately follow the first array object in the address space.\ [#9899_note94]_

.. _9899_6.5.9p7:

.. container:: snum

   :ref:`7 <9899_6.5.9p7>`

For the purposes of these operators, a pointer to an object that is not an element of an array behaves the same as a pointer to the first element of an array of length one with the type of the object as its element type.






.. rubric:: Footnotes

.. [#9899_note93] Because of the precedences, a<b == c<d is 1 whenever a<b and c<d have the same truth-value.
.. [#9899_note94] Two objects may be adjacent in memory because they are adjacent elements of a larger array or adjacent members of a structure with no padding between them, or because the implementation chose to place them so, even though they are unrelated. If prior invalid pointer operations (such as accesses outside array bounds) produced undefined behavior, subsequent comparisons also produce undefined behavior.
