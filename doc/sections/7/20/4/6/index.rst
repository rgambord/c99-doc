.. _9899_7.20.4.6:

7.20.4.6 The system function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.4.6p1:

:ref:`1 <9899_7.20.4.6p1>`

::

    #include <stdlib.h>
    int system(const char *string);

.. rubric:: Description

.. _9899_7.20.4.6p2:

:ref:`2 <9899_7.20.4.6p2>` If string is a null pointer, the system function determines whether the host environment has a command processor. If string is not a null pointer, the system function passes the string pointed to by string to that command processor to be executed in a manner which the implementation shall document; this might then cause the program calling system to behave in a non-conforming manner or to terminate.

.. rubric:: Returns

.. _9899_7.20.4.6p3:

:ref:`3 <9899_7.20.4.6p3>` If the argument is a null pointer, the system function returns nonzero only if a command processor is available. If the argument is not a null pointer, and the system function does return, it returns an implementation-defined value.

