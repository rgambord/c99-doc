.. _9899_6.5.2.1:

6.5.2.1 Array subscripting
''''''''''''''''''''''''''

.. rubric:: Constraints

.. _9899_6.5.2.1p1:

:ref:`1 <9899_6.5.2.1p1>` One of the expressions shall have type ''pointer to object type'', the other expression shall have integer type, and the result has type ''type''.

.. rubric:: Semantics

.. _9899_6.5.2.1p2:

:ref:`2 <9899_6.5.2.1p2>` A postfix expression followed by an expression in square brackets [] is a subscripted designation of an element of an array object. The definition of the subscript operator [] is that E1[E2] is identical to (\*((E1)+(E2))). Because of the conversion rules that apply to the binary + operator, if E1 is an array object (equivalently, a pointer to the initial element of an array object) and E2 is an integer, E1[E2] designates the E2-th element of E1 (counting from zero).

.. _9899_6.5.2.1p3:

:ref:`3 <9899_6.5.2.1p3>` Successive subscript operators designate an element of a multidimensional array object. If E is an n-dimensional array (n >= 2) with dimensions i x j x . . . x k, then E (used as other than an lvalue) is converted to a pointer to an (n - 1)-dimensional array with dimensions j x . . . x k. If the unary \* operator is applied to this pointer explicitly, or implicitly as a result of subscripting, the result is the pointed-to (n - 1)-dimensional array, which itself is converted into a pointer if used as other than an lvalue. It follows from this that arrays are stored in row-major order (last subscript varies fastest).

.. _9899_6.5.2.1p4:

:ref:`4 <9899_6.5.2.1p4>` EXAMPLE Consider the array object defined by the declaration

::

    int x[3][5];

Here x is a 3 x 5 array of ints; more precisely, x is an array of three element objects, each of which is an array of five ints. In the expression x[i], which is equivalent to (\*((x)+(i))), x is first converted to a pointer to the initial array of five ints. Then i is adjusted according to the type of x, which conceptually entails multiplying i by the size of the object to which the pointer points, namely an array of five int objects. The results are added and indirection is applied to yield an array of five ints. When used in the expression x[i][j], that array is in turn converted to a pointer to the first of the ints, so x[i][j] yields an int.

**Forward references**: additive operators (:ref:`6.5.6 <9899_6.5.6>`), address and indirection operators (:ref:`6.5.3.2 <9899_6.5.3.2>`), array declarators (:ref:`6.7.5.2 <9899_6.7.5.2>`).

