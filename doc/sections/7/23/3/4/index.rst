.. _9899_7.23.3.4:

7.23.3.4 The localtime function
'''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.23.3.4p1:

:ref:`1 <9899_7.23.3.4p1>`

::

    #include <time.h>
    struct tm *localtime(const time_t *timer);

.. rubric:: Description

.. _9899_7.23.3.4p2:

:ref:`2 <9899_7.23.3.4p2>` The localtime function converts the calendar time pointed to by timer into a broken-down time, expressed as local time.

.. rubric:: Returns

.. _9899_7.23.3.4p3:

:ref:`3 <9899_7.23.3.4p3>` The localtime function returns a pointer to the broken-down time, or a null pointer if the specified time cannot be converted to local time.

