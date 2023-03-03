.. _9899_H.3.1.1:

H.3.1.1 Indicators
''''''''''''''''''

.. _9899_H.3.1.1p1:

:ref:`1 <9899_H.3.1.1p1>` C's :ref:`\<fenv.h> <9899_7.6>` status flags are compatible with the LIA-1 indicators.

.. _9899_H.3.1.1p2:

:ref:`2 <9899_H.3.1.1p2>` The following mapping is for floating-point types:

.. code-block:: text

    undefined                FE_INVALID, FE_DIVBYZERO
    floating_overflow         FE_OVERFLOW
    underflow                FE_UNDERFLOW

.. _9899_H.3.1.1p3:

:ref:`3 <9899_H.3.1.1p3>` The floating-point indicator interrogation and manipulation operations are:

.. code-block:: text

    set_indicators          feraiseexcept(i)
    clear_indicators        feclearexcept(i)
    test_indicators         fetestexcept(i)
    current_indicators      fetestexcept(FE_ALL_EXCEPT)

where i is an expression of type int representing a subset of the LIA-1 indicators.

.. _9899_H.3.1.1p4:

:ref:`4 <9899_H.3.1.1p4>` C allows an implementation to provide the following LIA-1 required behavior: at program termination if any indicator is set the implementation shall send an unambiguous and ''hard to ignore'' message (see LIA-1 subclause 6.1.2)

.. _9899_H.3.1.1p5:

:ref:`5 <9899_H.3.1.1p5>` LIA-1 does not make the distinction between floating-point and integer for ''undefined''. This documentation makes that distinction because :ref:`\<fenv.h> <9899_7.6>` covers only the floating- point indicators.

