.. _9899_7.23.3.1:

7.23.3.1 The asctime function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.23.3.1p1:

:ref:`1 <9899_7.23.3.1p1>`

::

    #include <time.h>
    char *asctime(const struct tm *timeptr);

.. rubric:: Description

.. _9899_7.23.3.1p2:

:ref:`2 <9899_7.23.3.1p2>` The asctime function converts the broken-down time in the structure pointed to by timeptr into a string in the form

.. code-block:: text

    Sun Sep 16 01:03:52 1973\n\0

using the equivalent of the following algorithm.

::

    char *asctime(const struct tm *timeptr)
    {
         static const char wday_name[7][3] = {
              "Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"
         };
         static const char mon_name[12][3] = {
              "Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
         };
         static char result[26];
           sprintf(result, "%.3s %.3s%3d %.2d:%.2d:%.2d %d\n",
                wday_name[timeptr->tm_wday],
                mon_name[timeptr->tm_mon],
                timeptr->tm_mday, timeptr->tm_hour,
                timeptr->tm_min, timeptr->tm_sec,
                1900 + timeptr->tm_year);
           return result;
    }

.. rubric:: Returns

.. _9899_7.23.3.1p3:

:ref:`3 <9899_7.23.3.1p3>` The asctime function returns a pointer to the string.

