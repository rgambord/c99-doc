.. _9899_6.5.1:

6.5.1 Primary expressions
^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.5.1p1:

.. container:: snum

   :ref:`1 <9899_6.5.1p1>`



.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            primary-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            identifier
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            constant
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            string-literal
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            expression
     
   
         .. container:: syntax-terminal
   
            )

.. rubric:: Semantics

.. _9899_6.5.1p2:

.. container:: snum

   :ref:`2 <9899_6.5.1p2>`

An identifier is a primary expression, provided it has been declared as designating an object (in which case it is an lvalue) or a function (in which case it is a function designator).\ [#9899_note79]_

.. _9899_6.5.1p3:

.. container:: snum

   :ref:`3 <9899_6.5.1p3>`

A constant is a primary expression. Its type depends on its form and value, as detailed in :ref:`6.4.4 <9899_6.4.4>`.

.. _9899_6.5.1p4:

.. container:: snum

   :ref:`4 <9899_6.5.1p4>`

A string literal is a primary expression. It is an lvalue with type as detailed in :ref:`6.4.5 <9899_6.4.5>`.

.. _9899_6.5.1p5:

.. container:: snum

   :ref:`5 <9899_6.5.1p5>`

A parenthesized expression is a primary expression. Its type and value are identical to those of the unparenthesized expression. It is an lvalue, a function designator, or a void expression if the unparenthesized expression is, respectively, an lvalue, a function designator, or a void expression.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.7`





.. rubric:: Footnotes

.. [#9899_note79] Thus, an undeclared identifier is a violation of the syntax.
