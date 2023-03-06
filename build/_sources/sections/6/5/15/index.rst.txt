.. _9899_6.5.15:

6.5.15 Conditional operator
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.5.15p1:

.. container:: snum

   :ref:`1 <9899_6.5.15p1>`



.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            conditional-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            logical-OR-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            logical-OR-expression
     
   
         .. container:: syntax-terminal
   
            ?
     
   
         .. container:: syntax-nonterminal
   
            expression
     
   
         .. container:: syntax-terminal
   
            :
     
   
         .. container:: syntax-nonterminal
   
            conditional-expression

.. rubric:: Constraints

.. _9899_6.5.15p2:

.. container:: snum

   :ref:`2 <9899_6.5.15p2>`

The first operand shall have scalar type.

.. _9899_6.5.15p3:

.. container:: snum

   :ref:`3 <9899_6.5.15p3>`

One of the following shall hold for the second and third operands:

-  both operands have arithmetic type;
-  both operands have the same structure or union type;
-  both operands have void type;
-  both operands are pointers to qualified or unqualified versions of compatible types;
-  one operand is a pointer and the other is a null pointer constant; or
-  one operand is a pointer to an object or incomplete type and the other is a pointer to a qualified or unqualified version of void.

.. rubric:: Semantics

.. _9899_6.5.15p4:

.. container:: snum

   :ref:`4 <9899_6.5.15p4>`

The first operand is evaluated; there is a sequence point after its evaluation. The second operand is evaluated only if the first compares unequal to 0; the third operand is evaluated only if the first compares equal to 0; the result is the value of the second or third operand (whichever is evaluated), converted to the type described below.\ [#9899_note95]_ If an attempt is made to modify the result of a conditional operator or to access it after the next sequence point, the behavior is undefined.

.. _9899_6.5.15p5:

.. container:: snum

   :ref:`5 <9899_6.5.15p5>`

If both the second and third operands have arithmetic type, the result type that would be determined by the usual arithmetic conversions, were they applied to those two operands, is the type of the result. If both the operands have structure or union type, the result has that type. If both operands have void type, the result has void type.

.. _9899_6.5.15p6:

.. container:: snum

   :ref:`6 <9899_6.5.15p6>`

If both the second and third operands are pointers or one is a null pointer constant and the other is a pointer, the result type is a pointer to a type qualified with all the type qualifiers of the types pointed-to by both operands. Furthermore, if both operands are pointers to compatible types or to differently qualified versions of compatible types, the result type is a pointer to an appropriately qualified version of the composite type; if one operand is a null pointer constant, the result has the type of the other operand; otherwise, one operand is a pointer to void or a qualified version of void, in which case the result type is a pointer to an appropriately qualified version of void.

.. _9899_6.5.15p7:

.. container:: snum

   :ref:`7 <9899_6.5.15p7>`

EXAMPLE The common type that results when the second and third operands are pointers is determined in two independent stages. The appropriate qualifiers, for example, do not depend on whether the two pointers have compatible types.

.. _9899_6.5.15p8:

.. container:: snum

   :ref:`8 <9899_6.5.15p8>`

Given the declarations

::

    const void *c_vp;
    void *vp;
    const int *c_ip;
    volatile int *v_ip;
    int *ip;
    const char *c_cp;

the third column in the following table is the common type that is the result of a conditional expression in which the first two columns are the second and third operands (in either order):

::

    c_vp     c_ip      const void *
    v_ip     0         volatile int *
    c_ip     v_ip      const volatile int *
    vp       c_cp      const void *
    ip       c_ip      const int *
    vp       ip        void *





.. rubric:: Footnotes

.. [#9899_note95] A conditional expression does not yield an lvalue.
