.. _9899_6.8:

6.8 Statements and blocks
~~~~~~~~~~~~~~~~~~~~~~~~~


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index
   4/index
   5/index
   6/index


.. rubric:: Syntax

.. _9899_6.8p1:

.. container:: snum

   :ref:`1 <9899_6.8p1>`



.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            statement
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            labeled-statement
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            compound-statement
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            expression-statement
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            selection-statement
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            iteration-statement
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            jump-statement

.. rubric:: Semantics

.. _9899_6.8p2:

.. container:: snum

   :ref:`2 <9899_6.8p2>`

A statement specifies an action to be performed. Except as indicated, statements are executed in sequence.

.. _9899_6.8p3:

.. container:: snum

   :ref:`3 <9899_6.8p3>`

A block allows a set of declarations and statements to be grouped into one syntactic unit. The initializers of objects that have automatic storage duration, and the variable length array declarators of ordinary identifiers with block scope, are evaluated and the values are stored in the objects (including storing an indeterminate value in objects without an initializer) each time the declaration is reached in the order of execution, as if it were a statement, and within each declaration in the order that declarators appear.

.. _9899_6.8p4:

.. container:: snum

   :ref:`4 <9899_6.8p4>`

A full expression is an expression that is not part of another expression or of a declarator. Each of the following is a full expression: an initializer; the expression in an expression statement; the controlling expression of a selection statement (if or switch); the controlling expression of a while or do statement; each of the (optional) expressions of a for statement; the (optional) expression in a return statement. The end of a full expression is a sequence point.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.8.3`
   - :ref:`9899_6.8.4`
   - :ref:`9899_6.8.5`
   - :ref:`9899_6.8.6.4`

