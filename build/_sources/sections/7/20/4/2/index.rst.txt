.. _9899_7.20.4.2:

7.20.4.2 The atexit function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.4.2p1:

.. container:: snum

   :ref:`1 <9899_7.20.4.2p1>`



::

    #include <stdlib.h>
    int atexit(void (*func)(void));

.. rubric:: Description

.. _9899_7.20.4.2p2:

.. container:: snum

   :ref:`2 <9899_7.20.4.2p2>`

The atexit function registers the function pointed to by func, to be called without arguments at normal program termination.

.. rubric:: Environmental limits

.. _9899_7.20.4.2p3:

.. container:: snum

   :ref:`3 <9899_7.20.4.2p3>`

The implementation shall support the registration of at least 32 functions.

.. rubric:: Returns

.. _9899_7.20.4.2p4:

.. container:: snum

   :ref:`4 <9899_7.20.4.2p4>`

The atexit function returns zero if the registration succeeds, nonzero if it fails.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_7.20.4.3`

