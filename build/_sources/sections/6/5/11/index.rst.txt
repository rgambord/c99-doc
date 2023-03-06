.. _9899_6.5.11:

6.5.11 Bitwise exclusive OR operator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.5.11p1:

.. container:: snum

   :ref:`1 <9899_6.5.11p1>`



.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            exclusive-OR-expression
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            AND-expression
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            exclusive-OR-expression
     
   
         .. container:: syntax-terminal
   
            ^
     
   
         .. container:: syntax-nonterminal
   
            AND-expression

.. rubric:: Constraints

.. _9899_6.5.11p2:

.. container:: snum

   :ref:`2 <9899_6.5.11p2>`

Each of the operands shall have integer type.

.. rubric:: Semantics

.. _9899_6.5.11p3:

.. container:: snum

   :ref:`3 <9899_6.5.11p3>`

The usual arithmetic conversions are performed on the operands.

.. _9899_6.5.11p4:

.. container:: snum

   :ref:`4 <9899_6.5.11p4>`

The result of the ^ operator is the bitwise exclusive OR of the operands (that is, each bit in the result is set if and only if exactly one of the corresponding bits in the converted operands is set).

