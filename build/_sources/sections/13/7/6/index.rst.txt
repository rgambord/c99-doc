.. _9899_F.7.6:

F.7.6 Changing the environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_F.7.6p1:

.. container:: snum

   :ref:`1 <9899_F.7.6p1>`

Operations defined in :ref:`6.5 <9899_6.5>` and functions and macros defined for the standard libraries change floating-point status flags and control modes just as indicated by their specifications (including conformance to IEC 60559). They do not change flags or modes (so as to be detectable by the user) in any other cases.

.. _9899_F.7.6p2:

.. container:: snum

   :ref:`2 <9899_F.7.6p2>`

If the argument to the feraiseexcept function in :ref:`\<fenv.h> <9899_7.6>` represents IEC 60559 valid coincident floating-point exceptions for atomic operations (namely "overflow" and "inexact", or "underflow" and "inexact"), then "overflow" or "underflow" is raised before "inexact".

