.. _9899_7.6.4.1:

7.6.4.1 The fegetenv function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.6.4.1p1:

.. container:: snum

   :ref:`1 <9899_7.6.4.1p1>`



::

    #include <fenv.h>
    int fegetenv(fenv_t *envp);

.. rubric:: Description

.. _9899_7.6.4.1p2:

.. container:: snum

   :ref:`2 <9899_7.6.4.1p2>`

The fegetenv function attempts to store the current floating-point environment in the object pointed to by envp.

.. rubric:: Returns

.. _9899_7.6.4.1p3:

.. container:: snum

   :ref:`3 <9899_7.6.4.1p3>`

The fegetenv function returns zero if the environment was successfully stored. Otherwise, it returns a nonzero value.

