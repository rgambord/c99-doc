.. _9899_7.23.2.1:

7.23.2.1 The clock function
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.23.2.1p1:

.. container:: snum

   :ref:`1 <9899_7.23.2.1p1>`



::

    #include <time.h>
    clock_t clock(void);

.. rubric:: Description

.. _9899_7.23.2.1p2:

.. container:: snum

   :ref:`2 <9899_7.23.2.1p2>`

The clock function determines the processor time used.

.. rubric:: Returns

.. _9899_7.23.2.1p3:

.. container:: snum

   :ref:`3 <9899_7.23.2.1p3>`

The clock function returns the implementation's best approximation to the processor time used by the program since the beginning of an implementation-defined era related only to the program invocation. To determine the time in seconds, the value returned by the clock function should be divided by the value of the macro CLOCKS_PER_SEC. If the processor time used is not available or its value cannot be represented, the function returns the value (clock_t)(-1).\ [#9899_note275]_





.. rubric:: Footnotes

.. [#9899_note275] In order to measure the time spent in a program, the clock function should be called at the start of the program and its return value subtracted from the value returned by subsequent calls.
