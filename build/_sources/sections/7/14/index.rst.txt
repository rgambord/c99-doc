.. _9899_7.14:

7.14 Signal handling \<signal.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. toctree::
   :maxdepth: 2

   1/index
   2/index


.. _9899_7.14p1:

.. container:: snum

   :ref:`1 <9899_7.14p1>`

The header :ref:`\<signal.h> <9899_7.14>` declares a type and two functions and defines several macros, for handling various signals (conditions that may be reported during program execution).

.. _9899_7.14p2:

.. container:: snum

   :ref:`2 <9899_7.14p2>`

The type defined is

::

    sig_atomic_t

which is the (possibly volatile-qualified) integer type of an object that can be accessed as an atomic entity, even in the presence of asynchronous interrupts.

.. _9899_7.14p3:

.. container:: snum

   :ref:`3 <9899_7.14p3>`

The macros defined are

::

    SIG_DFL
    SIG_ERR
    SIG_IGN

which expand to constant expressions with distinct values that have type compatible with the second argument to, and the return value of, the signal function, and whose values compare unequal to the address of any declarable function; and the following, which expand to positive integer constant expressions with type int and distinct values that are the signal numbers, each corresponding to the specified condition:

.. code-block:: text

    SIGABRT        abnormal termination, such as is initiated by the abort function
    SIGFPE         an erroneous arithmetic operation, such as zero divide or an operation
                   resulting in overflow
    SIGILL         detection of an invalid function image, such as an invalid instruction
    SIGINT         receipt of an interactive attention signal
    SIGSEGV        an invalid access to storage
    SIGTERM        a termination request sent to the program

.. _9899_7.14p4:

.. container:: snum

   :ref:`4 <9899_7.14p4>`

An implementation need not generate any of these signals, except as a result of explicit calls to the raise function. Additional signals and pointers to undeclarable functions, with macro definitions beginning, respectively, with the letters SIG and an uppercase letter or with SIG\_ and an uppercase letter,\ [#9899_note219]_ may also be specified by the implementation. The complete set of signals, their semantics, and their default handling is implementation-defined; all signal numbers shall be positive.





.. rubric:: Footnotes

.. [#9899_note219] See "future library directions" (:ref:`7.26.9 <9899_7.26.9>`). The names of the signal numbers reflect the following terms (respectively): abort, floating-point exception, illegal instruction, interrupt, segmentation violation, and termination.
