.. _9899_7.6.4.3:

7.6.4.3 The fesetenv function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.6.4.3p1:

:ref:`1 <9899_7.6.4.3p1>`

::

    #include <fenv.h>
    int fesetenv(const fenv_t *envp);

.. rubric:: Description

.. _9899_7.6.4.3p2:

:ref:`2 <9899_7.6.4.3p2>` The fesetenv function attempts to establish the floating-point environment represented by the object pointed to by envp. The argument envp shall point to an object set by a call to fegetenv or feholdexcept, or equal a floating-point environment macro. Note that fesetenv merely installs the state of the floating-point status flags represented through its argument, and does not raise these floating-point exceptions.

.. rubric:: Returns

.. _9899_7.6.4.3p3:

:ref:`3 <9899_7.6.4.3p3>` The fesetenv function returns zero if the environment was successfully established. Otherwise, it returns a nonzero value.

