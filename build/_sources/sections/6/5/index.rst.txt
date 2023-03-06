.. _9899_6.5:

6.5 Expressions
~~~~~~~~~~~~~~~


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
   9/index
   10/index
   11/index
   12/index
   13/index
   14/index
   15/index
   16/index
   17/index


.. _9899_6.5p1:

.. container:: snum

   :ref:`1 <9899_6.5p1>`

An expression is a sequence of operators and operands that specifies computation of a value, or that designates an object or a function, or that generates side effects, or that performs a combination thereof.

.. _9899_6.5p2:

.. container:: snum

   :ref:`2 <9899_6.5p2>`

Between the previous and next sequence point an object shall have its stored value modified at most once by the evaluation of an expression.\ [#9899_note72]_ Furthermore, the prior value shall be read only to determine the value to be stored.\ [#9899_note73]_

.. _9899_6.5p3:

.. container:: snum

   :ref:`3 <9899_6.5p3>`

The grouping of operators and operands is indicated by the syntax.\ [#9899_note74]_ Except as specified later (for the function-call (), &&, \|\|, ?:, and comma operators), the order of evaluation of subexpressions and the order in which side effects take place are both unspecified.

.. _9899_6.5p4:

.. container:: snum

   :ref:`4 <9899_6.5p4>`

Some operators (the unary operator ~, and the binary operators <<, >>, &, ^, and \|, collectively described as bitwise operators) are required to have operands that have integer type. These operators yield values that depend on the internal representations of integers, and have implementation-defined and undefined aspects for signed types.

.. _9899_6.5p5:

.. container:: snum

   :ref:`5 <9899_6.5p5>`

If an exceptional condition occurs during the evaluation of an expression (that is, if the result is not mathematically defined or not in the range of representable values for its type), the behavior is undefined.

.. _9899_6.5p6:

.. container:: snum

   :ref:`6 <9899_6.5p6>`

The effective type of an object for an access to its stored value is the declared type of the object, if any.\ [#9899_note75]_ If a value is stored into an object having no declared type through an lvalue having a type that is not a character type, then the type of the lvalue becomes the effective type of the object for that access and for subsequent accesses that do not modify the stored value. If a value is copied into an object having no declared type using memcpy or memmove, or is copied as an array of character type, then the effective type of the modified object for that access and for subsequent accesses that do not modify the value is the effective type of the object from which the value is copied, if it has one. For all other accesses to an object having no declared type, the effective type of the object is simply the type of the lvalue used for the access.

.. _9899_6.5p7:

.. container:: snum

   :ref:`7 <9899_6.5p7>`

An object shall have its stored value accessed only by an lvalue expression that has one of the following types:[#9899_note76]_

-  a type compatible with the effective type of the object,
-  a qualified version of a type compatible with the effective type of the object,
-  a type that is the signed or unsigned type corresponding to the effective type of the object,
-  a type that is the signed or unsigned type corresponding to a qualified version of the effective type of the object,
-  an aggregate or union type that includes one of the aforementioned types among its members (including, recursively, a member of a subaggregate or contained union), or
-  a character type.

.. _9899_6.5p8:

.. container:: snum

   :ref:`8 <9899_6.5p8>`

A floating expression may be contracted, that is, evaluated as though it were an atomic operation, thereby omitting rounding errors implied by the source code and the expression evaluation method.\ [#9899_note77]_ The FP_CONTRACT pragma in :ref:`\<math.h> <9899_7.12>` provides a way to disallow contracted expressions. Otherwise, whether and how expressions are contracted is implementation-defined.\ [#9899_note78]_

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_7.12.2`
   - :ref:`9899_7.21.2`




::

    i = ++i + 1;
    a[i++] = i;

while allowing

::

    i = i + 1;
    a[i] = i;








.. rubric:: Footnotes

.. [#9899_note72] A floating-point status flag is not an object and can be set more than once within an expression.
.. [#9899_note73] This paragraph renders undefined statement expressions such as
.. [#9899_note74] The syntax specifies the precedence of operators in the evaluation of an expression, which is the same as the order of the major subclauses of this subclause, highest precedence first. Thus, for example, the expressions allowed as the operands of the binary + operator (:ref:`6.5.6 <9899_6.5.6>`) are those expressions defined in :ref:`6.5.1 <9899_6.5.1>` through :ref:`6.5.6 <9899_6.5.6>`. The exceptions are cast expressions (:ref:`6.5.4 <9899_6.5.4>`) as operands of unary operators (:ref:`6.5.3 <9899_6.5.3>`), and an operand contained between any of the following pairs of operators: grouping parentheses () (:ref:`6.5.1 <9899_6.5.1>`), subscripting brackets [] (:ref:`6.5.2.1 <9899_6.5.2.1>`), function-call parentheses () (:ref:`6.5.2.2 <9899_6.5.2.2>`), and the conditional operator ?: (:ref:`6.5.15 <9899_6.5.15>`). Within each major subclause, the operators have the same precedence. Left- or right-associativity is indicated in each subclause by the syntax for the expressions discussed therein.
.. [#9899_note75] Allocated objects have no declared type.
.. [#9899_note76] The intent of this list is to specify those circumstances in which an object may or may not be aliased.
.. [#9899_note77] A contracted expression might also omit the raising of floating-point exceptions.
.. [#9899_note78] This license is specifically intended to allow implementations to exploit fast machine instructions that combine multiple C operators. As contractions potentially undermine predictability, and can even decrease accuracy for containing expressions, their use needs to be well-defined and clearly documented.
