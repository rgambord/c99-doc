.. _9899_6.8.6.2:

6.8.6.2 The continue statement
''''''''''''''''''''''''''''''

.. rubric:: Constraints

.. _9899_6.8.6.2p1:

:ref:`1 <9899_6.8.6.2p1>` A continue statement shall appear only in or as a loop body.

.. rubric:: Semantics

.. _9899_6.8.6.2p2:

:ref:`2 <9899_6.8.6.2p2>` A continue statement causes a jump to the loop-continuation portion of the smallest enclosing iteration statement; that is, to the end of the loop body. More precisely, in each of the statements

::

    while (/* ... */) {                  do {                                 for (/* ... */) {
       /* ... */                            /* ... */                            /* ... */
       continue;                            continue;                            continue;
       /* ... */                            /* ... */                            /* ... */
    contin: ;                            contin: ;                            contin: ;
    }                                    } while (/* ... */);                 }

unless the continue statement shown is in an enclosed iteration statement (in which case it is interpreted within that statement), it is equivalent to goto contin;.\ [#9899_note138]_





.. rubric:: Footnotes

.. [#9899_note138] Following the contin: label is a null statement.
