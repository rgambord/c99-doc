.. _9899_7.19.10.3:

7.19.10.3 The ferror function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.10.3p1:

:ref:`1 <9899_7.19.10.3p1>`

::

    #include <stdio.h>
    int ferror(FILE *stream);

.. rubric:: Description

.. _9899_7.19.10.3p2:

:ref:`2 <9899_7.19.10.3p2>` The ferror function tests the error indicator for the stream pointed to by stream.

.. rubric:: Returns

.. _9899_7.19.10.3p3:

:ref:`3 <9899_7.19.10.3p3>` The ferror function returns nonzero if and only if the error indicator is set for stream.

