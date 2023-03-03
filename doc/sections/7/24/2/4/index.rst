.. _9899_7.24.2.4:

7.24.2.4 The swscanf function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.24.2.4p1:

:ref:`1 <9899_7.24.2.4p1>`

::

    #include <wchar.h>
    int swscanf(const wchar_t * restrict s,
         const wchar_t * restrict format, ...);

.. rubric:: Description

.. _9899_7.24.2.4p2:

:ref:`2 <9899_7.24.2.4p2>` The swscanf function is equivalent to fwscanf, except that the argument s specifies a wide string from which the input is to be obtained, rather than from a stream. Reaching the end of the wide string is equivalent to encountering end-of-file for the fwscanf function.

.. rubric:: Returns

.. _9899_7.24.2.4p3:

:ref:`3 <9899_7.24.2.4p3>` The swscanf function returns the value of the macro EOF if an input failure occurs before any conversion. Otherwise, the swscanf function returns the number of input items assigned, which can be fewer than provided for, or even zero, in the event of an early matching failure.

