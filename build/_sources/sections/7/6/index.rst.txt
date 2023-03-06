.. _9899_7.6:

7.6 Floating-point environment \<fenv.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index
   4/index


.. _9899_7.6p1:

.. container:: snum

   :ref:`1 <9899_7.6p1>`

The header :ref:`\<fenv.h> <9899_7.6>` declares two types and several macros and functions to provide access to the floating-point environment. The floating-point environment refers collectively to any floating-point status flags and control modes supported by the implementation.\ [#9899_note178]_ A floating-point status flag is a system variable whose value is set (but never cleared) when a floating-point exception is raised, which occurs as a side effect of exceptional floating-point arithmetic to provide auxiliary information.\ [#9899_note179]_ A floating- point control mode is a system variable whose value may be set by the user to affect the subsequent behavior of floating-point arithmetic.

.. _9899_7.6p2:

.. container:: snum

   :ref:`2 <9899_7.6p2>`

Certain programming conventions support the intended model of use for the floating- point environment:[#9899_note180]_

-  a function call does not alter its caller's floating-point control modes, clear its caller's floating-point status flags, nor depend on the state of its caller's floating-point status flags unless the function is so documented;
-  a function call is assumed to require default floating-point control modes, unless its documentation promises otherwise;
-  a function call is assumed to have the potential for raising floating-point exceptions, unless its documentation promises otherwise.

.. _9899_7.6p3:

.. container:: snum

   :ref:`3 <9899_7.6p3>`

The type

::

    fenv_t

represents the entire floating-point environment.

.. _9899_7.6p4:

.. container:: snum

   :ref:`4 <9899_7.6p4>`

The type

::

    fexcept_t

represents the floating-point status flags collectively, including any status the implementation associates with the flags.

.. _9899_7.6p5:

.. container:: snum

   :ref:`5 <9899_7.6p5>`

Each of the macros

::

    FE_DIVBYZERO
    FE_INEXACT
    FE_INVALID
    FE_OVERFLOW
    FE_UNDERFLOW

is defined if and only if the implementation supports the floating-point exception by means of the functions in 7.6.2.\ [#9899_note181]_ Additional implementation-defined floating-point exceptions, with macro definitions beginning with FE\_ and an uppercase letter, may also be specified by the implementation. The defined macros expand to integer constant expressions with values such that bitwise ORs of all combinations of the macros result in distinct values, and furthermore, bitwise ANDs of all combinations of the macros result in zero.\ [#9899_note182]_

.. _9899_7.6p6:

.. container:: snum

   :ref:`6 <9899_7.6p6>`

The macro

::

    FE_ALL_EXCEPT

is simply the bitwise OR of all floating-point exception macros defined by the implementation. If no such macros are defined, FE_ALL_EXCEPT shall be defined as 0.

.. _9899_7.6p7:

.. container:: snum

   :ref:`7 <9899_7.6p7>`

Each of the macros

::

    FE_DOWNWARD
    FE_TONEAREST
    FE_TOWARDZERO
    FE_UPWARD

is defined if and only if the implementation supports getting and setting the represented rounding direction by means of the fegetround and fesetround functions. Additional implementation-defined rounding directions, with macro definitions beginning with FE\_ and an uppercase letter, may also be specified by the implementation. The defined macros expand to integer constant expressions whose values are distinct nonnegative values.\ [#9899_note183]_

.. _9899_7.6p8:

.. container:: snum

   :ref:`8 <9899_7.6p8>`

The macro

::

    FE_DFL_ENV

represents the default floating-point environment -- the one installed at program startup -- and has type "pointer to const-qualified fenv_t". It can be used as an argument to :ref:`\<fenv.h> <9899_7.6>` functions that manage the floating-point environment.

.. _9899_7.6p9:

.. container:: snum

   :ref:`9 <9899_7.6p9>`

Additional implementation-defined environments, with macro definitions beginning with FE\_ and an uppercase letter, and having type "pointer to const-qualified fenv_t", may also be specified by the implementation.










.. rubric:: Footnotes

.. [#9899_note178] This header is designed to support the floating-point exception status flags and directed-rounding control modes required by IEC 60559, and other similar floating-point state information. Also it is designed to facilitate code portability among all systems.
.. [#9899_note179] A floating-point status flag is not an object and can be set more than once within an expression.
.. [#9899_note180] With these conventions, a programmer can safely assume default floating-point control modes (or be unaware of them). The responsibilities associated with accessing the floating-point environment fall on the programmer or program that does so explicitly.
.. [#9899_note181] The implementation supports an exception if there are circumstances where a call to at least one of the functions in :ref:`7.6.2 <9899_7.6.2>`, using the macro as the appropriate argument, will succeed. It is not necessary for all the functions to succeed all the time.
.. [#9899_note182] The macros should be distinct powers of two.
.. [#9899_note183] Even though the rounding direction macros may expand to constants corresponding to the values of FLT_ROUNDS, they are not required to do so.
