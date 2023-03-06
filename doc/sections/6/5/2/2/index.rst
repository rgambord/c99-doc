.. _9899_6.5.2.2:

6.5.2.2 Function calls
''''''''''''''''''''''

.. rubric:: Constraints

.. _9899_6.5.2.2p1:

.. container:: snum

   :ref:`1 <9899_6.5.2.2p1>`

The expression that denotes the called function\ [#9899_note80]_ shall have type pointer to function returning void or returning an object type other than an array type.

.. _9899_6.5.2.2p2:

.. container:: snum

   :ref:`2 <9899_6.5.2.2p2>`

If the expression that denotes the called function has a type that includes a prototype, the number of arguments shall agree with the number of parameters. Each argument shall have a type such that its value may be assigned to an object with the unqualified version of the type of its corresponding parameter.

.. rubric:: Semantics

.. _9899_6.5.2.2p3:

.. container:: snum

   :ref:`3 <9899_6.5.2.2p3>`

A postfix expression followed by parentheses () containing a possibly empty, comma- separated list of expressions is a function call. The postfix expression denotes the called function. The list of expressions specifies the arguments to the function.

.. _9899_6.5.2.2p4:

.. container:: snum

   :ref:`4 <9899_6.5.2.2p4>`

An argument may be an expression of any object type. In preparing for the call to a function, the arguments are evaluated, and each parameter is assigned the value of the corresponding argument.\ [#9899_note81]_

.. _9899_6.5.2.2p5:

.. container:: snum

   :ref:`5 <9899_6.5.2.2p5>`

If the expression that denotes the called function has type pointer to function returning an object type, the function call expression has the same type as that object type, and has the value determined as specified in :ref:`6.8.6.4 <9899_6.8.6.4>`. Otherwise, the function call has type void. If an attempt is made to modify the result of a function call or to access it after the next sequence point, the behavior is undefined.

.. _9899_6.5.2.2p6:

.. container:: snum

   :ref:`6 <9899_6.5.2.2p6>`

If the expression that denotes the called function has a type that does not include a prototype, the integer promotions are performed on each argument, and arguments that have type float are promoted to double. These are called the default argument promotions. If the number of arguments does not equal the number of parameters, the behavior is undefined. If the function is defined with a type that includes a prototype, and either the prototype ends with an ellipsis (, \.\.\.) or the types of the arguments after promotion are not compatible with the types of the parameters, the behavior is undefined. If the function is defined with a type that does not include a prototype, and the types of the arguments after promotion are not compatible with those of the parameters after promotion, the behavior is undefined, except for the following cases:

-  one promoted type is a signed integer type, the other promoted type is the corresponding unsigned integer type, and the value is representable in both types;
-  both types are pointers to qualified or unqualified versions of a character type or void.

.. _9899_6.5.2.2p7:

.. container:: snum

   :ref:`7 <9899_6.5.2.2p7>`

If the expression that denotes the called function has a type that does include a prototype, the arguments are implicitly converted, as if by assignment, to the types of the corresponding parameters, taking the type of each parameter to be the unqualified version of its declared type. The ellipsis notation in a function prototype declarator causes argument type conversion to stop after the last declared parameter. The default argument promotions are performed on trailing arguments.

.. _9899_6.5.2.2p8:

.. container:: snum

   :ref:`8 <9899_6.5.2.2p8>`

No other conversions are performed implicitly; in particular, the number and types of arguments are not compared with those of the parameters in a function definition that does not include a function prototype declarator.

.. _9899_6.5.2.2p9:

.. container:: snum

   :ref:`9 <9899_6.5.2.2p9>`

If the function is defined with a type that is not compatible with the type (of the expression) pointed to by the expression that denotes the called function, the behavior is undefined.

.. _9899_6.5.2.2p10:

.. container:: snum

   :ref:`10 <9899_6.5.2.2p10>`

The order of evaluation of the function designator, the actual arguments, and subexpressions within the actual arguments is unspecified, but there is a sequence point before the actual call.

.. _9899_6.5.2.2p11:

.. container:: snum

   :ref:`11 <9899_6.5.2.2p11>`

Recursive function calls shall be permitted, both directly and indirectly through any chain of other functions.

.. _9899_6.5.2.2p12:

.. container:: snum

   :ref:`12 <9899_6.5.2.2p12>`

EXAMPLE In the function call

::

    (*pf[f1()]) (f2(), f3() + f4())

the functions f1, f2, f3, and f4 may be called in any order. All side effects have to be completed before the function pointed to by pf[f1()] is called.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.7.5.3`
   - :ref:`9899_6.9.1`
   - :ref:`9899_6.8.6.4`
   - :ref:`9899_6.5.16.1`






.. rubric:: Footnotes

.. [#9899_note80] Most often, this is the result of converting an identifier that is a function designator.
.. [#9899_note81] A function may change the values of its parameters, but these changes cannot affect the values of the arguments. On the other hand, it is possible to pass a pointer to an object, and the function may change the value of the object pointed to. A parameter declared to have array or function type is adjusted to have a pointer type as described in :ref:`6.9.1 <9899_6.9.1>`.
