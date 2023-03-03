.. _9899_7.6.2.3:

7.6.2.3 The feraiseexcept function
''''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.6.2.3p1:

:ref:`1 <9899_7.6.2.3p1>`

::

    #include <fenv.h>
    int feraiseexcept(int excepts);

.. rubric:: Description

.. _9899_7.6.2.3p2:

:ref:`2 <9899_7.6.2.3p2>` The feraiseexcept function attempts to raise the supported floating-point exceptions represented by its argument.\ [#9899_note187]_ The order in which these floating-point exceptions are raised is unspecified, except as stated in :ref:`F.7.6 <9899_F.7.6>`. Whether the feraiseexcept function additionally raises the ''inexact'' floating-point exception whenever it raises the ''overflow'' or ''underflow'' floating-point exception is implementation-defined.

.. rubric:: Returns

.. _9899_7.6.2.3p3:

:ref:`3 <9899_7.6.2.3p3>` The feraiseexcept function returns zero if the excepts argument is zero or if all the specified exceptions were successfully raised. Otherwise, it returns a nonzero value.





.. rubric:: Footnotes

.. [#9899_note187] The effect is intended to be similar to that of floating-point exceptions raised by arithmetic operations. Hence, enabled traps for floating-point exceptions raised by this function are taken. The specification in :ref:`F.7.6 <9899_F.7.6>` is in the same spirit.
