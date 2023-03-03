.. _9899_7.20.4.3:

7.20.4.3 The exit function
''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.4.3p1:

:ref:`1 <9899_7.20.4.3p1>`

::

    #include <stdlib.h>
    void exit(int status);

.. rubric:: Description

.. _9899_7.20.4.3p2:

:ref:`2 <9899_7.20.4.3p2>` The exit function causes normal program termination to occur. If more than one call to the exit function is executed by a program, the behavior is undefined.

.. _9899_7.20.4.3p3:

:ref:`3 <9899_7.20.4.3p3>` First, all functions registered by the atexit function are called, in the reverse order of their registration,\ [#9899_note262]_ except that a function is called after any previously registered functions that had already been called at the time it was registered. If, during the call to any such function, a call to the longjmp function is made that would terminate the call to the registered function, the behavior is undefined.

.. _9899_7.20.4.3p4:

:ref:`4 <9899_7.20.4.3p4>` Next, all open streams with unwritten buffered data are flushed, all open streams are closed, and all files created by the tmpfile function are removed.

.. _9899_7.20.4.3p5:

:ref:`5 <9899_7.20.4.3p5>` Finally, control is returned to the host environment. If the value of status is zero or EXIT_SUCCESS, an implementation-defined form of the status successful termination is returned. If the value of status is EXIT_FAILURE, an implementation-defined form of the status unsuccessful termination is returned. Otherwise the status returned is implementation-defined.

.. rubric:: Returns

.. _9899_7.20.4.3p6:

:ref:`6 <9899_7.20.4.3p6>` The exit function cannot return to its caller.





.. rubric:: Footnotes

.. [#9899_note262] Each function is called as many times as it was registered, and in the correct order with respect to other registered functions.
