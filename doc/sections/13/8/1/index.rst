.. _9899_F.8.1:

F.8.1 Global transformations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_F.8.1p1:

:ref:`1 <9899_F.8.1p1>` Floating-point arithmetic operations and external function calls may entail side effects which optimization shall honor, at least where the state of the FENV_ACCESS pragma is ''on''. The flags and modes in the floating-point environment may be regarded as global variables; floating-point operations (+, \*, etc.) implicitly read the modes and write the flags.

.. _9899_F.8.1p2:

:ref:`2 <9899_F.8.1p2>` Concern about side effects may inhibit code motion and removal of seemingly useless code. For example, in

::

    #include <fenv.h>
    #pragma STDC FENV_ACCESS ON
    void f(double x)
    {
         /* ... */
         for (i = 0; i < n; i++) x + 1;
         /* ... */
    }

x + 1 might raise floating-point exceptions, so cannot be removed. And since the loop body might not execute (maybe 0 >= n), x + 1 cannot be moved out of the loop. (Of course these optimizations are valid if the implementation can rule out the nettlesome cases.)

.. _9899_F.8.1p3:

:ref:`3 <9899_F.8.1p3>` This specification does not require support for trap handlers that maintain information about the order or count of floating-point exceptions. Therefore, between function calls, floating-point exceptions need not be precise: the actual order and number of occurrences of floating-point exceptions (> 1) may vary from what the source code expresses. Thus, the preceding loop could be treated as

::

    if (0 < n) x + 1;

