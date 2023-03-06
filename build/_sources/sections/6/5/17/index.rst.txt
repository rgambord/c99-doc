.. _9899_6.5.17:

6.5.17 Comma operator
^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.5.17p1:

.. container:: snum

   :ref:`1 <9899_6.5.17p1>`



.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            assignment-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            expression
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-nonterminal
   
            assignment-expression

.. rubric:: Semantics

.. _9899_6.5.17p2:

.. container:: snum

   :ref:`2 <9899_6.5.17p2>`

The left operand of a comma operator is evaluated as a void expression; there is a sequence point after its evaluation. Then the right operand is evaluated; the result has its type and value.\ [#9899_note97]_ If an attempt is made to modify the result of a comma operator or to access it after the next sequence point, the behavior is undefined.

.. _9899_6.5.17p3:

.. container:: snum

   :ref:`3 <9899_6.5.17p3>`

EXAMPLE As indicated by the syntax, the comma operator (as described in this subclause) cannot appear in contexts where a comma is used to separate items in a list (such as arguments to functions or lists of initializers). On the other hand, it can be used within a parenthesized expression or within the second expression of a conditional operator in such contexts. In the function call

::

    f(a, (t=3, t+2), c)

the function has three arguments, the second of which has the value 5.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.7.8`





.. rubric:: Footnotes

.. [#9899_note97] A comma operator does not yield an lvalue.
