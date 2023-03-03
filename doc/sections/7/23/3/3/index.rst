.. _9899_7.23.3.3:

7.23.3.3 The gmtime function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.23.3.3p1:

:ref:`1 <9899_7.23.3.3p1>`

::

    #include <time.h>
    struct tm *gmtime(const time_t *timer);

.. rubric:: Description

.. _9899_7.23.3.3p2:

:ref:`2 <9899_7.23.3.3p2>` The gmtime function converts the calendar time pointed to by timer into a broken- down time, expressed as UTC.

.. rubric:: Returns

.. _9899_7.23.3.3p3:

:ref:`3 <9899_7.23.3.3p3>` The gmtime function returns a pointer to the broken-down time, or a null pointer if the specified time cannot be converted to UTC.

