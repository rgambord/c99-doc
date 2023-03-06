.. _9899_7.6.1:

7.6.1 The FENV_ACCESS pragma
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Synopsis

.. _9899_7.6.1p1:

.. container:: snum

   :ref:`1 <9899_7.6.1p1>`



::

    #include <fenv.h>
    #pragma STDC FENV_ACCESS on-off-switch

.. rubric:: Description

.. _9899_7.6.1p2:

.. container:: snum

   :ref:`2 <9899_7.6.1p2>`

The FENV_ACCESS pragma provides a means to inform the implementation when a program might access the floating-point environment to test floating-point status flags or run under non-default floating-point control modes.\ [#9899_note184]_ The pragma shall occur either outside external declarations or preceding all explicit declarations and statements inside a compound statement. When outside external declarations, the pragma takes effect from its occurrence until another FENV_ACCESS pragma is encountered, or until the end of the translation unit. When inside a compound statement, the pragma takes effect from its occurrence until another FENV_ACCESS pragma is encountered (including within a nested compound statement), or until the end of the compound statement; at the end of a compound statement the state for the pragma is restored to its condition just before the compound statement. If this pragma is used in any other context, the behavior is undefined. If part of a program tests floating-point status flags, sets floating-point control modes, or runs under non-default mode settings, but was translated with the state for the FENV_ACCESS pragma "off", the behavior is undefined. The default state ("on" or "off") for the pragma is implementation-defined. (When execution passes from a part of the program translated with FENV_ACCESS "off" to a part translated with FENV_ACCESS "on", the state of the floating-point status flags is unspecified and the floating-point control modes have their default settings.)

.. _9899_7.6.1p3:

.. container:: snum

   :ref:`3 <9899_7.6.1p3>`

EXAMPLE

::

    #include <fenv.h>
    void f(double x)
    {
          #pragma STDC FENV_ACCESS ON
          void g(double);
          void h(double);
          /* ... */
          g(x + 1);
          h(x + 1);
          /* ... */
    }

.. _9899_7.6.1p4:

.. container:: snum

   :ref:`4 <9899_7.6.1p4>`

If the function g might depend on status flags set as a side effect of the first x + 1, or if the second x + 1 might depend on control modes set as a side effect of the call to function g, then the program shall contain an appropriately placed invocation of `#pragma` STDC FENV_ACCESS ON.`\ [#9899_note185]_






.. rubric:: Footnotes

.. [#9899_note184] The purpose of the FENV_ACCESS pragma is to allow certain optimizations that could subvert flag tests and mode changes (e.g., global common subexpression elimination, code motion, and constant folding). In general, if the state of FENV_ACCESS is "off", the translator can assume that default modes are in effect and the flags are not tested.
.. [#9899_note185] The side effects impose a temporal ordering that requires two evaluations of x + 1. On the other hand, without the `#pragma` STDC FENV_ACCESS ON pragma, and assuming the default state is "off", just one evaluation of x + 1 would suffice.
