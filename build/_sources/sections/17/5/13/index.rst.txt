.. _9899_J.5.13:

J.5.13 Floating-point status flags
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_J.5.13p1:

.. container:: snum

   :ref:`1 <9899_J.5.13p1>`

If any floating-point status flags are set on normal termination after all calls to functions registered by the atexit function have been made (see :ref:`7.20.4.3 <9899_7.20.4.3>`), the implementation writes some diagnostics indicating the fact to the stderr stream, if it is still open,

