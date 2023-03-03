.. _9899_6.8.6.4:

6.8.6.4 The return statement
''''''''''''''''''''''''''''

.. rubric:: Constraints

.. _9899_6.8.6.4p1:

:ref:`1 <9899_6.8.6.4p1>` A return statement with an expression shall not appear in a function whose return type is void. A return statement without an expression shall only appear in a function whose return type is void.

.. rubric:: Semantics

.. _9899_6.8.6.4p2:

:ref:`2 <9899_6.8.6.4p2>` A return statement terminates execution of the current function and returns control to its caller. A function may have any number of return statements.

.. _9899_6.8.6.4p3:

:ref:`3 <9899_6.8.6.4p3>` If a return statement with an expression is executed, the value of the expression is returned to the caller as the value of the function call expression. If the expression has a type different from the return type of the function in which it appears, the value is converted as if by assignment to an object having the return type of the function.\ [#9899_note139]_

.. _9899_6.8.6.4p4:

:ref:`4 <9899_6.8.6.4p4>` EXAMPLE In:

::

    struct s { double i; } f(void);
    union {
          struct {
                int f1;
                struct s f2;
          } u1;
          struct {
                struct s f3;
                int f4;
          } u2;
    } g;
    struct s f(void)
    {
          return g.u1.f2;
    }
    /* ... */
    g.u2.f3 = f();

there is no undefined behavior, although there would be if the assignment were done directly (without using a function call to fetch the value).





.. rubric:: Footnotes

.. [#9899_note139] The return statement is not an assignment. The overlap restriction of subclause :ref:`6.5.16.1 <9899_6.5.16.1>` does not apply to the case of function return. The representation of floating-point values may have wider range or precision and is determined by FLT_EVAL_METHOD. A cast may be used to remove this extra range and precision.
