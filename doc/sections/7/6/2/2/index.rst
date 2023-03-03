.. _9899_7.6.2.2:

7.6.2.2 The fegetexceptflag function
''''''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.6.2.2p1:

:ref:`1 <9899_7.6.2.2p1>`

::

    #include <fenv.h>
    int fegetexceptflag(fexcept_t *flagp,
         int excepts);

.. rubric:: Description

.. _9899_7.6.2.2p2:

:ref:`2 <9899_7.6.2.2p2>` The fegetexceptflag function attempts to store an implementation-defined representation of the states of the floating-point status flags indicated by the argument excepts in the object pointed to by the argument flagp.

.. rubric:: Returns

.. _9899_7.6.2.2p3:

:ref:`3 <9899_7.6.2.2p3>` The fegetexceptflag function returns zero if the representation was successfully stored. Otherwise, it returns a nonzero value.

