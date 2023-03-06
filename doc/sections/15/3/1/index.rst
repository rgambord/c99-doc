.. _9899_H.3.1:

H.3.1 Notification alternatives
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index


.. _9899_H.3.1p1:

.. container:: snum

   :ref:`1 <9899_H.3.1p1>`

LIA-1 requires at least the following two alternatives for handling of notifications: setting indicators or trap-and-terminate. LIA-1 allows a third alternative: trap-and- resume.

.. _9899_H.3.1p2:

.. container:: snum

   :ref:`2 <9899_H.3.1p2>`

An implementation need only support a given notification alternative for the entire program. An implementation may support the ability to switch between notification alternatives during execution, but is not required to do so. An implementation can provide separate selection for each kind of notification, but this is not required.

.. _9899_H.3.1p3:

.. container:: snum

   :ref:`3 <9899_H.3.1p3>`

C allows an implementation to provide notification. C's SIGFPE (for traps) and FE_INVALID, FE_DIVBYZERO, FE_OVERFLOW, FE_UNDERFLOW (for indicators) can provide LIA-1 notification.

.. _9899_H.3.1p4:

.. container:: snum

   :ref:`4 <9899_H.3.1p4>`

C's signal handlers are compatible with LIA-1. Default handling of SIGFPE can provide trap-and-terminate behavior, except for those LIA-1 operations implemented by math library function calls. User-provided signal handlers for SIGFPE allow for trap- and-resume behavior with the same constraint.

