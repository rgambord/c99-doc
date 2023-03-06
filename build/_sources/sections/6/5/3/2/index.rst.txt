.. _9899_6.5.3.2:

6.5.3.2 Address and indirection operators
'''''''''''''''''''''''''''''''''''''''''

.. rubric:: Constraints

.. _9899_6.5.3.2p1:

.. container:: snum

   :ref:`1 <9899_6.5.3.2p1>`

The operand of the unary & operator shall be either a function designator, the result of a [] or unary \* operator, or an lvalue that designates an object that is not a bit-field and is not declared with the register storage-class specifier.

.. _9899_6.5.3.2p2:

.. container:: snum

   :ref:`2 <9899_6.5.3.2p2>`

The operand of the unary \* operator shall have pointer type.

.. rubric:: Semantics

.. _9899_6.5.3.2p3:

.. container:: snum

   :ref:`3 <9899_6.5.3.2p3>`

The unary & operator yields the address of its operand. If the operand has type "type", the result has type "pointer to type". If the operand is the result of a unary \* operator, neither that operator nor the & operator is evaluated and the result is as if both were omitted, except that the constraints on the operators still apply and the result is not an lvalue. Similarly, if the operand is the result of a [] operator, neither the & operator nor the unary \* that is implied by the [] is evaluated and the result is as if the & operator were removed and the [] operator were changed to a + operator. Otherwise, the result is a pointer to the object or function designated by its operand.

.. _9899_6.5.3.2p4:

.. container:: snum

   :ref:`4 <9899_6.5.3.2p4>`

The unary \* operator denotes indirection. If the operand points to a function, the result is a function designator; if it points to an object, the result is an lvalue designating the object. If the operand has type "pointer to type", the result has type "type". If an invalid value has been assigned to the pointer, the behavior of the unary \* operator is undefined.\ [#9899_note87]_

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.7.1`
   - :ref:`9899_6.7.2.1`





.. rubric:: Footnotes

.. [#9899_note87] Thus, &*E is equivalent to E (even if E is a null pointer), and &(E1[E2]) to ((E1)+(E2)). It is always true that if E is a function designator or an lvalue that is a valid operand of the unary & operator, \*&E is a function designator or an lvalue equal to E. If \*P is an lvalue and T is the name of an object pointer type, \*(T)P is an lvalue that has a type compatible with that to which T points. Among the invalid values for dereferencing a pointer by the unary \* operator are a null pointer, an address inappropriately aligned for the type of object pointed to, and the address of an object after the end of its lifetime.
