.. _9899_6.6:

6.6 Constant expressions
~~~~~~~~~~~~~~~~~~~~~~~~

.. rubric:: Syntax

.. _9899_6.6p1:

.. container:: snum

   :ref:`1 <9899_6.6p1>`



.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            constant-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            conditional-expression

.. rubric:: Description

.. _9899_6.6p2:

.. container:: snum

   :ref:`2 <9899_6.6p2>`

A constant expression can be evaluated during translation rather than runtime, and accordingly may be used in any place that a constant may be.

.. rubric:: Constraints

.. _9899_6.6p3:

.. container:: snum

   :ref:`3 <9899_6.6p3>`

Constant expressions shall not contain assignment, increment, decrement, function-call, or comma operators, except when they are contained within a subexpression that is not evaluated.\ [#9899_note98]_

.. _9899_6.6p4:

.. container:: snum

   :ref:`4 <9899_6.6p4>`

Each constant expression shall evaluate to a constant that is in the range of representable values for its type.

.. rubric:: Semantics

.. _9899_6.6p5:

.. container:: snum

   :ref:`5 <9899_6.6p5>`

An expression that evaluates to a constant is required in several contexts. If a floating expression is evaluated in the translation environment, the arithmetic precision and range shall be at least as great as if the expression were being evaluated in the execution environment.

.. _9899_6.6p6:

.. container:: snum

   :ref:`6 <9899_6.6p6>`

An integer constant expression\ [#9899_note99]_ shall have integer type and shall only have operands that are integer constants, enumeration constants, character constants, sizeof expressions whose results are integer constants, and floating constants that are the immediate operands of casts. Cast operators in an integer constant expression shall only convert arithmetic types to integer types, except as part of an operand to the sizeof operator.

.. _9899_6.6p7:

.. container:: snum

   :ref:`7 <9899_6.6p7>`

More latitude is permitted for constant expressions in initializers. Such a constant expression shall be, or evaluate to, one of the following:

-  an arithmetic constant expression,
-  a null pointer constant,
-  an address constant, or
-  an address constant for an object type plus or minus an integer constant expression.

.. _9899_6.6p8:

.. container:: snum

   :ref:`8 <9899_6.6p8>`

An arithmetic constant expression shall have arithmetic type and shall only have operands that are integer constants, floating constants, enumeration constants, character constants, and sizeof expressions. Cast operators in an arithmetic constant expression shall only convert arithmetic types to arithmetic types, except as part of an operand to a sizeof operator whose result is an integer constant.

.. _9899_6.6p9:

.. container:: snum

   :ref:`9 <9899_6.6p9>`

An address constant is a null pointer, a pointer to an lvalue designating an object of static storage duration, or a pointer to a function designator; it shall be created explicitly using the unary & operator or an integer constant cast to pointer type, or implicitly by the use of an expression of array or function type. The array-subscript [] and member-access . and -> operators, the address & and indirection \* unary operators, and pointer casts may be used in the creation of an address constant, but the value of an object shall not be accessed by use of these operators.

.. _9899_6.6p10:

.. container:: snum

   :ref:`10 <9899_6.6p10>`

An implementation may accept other forms of constant expressions.

.. _9899_6.6p11:

.. container:: snum

   :ref:`11 <9899_6.6p11>`

The semantic rules for the evaluation of a constant expression are the same as for nonconstant expressions.\ [#9899_note100]_

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.7.5.2`
   - :ref:`9899_6.7.8`





::

    static int i = 2 || 1 / 0;

the expression is a valid integer constant expression with value one.



.. rubric:: Footnotes

.. [#9899_note98] The operand of a sizeof operator is usually not evaluated (:ref:`6.5.3.4 <9899_6.5.3.4>`).
.. [#9899_note99] An integer constant expression is used to specify the size of a bit-field member of a structure, the value of an enumeration constant, the size of an array, or the value of a case constant. Further constraints that apply to the integer constant expressions used in conditional-inclusion preprocessing directives are discussed in :ref:`6.10.1 <9899_6.10.1>`.
.. [#9899_note100] Thus, in the following initialization,
