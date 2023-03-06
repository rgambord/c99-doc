.. _9899_6.8.1:

6.8.1 Labeled statements
^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.8.1p1:

.. container:: snum

   :ref:`1 <9899_6.8.1p1>`



.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            labeled-statement
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            identifier
     
   
         .. container:: syntax-terminal
   
            :
     
   
         .. container:: syntax-nonterminal
   
            statement
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            case
     
   
         .. container:: syntax-nonterminal
   
            constant-expression
     
   
         .. container:: syntax-terminal
   
            :
     
   
         .. container:: syntax-nonterminal
   
            statement
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            default
     
   
         .. container:: syntax-terminal
   
            :
     
   
         .. container:: syntax-nonterminal
   
            statement

.. rubric:: Constraints

.. _9899_6.8.1p2:

.. container:: snum

   :ref:`2 <9899_6.8.1p2>`

A case or default label shall appear only in a switch statement. Further constraints on such labels are discussed under the switch statement.

.. _9899_6.8.1p3:

.. container:: snum

   :ref:`3 <9899_6.8.1p3>`

Label names shall be unique within a function.

.. rubric:: Semantics

.. _9899_6.8.1p4:

.. container:: snum

   :ref:`4 <9899_6.8.1p4>`

Any statement may be preceded by a prefix that declares an identifier as a label name. Labels in themselves do not alter the flow of control, which continues unimpeded across them.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.8.6.1`
   - :ref:`9899_6.8.4.2`

