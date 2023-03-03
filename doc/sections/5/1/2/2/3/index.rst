.. _9899_5.1.2.2.3:

5.1.2.2.3 Program termination
"""""""""""""""""""""""""""""

.. _9899_5.1.2.2.3p1:

:ref:`1 <9899_5.1.2.2.3p1>` If the return type of the main function is a type compatible with int, a return from the initial call to the main function is equivalent to calling the exit function with the value returned by the main function as its argument;\ [#9899_note10]_ reaching the } that terminates the main function returns a value of 0. If the return type is not compatible with int, the termination status returned to the host environment is unspecified.

**Forward references**: definition of terms (:ref:`7.1.1 <9899_7.1.1>`), the exit function (:ref:`7.20.4.3 <9899_7.20.4.3>`).



.. _9899_5.1.2.3:



.. rubric:: Footnotes

.. [#9899_note10] In accordance with :ref:`6.2.4 <9899_6.2.4>`, the lifetimes of objects with automatic storage duration declared in main will have ended in the former case, even where they would not have in the latter.
