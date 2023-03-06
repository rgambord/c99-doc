.. _9899_7.23.2.4:

7.23.2.4 The time function
''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.23.2.4p1:

.. container:: snum

   :ref:`1 <9899_7.23.2.4p1>`



::

    #include <time.h>
    time_t time(time_t *timer);

.. rubric:: Description

.. _9899_7.23.2.4p2:

.. container:: snum

   :ref:`2 <9899_7.23.2.4p2>`

The time function determines the current calendar time. The encoding of the value is unspecified.

.. rubric:: Returns

.. _9899_7.23.2.4p3:

.. container:: snum

   :ref:`3 <9899_7.23.2.4p3>`

The time function returns the implementation's best approximation to the current calendar time. The value (time_t)(-1) is returned if the calendar time is not available. If timer is not a null pointer, the return value is also assigned to the object it points to.

