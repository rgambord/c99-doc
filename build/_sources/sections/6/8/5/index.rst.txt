.. _9899_6.8.5:

6.8.5 Iteration statements
^^^^^^^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index


.. rubric:: Syntax

.. _9899_6.8.5p1:

.. container:: snum

   :ref:`1 <9899_6.8.5p1>`



.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            iteration-statement
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            while
     
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            expression
     
   
         .. container:: syntax-terminal
   
            )
     
   
         .. container:: syntax-nonterminal
   
            statement
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            do
     
   
         .. container:: syntax-nonterminal
   
            statement
     
   
         .. container:: syntax-terminal
   
            while
     
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            expression
     
   
         .. container:: syntax-terminal
   
            )
     
   
         .. container:: syntax-terminal
   
            ;
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            for
     
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            expression
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            ;
     
   
         .. container:: syntax-nonterminal
   
            expression
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            ;
     
   
         .. container:: syntax-nonterminal
   
            expression
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            )
     
   
         .. container:: syntax-nonterminal
   
            statement
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            for
     
   
         .. container:: syntax-terminal
   
            (
     
   
         .. container:: syntax-nonterminal
   
            declaration
     
   
         .. container:: syntax-nonterminal
   
            expression
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            ;
     
   
         .. container:: syntax-nonterminal
   
            expression
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            )
     
   
         .. container:: syntax-nonterminal
   
            statement

.. rubric:: Constraints

.. _9899_6.8.5p2:

.. container:: snum

   :ref:`2 <9899_6.8.5p2>`

The controlling expression of an iteration statement shall have scalar type.

.. _9899_6.8.5p3:

.. container:: snum

   :ref:`3 <9899_6.8.5p3>`

The declaration part of a for statement shall only declare identifiers for objects having storage class auto or register.

.. rubric:: Semantics

.. _9899_6.8.5p4:

.. container:: snum

   :ref:`4 <9899_6.8.5p4>`

An iteration statement causes a statement called the loop body to be executed repeatedly until the controlling expression compares equal to 0. The repetition occurs regardless of whether the loop body is entered from the iteration statement or by a jump.\ [#9899_note136]_

.. _9899_6.8.5p5:

.. container:: snum

   :ref:`5 <9899_6.8.5p5>`

An iteration statement is a block whose scope is a strict subset of the scope of its enclosing block. The loop body is also a block whose scope is a strict subset of the scope of the iteration statement.





.. rubric:: Footnotes

.. [#9899_note136] Code jumped over is not executed. In particular, the controlling expression of a for or while statement is not evaluated before entering the loop body, nor is clause-1 of a for statement.
