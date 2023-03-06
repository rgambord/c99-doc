.. _9899_F.7.1:

F.7.1 Environment management
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_F.7.1p1:

.. container:: snum

   :ref:`1 <9899_F.7.1p1>`

IEC 60559 requires that floating-point operations implicitly raise floating-point exception status flags, and that rounding control modes can be set explicitly to affect result values of floating-point operations. When the state for the FENV_ACCESS pragma (defined in :ref:`\<fenv.h> <9899_7.6>`) is "on", these changes to the floating-point state are treated as side effects which respect sequence points.\ [#9899_note313]_





.. rubric:: Footnotes

.. [#9899_note313] If the state for the FENV_ACCESS pragma is "off", the implementation is free to assume the floating- point control modes will be the default ones and the floating-point status flags will not be tested, which allows certain optimizations (see :ref:`F.8 <9899_F.8>`).
