.. _9899_7.6.2.1:

7.6.2.1 The feclearexcept function
''''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.6.2.1p1:

:ref:`1 <9899_7.6.2.1p1>`

::

    #include <fenv.h>
    int feclearexcept(int excepts);

.. rubric:: Description

.. _9899_7.6.2.1p2:

:ref:`2 <9899_7.6.2.1p2>` The feclearexcept function attempts to clear the supported floating-point exceptions represented by its argument.

.. rubric:: Returns

.. _9899_7.6.2.1p3:

:ref:`3 <9899_7.6.2.1p3>` The feclearexcept function returns zero if the excepts argument is zero or if all the specified exceptions were successfully cleared. Otherwise, it returns a nonzero value.

