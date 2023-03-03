.. _9899_6.5.6:

6.5.6 Additive operators
^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.5.6p1:

:ref:`1 <9899_6.5.6p1>`

.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            additive-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            multiplicative-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            additive-expression
     
   
         .. container:: syntax-terminal
   
            \+
     
   
         .. container:: syntax-nonterminal
   
            multiplicative-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            additive-expression
     
   
         .. container:: syntax-terminal
   
            \-
     
   
         .. container:: syntax-nonterminal
   
            multiplicative-expression

.. rubric:: Constraints

.. _9899_6.5.6p2:

:ref:`2 <9899_6.5.6p2>` For addition, either both operands shall have arithmetic type, or one operand shall be a pointer to an object type and the other shall have integer type. (Incrementing is equivalent to adding 1.)

.. _9899_6.5.6p3:

:ref:`3 <9899_6.5.6p3>` For subtraction, one of the following shall hold:

-  both operands have arithmetic type;
-  both operands are pointers to qualified or unqualified versions of compatible object types; or
-  the left operand is a pointer to an object type and the right operand has integer type.

(Decrementing is equivalent to subtracting 1.)

.. rubric:: Semantics

.. _9899_6.5.6p4:

:ref:`4 <9899_6.5.6p4>` If both operands have arithmetic type, the usual arithmetic conversions are performed on them.

.. _9899_6.5.6p5:

:ref:`5 <9899_6.5.6p5>` The result of the binary + operator is the sum of the operands.

.. _9899_6.5.6p6:

:ref:`6 <9899_6.5.6p6>` The result of the binary - operator is the difference resulting from the subtraction of the second operand from the first.

.. _9899_6.5.6p7:

:ref:`7 <9899_6.5.6p7>` For the purposes of these operators, a pointer to an object that is not an element of an array behaves the same as a pointer to the first element of an array of length one with the type of the object as its element type.

.. _9899_6.5.6p8:

:ref:`8 <9899_6.5.6p8>` When an expression that has integer type is added to or subtracted from a pointer, the result has the type of the pointer operand. If the pointer operand points to an element of an array object, and the array is large enough, the result points to an element offset from the original element such that the difference of the subscripts of the resulting and original array elements equals the integer expression. In other words, if the expression P points to the i-th element of an array object, the expressions (P)+N (equivalently, N+(P)) and (P)-N (where N has the value n) point to, respectively, the i+n-th and i-n-th elements of the array object, provided they exist. Moreover, if the expression P points to the last element of an array object, the expression (P)+1 points one past the last element of the array object, and if the expression Q points one past the last element of an array object, the expression (Q)-1 points to the last element of the array object. If both the pointer operand and the result point to elements of the same array object, or one past the last element of the array object, the evaluation shall not produce an overflow; otherwise, the behavior is undefined. If the result points one past the last element of the array object, it shall not be used as the operand of a unary \* operator that is evaluated.

.. _9899_6.5.6p9:

:ref:`9 <9899_6.5.6p9>` When two pointers are subtracted, both shall point to elements of the same array object, or one past the last element of the array object; the result is the difference of the subscripts of the two array elements. The size of the result is implementation-defined, and its type (a signed integer type) is ptrdiff_t defined in the :ref:`\<stddef.h> <9899_7.17>` header. If the result is not representable in an object of that type, the behavior is undefined. In other words, if the expressions P and Q point to, respectively, the i-th and j-th elements of an array object, the expression (P)-(Q) has the value i-j provided the value fits in an object of type ptrdiff_t. Moreover, if the expression P points either to an element of an array object or one past the last element of an array object, and the expression Q points to the last element of the same array object, the expression ((Q)+1)-(P) has the same value as ((Q)-(P))+1 and as -((P)-((Q)+1)), and has the value zero if the expression P points one past the last element of the array object, even though the expression (Q)+1 does not point to an element of the array object.\ [#9899_note91]_

.. _9899_6.5.6p10:

:ref:`10 <9899_6.5.6p10>` EXAMPLE Pointer arithmetic is well defined with pointers to variable length array types.

::

    {
             int n = 4, m = 3;
             int a[n][m];
             int (*p)[m] = a;            //   p == &a[0]
             p += 1;                     //   p == &a[1]
             (*p)[2] = 99;               //   a[1][2] == 99
             n = p - a;                  //   n == 1
    }

.. _9899_6.5.6p11:

:ref:`11 <9899_6.5.6p11>` If array a in the above example were declared to be an array of known constant size, and pointer p were declared to be a pointer to an array of the same known constant size (pointing to a), the results would be the same.

**Forward references**: array declarators (:ref:`6.7.5.2 <9899_6.7.5.2>`), common definitions :ref:`\<stddef.h> <9899_7.17>` (:ref:`7.17 <9899_7.17>`).





.. rubric:: Footnotes

.. [#9899_note91] Another way to approach pointer arithmetic is first to convert the pointer(s) to character pointer(s): In this scheme the integer expression added to or subtracted from the converted pointer is first multiplied by the size of the object originally pointed to, and the resulting pointer is converted back to the original type. For pointer subtraction, the result of the difference between the character pointers is similarly divided by the size of the object originally pointed to. When viewed in this way, an implementation need only provide one extra byte (which may overlap another object in the program) just after the end of the object in order to satisfy the ''one past the last element'' requirements.
