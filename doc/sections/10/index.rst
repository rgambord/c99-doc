.. _9899_C:

Annex C
-------

(informative)

Sequence points

.. _9899_Cp1:

:ref:`1 <9899_Cp1>` The following are the sequence points described in :ref:`5.1.2.3 <9899_5.1.2.3>`:

-  The call to a function, after the arguments have been evaluated (:ref:`6.5.2.2 <9899_6.5.2.2>`).
-  The end of the first operand of the following operators: logical AND && (:ref:`6.5.13 <9899_6.5.13>`); logical OR \|\| (:ref:`6.5.14 <9899_6.5.14>`); conditional ? (:ref:`6.5.15 <9899_6.5.15>`); comma , (:ref:`6.5.17 <9899_6.5.17>`).
-  The end of a full declarator: declarators (:ref:`6.7.5 <9899_6.7.5>`);
-  The end of a full expression: an initializer (:ref:`6.7.8 <9899_6.7.8>`); the expression in an expression statement (:ref:`6.8.3 <9899_6.8.3>`); the controlling expression of a selection statement (if or switch) (:ref:`6.8.4 <9899_6.8.4>`); the controlling expression of a while or do statement (:ref:`6.8.5 <9899_6.8.5>`); each of the expressions of a for statement (:ref:`6.8.5.3 <9899_6.8.5.3>`); the expression in a return statement (:ref:`6.8.6.4 <9899_6.8.6.4>`).
-  Immediately before a library function returns (:ref:`7.1.4 <9899_7.1.4>`).
-  After the actions associated with each formatted input/output function conversion specifier (:ref:`7.19.6 <9899_7.19.6>`, :ref:`7.24.2 <9899_7.24.2>`).
-  Immediately before and immediately after each call to a comparison function, and also between any call to a comparison function and any movement of the objects passed as arguments to that call (:ref:`7.20.5 <9899_7.20.5>`).

