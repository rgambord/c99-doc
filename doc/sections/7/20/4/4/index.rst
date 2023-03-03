.. _9899_7.20.4.4:

7.20.4.4 The \_Exit function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.4.4p1:

:ref:`1 <9899_7.20.4.4p1>`

::

    #include <stdlib.h>
    void _Exit(int status);

.. rubric:: Description

.. _9899_7.20.4.4p2:

:ref:`2 <9899_7.20.4.4p2>` The \_Exit function causes normal program termination to occur and control to be returned to the host environment. No functions registered by the atexit function or signal handlers registered by the signal function are called. The status returned to the host environment is determined in the same way as for the exit function (:ref:`7.20.4.3 <9899_7.20.4.3>`). Whether open streams with unwritten buffered data are flushed, open streams are closed, or temporary files are removed is implementation-defined.

.. rubric:: Returns

.. _9899_7.20.4.4p3:

:ref:`3 <9899_7.20.4.4p3>` The \_Exit function cannot return to its caller.

