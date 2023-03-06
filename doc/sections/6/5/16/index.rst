.. _9899_6.5.16:

6.5.16 Assignment operators
^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index


.. rubric:: Syntax

.. _9899_6.5.16p1:

.. container:: snum

   :ref:`1 <9899_6.5.16p1>`



.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            assignment-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            conditional-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            unary-expression
     
   
         .. container:: syntax-nonterminal
   
            assignment-operator
     
   
         .. container:: syntax-nonterminal
   
            assignment-expression
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            assignment-operator
   
         : one of
   
      .. container:: syntax-rule-tbl
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               =
      
            .. container:: syntax-terminal
      
               \*=
      
            .. container:: syntax-terminal
      
               /=
      
            .. container:: syntax-terminal
      
               \%=
      
            .. container:: syntax-terminal
      
               +=
      
            .. container:: syntax-terminal
      
               -=
      
            .. container:: syntax-terminal
      
               <<=
      
            .. container:: syntax-terminal
      
               >>=
      
            .. container:: syntax-terminal
      
               &=
      
            .. container:: syntax-terminal
      
               ^=
      
            .. container:: syntax-terminal
      
               \|=

.. rubric:: Constraints

.. _9899_6.5.16p2:

.. container:: snum

   :ref:`2 <9899_6.5.16p2>`

An assignment operator shall have a modifiable lvalue as its left operand.

.. rubric:: Semantics

.. _9899_6.5.16p3:

.. container:: snum

   :ref:`3 <9899_6.5.16p3>`

An assignment operator stores a value in the object designated by the left operand. An assignment expression has the value of the left operand after the assignment, but is not an lvalue. The type of an assignment expression is the type of the left operand unless the left operand has qualified type, in which case it is the unqualified version of the type of the left operand. The side effect of updating the stored value of the left operand shall occur between the previous and the next sequence point.

.. _9899_6.5.16p4:

.. container:: snum

   :ref:`4 <9899_6.5.16p4>`

The order of evaluation of the operands is unspecified. If an attempt is made to modify the result of an assignment operator or to access it after the next sequence point, the behavior is undefined.

