.. _9899_7.6.4.2:

7.6.4.2 The feholdexcept function
'''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.6.4.2p1:

:ref:`1 <9899_7.6.4.2p1>`

::

    #include <fenv.h>
    int feholdexcept(fenv_t *envp);

.. rubric:: Description

.. _9899_7.6.4.2p2:

:ref:`2 <9899_7.6.4.2p2>` The feholdexcept function saves the current floating-point environment in the object pointed to by envp, clears the floating-point status flags, and then installs a non-stop (continue on floating-point exceptions) mode, if available, for all floating-point exceptions.\ [#9899_note189]_

.. rubric:: Returns

.. _9899_7.6.4.2p3:

:ref:`3 <9899_7.6.4.2p3>` The feholdexcept function returns zero if and only if non-stop floating-point exception handling was successfully installed.





.. rubric:: Footnotes

.. [#9899_note189] IEC 60559 systems have a default non-stop mode, and typically at least one other mode for trap handling or aborting; if the system provides only the non-stop mode then installing it is trivial. For such systems, the feholdexcept function can be used in conjunction with the feupdateenv function to write routines that hide spurious floating-point exceptions from their callers.
