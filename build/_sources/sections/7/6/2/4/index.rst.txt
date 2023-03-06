.. _9899_7.6.2.4:

7.6.2.4 The fesetexceptflag function
''''''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.6.2.4p1:

.. container:: snum

   :ref:`1 <9899_7.6.2.4p1>`



::

    #include <fenv.h>
    int fesetexceptflag(const fexcept_t *flagp,
         int excepts);

.. rubric:: Description

.. _9899_7.6.2.4p2:

.. container:: snum

   :ref:`2 <9899_7.6.2.4p2>`

The fesetexceptflag function attempts to set the floating-point status flags indicated by the argument excepts to the states stored in the object pointed to by flagp. The value of \*flagp shall have been set by a previous call to fegetexceptflag whose second argument represented at least those floating-point exceptions represented by the argument excepts. This function does not raise floating- point exceptions, but only sets the state of the flags.

.. rubric:: Returns

.. _9899_7.6.2.4p3:

.. container:: snum

   :ref:`3 <9899_7.6.2.4p3>`

The fesetexceptflag function returns zero if the excepts argument is zero or if all the specified flags were successfully set to the appropriate state. Otherwise, it returns a nonzero value.

