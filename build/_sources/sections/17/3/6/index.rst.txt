.. _9899_J.3.6:

J.3.6 Floating point
^^^^^^^^^^^^^^^^^^^^

.. _9899_J.3.6p1:

.. container:: snum

   :ref:`1 <9899_J.3.6p1>`



-  The accuracy of the floating-point operations and of the library functions in :ref:`\<math.h> <9899_7.12>` and :ref:`\<complex.h> <9899_7.3>` that return floating-point results (:ref:`5.2.4.2.2 <9899_5.2.4.2.2>`).
-  The accuracy of the conversions between floating-point internal representations and string representations performed by the library functions in :ref:`\<stdio.h> <9899_7.19>`, :ref:`\<stdlib.h> <9899_7.20>`, and :ref:`\<wchar.h> <9899_7.24>` (:ref:`5.2.4.2.2 <9899_5.2.4.2.2>`).
-  The rounding behaviors characterized by non-standard values of FLT_ROUNDS (:ref:`5.2.4.2.2 <9899_5.2.4.2.2>`).
-  The evaluation methods characterized by non-standard negative values of FLT_EVAL_METHOD (:ref:`5.2.4.2.2 <9899_5.2.4.2.2>`).
-  The direction of rounding when an integer is converted to a floating-point number that cannot exactly represent the original value (:ref:`6.3.1.4 <9899_6.3.1.4>`).
-  The direction of rounding when a floating-point number is converted to a narrower floating-point number (:ref:`6.3.1.5 <9899_6.3.1.5>`).
-  How the nearest representable value or the larger or smaller representable value immediately adjacent to the nearest representable value is chosen for certain floating constants (:ref:`6.4.4.2 <9899_6.4.4.2>`).
-  Whether and how floating expressions are contracted when not disallowed by the FP_CONTRACT pragma (:ref:`6.5 <9899_6.5>`).
-  The default state for the FENV_ACCESS pragma (:ref:`7.6.1 <9899_7.6.1>`).
-  Additional floating-point exceptions, rounding modes, environments, and classifications, and their macro names (:ref:`7.6 <9899_7.6>`, :ref:`7.12 <9899_7.12>`).
-  The default state for the FP_CONTRACT pragma (:ref:`7.12.2 <9899_7.12.2>`). \*

