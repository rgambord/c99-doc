.. _9899_7.23.3.2:

7.23.3.2 The ctime function
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.23.3.2p1:

.. container:: snum

   :ref:`1 <9899_7.23.3.2p1>`



::

    #include <time.h>
    char *ctime(const time_t *timer);

.. rubric:: Description

.. _9899_7.23.3.2p2:

.. container:: snum

   :ref:`2 <9899_7.23.3.2p2>`

The ctime function converts the calendar time pointed to by timer to local time in the form of a string. It is equivalent to

::

    asctime(localtime(timer))

.. rubric:: Returns

.. _9899_7.23.3.2p3:

.. container:: snum

   :ref:`3 <9899_7.23.3.2p3>`

The ctime function returns the pointer returned by the asctime function with that broken-down time as argument.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_7.23.3.4`

