.. _9899_6.5.4:

6.5.4 Cast operators
^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.5.4p1:

:ref:`1 <9899_6.5.4p1>`

.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            cast-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            unary-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            type-name
     
   
         .. container:: syntax-terminal
   
            )
     
   
         .. container:: syntax-nonterminal
   
            cast-expression

.. rubric:: Constraints

.. _9899_6.5.4p2:

:ref:`2 <9899_6.5.4p2>` Unless the type name specifies a void type, the type name shall specify qualified or unqualified scalar type and the operand shall have scalar type.

.. _9899_6.5.4p3:

:ref:`3 <9899_6.5.4p3>` Conversions that involve pointers, other than where permitted by the constraints of :ref:`6.5.16.1 <9899_6.5.16.1>`, shall be specified by means of an explicit cast.

.. rubric:: Semantics

.. _9899_6.5.4p4:

:ref:`4 <9899_6.5.4p4>` Preceding an expression by a parenthesized type name converts the value of the expression to the named type. This construction is called a cast.\ [#9899_note89]_ A cast that specifies no conversion has no effect on the type or value of an expression.

.. _9899_6.5.4p5:

:ref:`5 <9899_6.5.4p5>` If the value of the expression is represented with greater precision or range than required by the type named by the cast (:ref:`6.3.1.8 <9899_6.3.1.8>`), then the cast specifies a conversion even if the type of the expression is the same as the named type.

**Forward references**: equality operators (:ref:`6.5.9 <9899_6.5.9>`), function declarators (including prototypes) (:ref:`6.7.5.3 <9899_6.7.5.3>`), simple assignment (:ref:`6.5.16.1 <9899_6.5.16.1>`), type names (:ref:`6.7.6 <9899_6.7.6>`).





.. rubric:: Footnotes

.. [#9899_note89] A cast does not yield an lvalue. Thus, a cast to a qualified type has the same effect as a cast to the unqualified version of the type.
