.. _9899_6.8.3:

6.8.3 Expression and null statements
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.8.3p1:

:ref:`1 <9899_6.8.3p1>`

.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            expression-statement
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            expression
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            ;

.. rubric:: Semantics

.. _9899_6.8.3p2:

:ref:`2 <9899_6.8.3p2>` The expression in an expression statement is evaluated as a void expression for its side effects.\ [#9899_note134]_

.. _9899_6.8.3p3:

:ref:`3 <9899_6.8.3p3>` A null statement (consisting of just a semicolon) performs no operations.

.. _9899_6.8.3p4:

:ref:`4 <9899_6.8.3p4>` EXAMPLE 1 If a function call is evaluated as an expression statement for its side effects only, the discarding of its value may be made explicit by converting the expression to a void expression by means of a cast:

::

    int p(int);
    /* ... */
    (void)p(0);

.. _9899_6.8.3p5:

:ref:`5 <9899_6.8.3p5>` EXAMPLE 2 In the program fragment

::

    char *s;
    /* ... */
    while (*s++ != '\0')
            ;

a null statement is used to supply an empty loop body to the iteration statement.

.. _9899_6.8.3p6:

:ref:`6 <9899_6.8.3p6>` EXAMPLE 3 A null statement may also be used to carry a label just before the closing } of a compound statement.

::

    while (loop1) {
          /* ... */
          while (loop2) {
                  /* ... */
                  if (want_out)
                          goto end_loop1;
                  /* ... */
          }
          /* ... */
    end_loop1: ;
    }

**Forward references**: iteration statements (:ref:`6.8.5 <9899_6.8.5>`).





.. rubric:: Footnotes

.. [#9899_note134] Such as assignments, and function calls which have side effects.
