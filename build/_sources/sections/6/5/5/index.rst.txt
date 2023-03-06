.. _9899_6.5.5:

6.5.5 Multiplicative operators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.5.5p1:

.. container:: snum

   :ref:`1 <9899_6.5.5p1>`



.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            multiplicative-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            cast-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            multiplicative-expression
     
   
         .. container:: syntax-terminal
   
            \*
     
   
         .. container:: syntax-nonterminal
   
            cast-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            multiplicative-expression
     
   
         .. container:: syntax-terminal
   
            /
     
   
         .. container:: syntax-nonterminal
   
            cast-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            multiplicative-expression
     
   
         .. container:: syntax-terminal
   
            \%
     
   
         .. container:: syntax-nonterminal
   
            cast-expression

.. rubric:: Constraints

.. _9899_6.5.5p2:

.. container:: snum

   :ref:`2 <9899_6.5.5p2>`

Each of the operands shall have arithmetic type. The operands of the % operator shall have integer type.

.. rubric:: Semantics

.. _9899_6.5.5p3:

.. container:: snum

   :ref:`3 <9899_6.5.5p3>`

The usual arithmetic conversions are performed on the operands.

.. _9899_6.5.5p4:

.. container:: snum

   :ref:`4 <9899_6.5.5p4>`

The result of the binary \* operator is the product of the operands.

.. _9899_6.5.5p5:

.. container:: snum

   :ref:`5 <9899_6.5.5p5>`

The result of the / operator is the quotient from the division of the first operand by the second; the result of the % operator is the remainder. In both operations, if the value of the second operand is zero, the behavior is undefined.

.. _9899_6.5.5p6:

.. container:: snum

   :ref:`6 <9899_6.5.5p6>`

When integers are divided, the result of the / operator is the algebraic quotient with any fractional part discarded.\ [#9899_note90]_ If the quotient a/b is representable, the expression (a/b)*b + a%b shall equal a.





.. rubric:: Footnotes

.. [#9899_note90] This is often called "truncation toward zero".
