.. _9899_6.3.2.1:

6.3.2.1 Lvalues, arrays, and function designators
'''''''''''''''''''''''''''''''''''''''''''''''''

.. _9899_6.3.2.1p1:

:ref:`1 <9899_6.3.2.1p1>` An lvalue is an expression with an object type or an incomplete type other than void;\ [#9899_note53]_ if an lvalue does not designate an object when it is evaluated, the behavior is undefined. When an object is said to have a particular type, the type is specified by the lvalue used to designate the object. A modifiable lvalue is an lvalue that does not have array type, does not have an incomplete type, does not have a const-qualified type, and if it is a structure or union, does not have any member (including, recursively, any member or element of all contained aggregates or unions) with a const-qualified type.

.. _9899_6.3.2.1p2:

:ref:`2 <9899_6.3.2.1p2>` Except when it is the operand of the sizeof operator, the unary & operator, the ++ operator, the -- operator, or the left operand of the . operator or an assignment operator, an lvalue that does not have array type is converted to the value stored in the designated object (and is no longer an lvalue). If the lvalue has qualified type, the value has the unqualified version of the type of the lvalue; otherwise, the value has the type of the lvalue. If the lvalue has an incomplete type and does not have array type, the behavior is undefined.

.. _9899_6.3.2.1p3:

:ref:`3 <9899_6.3.2.1p3>` Except when it is the operand of the sizeof operator or the unary & operator, or is a string literal used to initialize an array, an expression that has type ''array of type'' is converted to an expression with type ''pointer to type'' that points to the initial element of the array object and is not an lvalue. If the array object has register storage class, the behavior is undefined.

.. _9899_6.3.2.1p4:

:ref:`4 <9899_6.3.2.1p4>` A function designator is an expression that has function type. Except when it is the operand of the sizeof operator\ [#9899_note54]_ or the unary & operator, a function designator with type ''function returning type'' is converted to an expression that has type ''pointer to function returning type''.

**Forward references**: address and indirection operators (:ref:`6.5.3.2 <9899_6.5.3.2>`), assignment operators (:ref:`6.5.16 <9899_6.5.16>`), common definitions :ref:`\<stddef.h> <9899_7.17>` (:ref:`7.17 <9899_7.17>`), initialization (:ref:`6.7.8 <9899_6.7.8>`), postfix increment and decrement operators (:ref:`6.5.2.4 <9899_6.5.2.4>`), prefix increment and decrement operators (:ref:`6.5.3.1 <9899_6.5.3.1>`), the sizeof operator (:ref:`6.5.3.4 <9899_6.5.3.4>`), structure and union members (:ref:`6.5.2.3 <9899_6.5.2.3>`).






.. rubric:: Footnotes

.. [#9899_note53] The name ''lvalue'' comes originally from the assignment expression E1 = E2, in which the left operand E1 is required to be a (modifiable) lvalue. It is perhaps better considered as representing an object ''locator value''. What is sometimes called ''rvalue'' is in this International Standard described as the ''value of an expression''. An obvious example of an lvalue is an identifier of an object. As a further example, if E is a unary expression that is a pointer to an object, \*E is an lvalue that designates the object to which E points.
.. [#9899_note54] Because this conversion does not occur, the operand of the sizeof operator remains a function designator and violates the constraint in :ref:`6.5.3.4 <9899_6.5.3.4>`.
