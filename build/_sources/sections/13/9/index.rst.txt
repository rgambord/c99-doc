.. _9899_F.9:

F.9 Mathematics \<math.h>
~~~~~~~~~~~~~~~~~~~~~~~~~


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index
   4/index
   5/index
   6/index
   7/index
   8/index
   9/index
   10/index


.. _9899_F.9p1:

.. container:: snum

   :ref:`1 <9899_F.9p1>`

This subclause contains specifications of :ref:`\<math.h> <9899_7.12>` facilities that are particularly suited for IEC 60559 implementations.

.. _9899_F.9p2:

.. container:: snum

   :ref:`2 <9899_F.9p2>`

The Standard C macro HUGE_VAL and its float and long double analogs, HUGE_VALF and HUGE_VALL, expand to expressions whose values are positive infinities.

.. _9899_F.9p3:

.. container:: snum

   :ref:`3 <9899_F.9p3>`

Special cases for functions in :ref:`\<math.h> <9899_7.12>` are covered directly or indirectly by IEC 60559. The functions that IEC 60559 specifies directly are identified in :ref:`F.3 <9899_F.3>`. The other functions in :ref:`\<math.h> <9899_7.12>` treat infinities, NaNs, signed zeros, subnormals, and (provided the state of the FENV_ACCESS pragma is "on") the floating-point status flags in a manner consistent with the basic arithmetic operations covered by IEC 60559.

.. _9899_F.9p4:

.. container:: snum

   :ref:`4 <9899_F.9p4>`

The expression math_errhandling & MATH_ERREXCEPT shall evaluate to a nonzero value.

.. _9899_F.9p5:

.. container:: snum

   :ref:`5 <9899_F.9p5>`

The "invalid" and "divide-by-zero" floating-point exceptions are raised as specified in subsequent subclauses of this annex.

.. _9899_F.9p6:

.. container:: snum

   :ref:`6 <9899_F.9p6>`

The "overflow" floating-point exception is raised whenever an infinity -- or, because of rounding direction, a maximal-magnitude finite number -- is returned in lieu of a value whose magnitude is too large.

.. _9899_F.9p7:

.. container:: snum

   :ref:`7 <9899_F.9p7>`

The "underflow" floating-point exception is raised whenever a result is tiny (essentially subnormal or zero) and suffers loss of accuracy.\ [#9899_note320]_

.. _9899_F.9p8:

.. container:: snum

   :ref:`8 <9899_F.9p8>`

Whether or when library functions raise the "inexact" floating-point exception is unspecified, unless explicitly specified otherwise.

.. _9899_F.9p9:

.. container:: snum

   :ref:`9 <9899_F.9p9>`

Whether or when library functions raise an undeserved "underflow" floating-point exception is unspecified.\ [#9899_note321]_ Otherwise, as implied by :ref:`F.7.6 <9899_F.7.6>`, the :ref:`\<math.h> <9899_7.12>` functions do not raise spurious floating-point exceptions (detectable by the user), other than the "inexact" floating-point exception.

.. _9899_F.9p10:

.. container:: snum

   :ref:`10 <9899_F.9p10>`

Whether the functions honor the rounding direction mode is implementation-defined, unless explicitly specified otherwise.

.. _9899_F.9p11:

.. container:: snum

   :ref:`11 <9899_F.9p11>`

Functions with a NaN argument return a NaN result and raise no floating-point exception, except where stated otherwise.

.. _9899_F.9p12:

.. container:: snum

   :ref:`12 <9899_F.9p12>`

The specifications in the following subclauses append to the definitions in :ref:`\<math.h> <9899_7.12>`. For families of functions, the specifications apply to all of the functions even though only the principal function is shown. Unless otherwise specified, where the symbol ''(+-)'' occurs in both an argument and the result, the result has the same sign as the argument.

.. rubric:: Recommended practice

.. _9899_F.9p13:

.. container:: snum

   :ref:`13 <9899_F.9p13>`

If a function with one or more NaN arguments returns a NaN result, the result should be the same as one of the NaN arguments (after possible type conversion), except perhaps for the sign.






.. rubric:: Footnotes

.. [#9899_note320] IEC 60559 allows different definitions of underflow. They all result in the same values, but differ on when the floating-point exception is raised.
.. [#9899_note321] It is intended that undeserved "underflow" and "inexact" floating-point exceptions are raised only if avoiding them would be too costly.
