.. _9899_F.4:

F.4 Floating to integer conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _9899_F.4p1:

.. container:: snum

   :ref:`1 <9899_F.4p1>`

If the floating value is infinite or NaN or if the integral part of the floating value exceeds the range of the integer type, then the "invalid" floating-point exception is raised and the resulting value is unspecified. Whether conversion of non-integer floating values whose integral part is within the range of the integer type raises the "inexact" floating-point exception is unspecified.\ [#9899_note310]_





.. rubric:: Footnotes

.. [#9899_note310] ANSI/IEEE 854, but not IEC 60559 (ANSI/IEEE 754), directly specifies that floating-to-integer conversions raise the "inexact" floating-point exception for non-integer in-range values. In those cases where it matters, library functions can be used to effect such conversions with or without raising the "inexact" floating-point exception. See rint, lrint, llrint, and nearbyint in :ref:`\<math.h> <9899_7.12>`.
