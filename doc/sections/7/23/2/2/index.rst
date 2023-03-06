.. _9899_7.23.2.2:

7.23.2.2 The difftime function
''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.23.2.2p1:

.. container:: snum

   :ref:`1 <9899_7.23.2.2p1>`



::

    #include <time.h>
    double difftime(time_t time1, time_t time0);

.. rubric:: Description

.. _9899_7.23.2.2p2:

.. container:: snum

   :ref:`2 <9899_7.23.2.2p2>`

The difftime function computes the difference between two calendar times: time1 - time0.

.. rubric:: Returns

.. _9899_7.23.2.2p3:

.. container:: snum

   :ref:`3 <9899_7.23.2.2p3>`

The difftime function returns the difference expressed in seconds as a double.

