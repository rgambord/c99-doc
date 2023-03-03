.. _9899_6.5.16.1:

6.5.16.1 Simple assignment
''''''''''''''''''''''''''

.. rubric:: Constraints

.. _9899_6.5.16.1p1:

:ref:`1 <9899_6.5.16.1p1>` One of the following shall hold:[#9899_note96]_

-  the left operand has qualified or unqualified arithmetic type and the right has arithmetic type;
-  the left operand has a qualified or unqualified version of a structure or union type compatible with the type of the right;
-  both operands are pointers to qualified or unqualified versions of compatible types, and the type pointed to by the left has all the qualifiers of the type pointed to by the right;
-  one operand is a pointer to an object or incomplete type and the other is a pointer to a qualified or unqualified version of void, and the type pointed to by the left has all the qualifiers of the type pointed to by the right;
-  the left operand is a pointer and the right is a null pointer constant; or
-  the left operand has type \_Bool and the right is a pointer.

.. rubric:: Semantics

.. _9899_6.5.16.1p2:

:ref:`2 <9899_6.5.16.1p2>` In simple assignment (=), the value of the right operand is converted to the type of the assignment expression and replaces the value stored in the object designated by the left operand.

.. _9899_6.5.16.1p3:

:ref:`3 <9899_6.5.16.1p3>` If the value being stored in an object is read from another object that overlaps in any way the storage of the first object, then the overlap shall be exact and the two objects shall have qualified or unqualified versions of a compatible type; otherwise, the behavior is undefined.

.. _9899_6.5.16.1p4:

:ref:`4 <9899_6.5.16.1p4>` EXAMPLE 1 In the program fragment

::

    int f(void);
    char c;
    /* ... */
    if ((c = f()) == -1)
            /* ... */

the int value returned by the function may be truncated when stored in the char, and then converted back to int width prior to the comparison. In an implementation in which ''plain'' char has the same range of values as unsigned char (and char is narrower than int), the result of the conversion cannot be negative, so the operands of the comparison can never compare equal. Therefore, for full portability, the variable c should be declared as int.

.. _9899_6.5.16.1p5:

:ref:`5 <9899_6.5.16.1p5>` EXAMPLE 2 In the fragment:

::

    char c;
    int i;
    long l;
    l = (c = i);

the value of i is converted to the type of the assignment expression c = i, that is, char type. The value of the expression enclosed in parentheses is then converted to the type of the outer assignment expression, that is, long int type.

.. _9899_6.5.16.1p6:

:ref:`6 <9899_6.5.16.1p6>` EXAMPLE 3 Consider the fragment:

::

    const char **cpp;
    char *p;
    const char c = 'A';
    cpp = &p;                  // constraint violation
    *cpp = &c;                 // valid
    *p = 0;                    // valid

The first assignment is unsafe because it would allow the following valid code to attempt to change the value of the const object c.





.. rubric:: Footnotes

.. [#9899_note96] The asymmetric appearance of these constraints with respect to type qualifiers is due to the conversion (specified in :ref:`6.3.2.1 <9899_6.3.2.1>`) that changes lvalues to ''the value of the expression'' and thus removes any type qualifiers that were applied to the type category of the expression (for example, it removes const but not volatile from the type int volatile \* const).
