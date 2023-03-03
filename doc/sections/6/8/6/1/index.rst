.. _9899_6.8.6.1:

6.8.6.1 The goto statement
''''''''''''''''''''''''''

.. rubric:: Constraints

.. _9899_6.8.6.1p1:

:ref:`1 <9899_6.8.6.1p1>` The identifier in a goto statement shall name a label located somewhere in the enclosing function. A goto statement shall not jump from outside the scope of an identifier having a variably modified type to inside the scope of that identifier.

.. rubric:: Semantics

.. _9899_6.8.6.1p2:

:ref:`2 <9899_6.8.6.1p2>` A goto statement causes an unconditional jump to the statement prefixed by the named label in the enclosing function.

.. _9899_6.8.6.1p3:

:ref:`3 <9899_6.8.6.1p3>` EXAMPLE 1 It is sometimes convenient to jump into the middle of a complicated set of statements. The following outline presents one possible approach to a problem based on these three assumptions:

#. The general initialization code accesses objects only visible to the current function.

#. The general initialization code is too large to warrant duplication.

#. The code to determine the next operation is at the head of the loop. (To allow it to be reached by continue statements, for example.)

::

    /* ... */
    goto first_time;
    for (;;) {
            // determine next operation
            /* ... */
            if (need to reinitialize) {
                    // reinitialize-only code
                    /* ... */
            first_time:
                    // general initialization code
                    /* ... */
                    continue;
            }
            // handle other operations
            /* ... */
    }

.. _9899_6.8.6.1p4:

:ref:`4 <9899_6.8.6.1p4>` EXAMPLE 2 A goto statement is not allowed to jump past any declarations of objects with variably modified types. A jump within the scope, however, is permitted.

::

    goto lab3;                         // invalid: going INTO scope of VLA.
    {
          double a[n];
          a[j] = 4.4;
    lab3:
          a[j] = 3.3;
          goto lab4;                   // valid: going WITHIN scope of VLA.
          a[j] = 5.5;
    lab4:
          a[j] = 6.6;
    }
    goto lab4;                         // invalid: going INTO scope of VLA.

