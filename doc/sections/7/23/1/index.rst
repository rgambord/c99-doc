.. _9899_7.23.1:

7.23.1 Components of time
^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_7.23.1p1:

.. container:: snum

   :ref:`1 <9899_7.23.1p1>`

The header :ref:`\<time.h> <9899_7.23>` defines two macros, and declares several types and functions for manipulating time. Many functions deal with a calendar time that represents the current date (according to the Gregorian calendar) and time. Some functions deal with local time, which is the calendar time expressed for some specific time zone, and with Daylight Saving Time, which is a temporary change in the algorithm for determining local time. The local time zone and Daylight Saving Time are implementation-defined.

.. _9899_7.23.1p2:

.. container:: snum

   :ref:`2 <9899_7.23.1p2>`

The macros defined are NULL (described in :ref:`7.17 <9899_7.17>`); and

::

    CLOCKS_PER_SEC

which expands to an expression with type clock_t (described below) that is the number per second of the value returned by the clock function.

.. _9899_7.23.1p3:

.. container:: snum

   :ref:`3 <9899_7.23.1p3>`

The types declared are size_t (described in :ref:`7.17 <9899_7.17>`);

::

    clock_t

and

::

    time_t

which are arithmetic types capable of representing times; and

::

    struct tm

which holds the components of a calendar time, called the broken-down time.

.. _9899_7.23.1p4:

.. container:: snum

   :ref:`4 <9899_7.23.1p4>`

The range and precision of times representable in clock_t and time_t are implementation-defined. The tm structure shall contain at least the following members, in any order. The semantics of the members and their normal ranges are expressed in the comments.\ [#9899_note274]_

::

    int    tm_sec;           //   seconds after the minute -- [0, 60]
    int    tm_min;           //   minutes after the hour -- [0, 59]
    int    tm_hour;          //   hours since midnight -- [0, 23]
    int    tm_mday;          //   day of the month -- [1, 31]
    int    tm_mon;           //   months since January -- [0, 11]
    int    tm_year;          //   years since 1900
    int    tm_wday;          //   days since Sunday -- [0, 6]
    int    tm_yday;          //   days since January 1 -- [0, 365]
    int    tm_isdst;         //   Daylight Saving Time flag

The value of tm_isdst is positive if Daylight Saving Time is in effect, zero if Daylight Saving Time is not in effect, and negative if the information is not available.





.. rubric:: Footnotes

.. [#9899_note274] The range [0, 60] for tm_sec allows for a positive leap second.
