.. _9899_7.14.2.1:

7.14.2.1 The raise function
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.14.2.1p1:

.. container:: snum

   :ref:`1 <9899_7.14.2.1p1>`



::

    #include <signal.h>
    int raise(int sig);

.. rubric:: Description

.. _9899_7.14.2.1p2:

.. container:: snum

   :ref:`2 <9899_7.14.2.1p2>`

The raise function carries out the actions described in :ref:`7.14.1.1 <9899_7.14.1.1>` for the signal sig. If a signal handler is called, the raise function shall not return until after the signal handler does.

.. rubric:: Returns

.. _9899_7.14.2.1p3:

.. container:: snum

   :ref:`3 <9899_7.14.2.1p3>`

The raise function returns zero if successful, nonzero if unsuccessful.

