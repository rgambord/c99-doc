.. _9899_F.6:

F.6 Contracted expressions
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _9899_F.6p1:

.. container:: snum

   :ref:`1 <9899_F.6p1>`

A contracted expression treats infinities, NaNs, signed zeros, subnormals, and the rounding directions in a manner consistent with the basic arithmetic operations covered by IEC 60559.

.. rubric:: Recommended practice

.. _9899_F.6p2:

.. container:: snum

   :ref:`2 <9899_F.6p2>`

A contracted expression should raise floating-point exceptions in a manner generally consistent with the basic arithmetic operations. A contracted expression should deliver the same value as its uncontracted counterpart, else should be correctly rounded (once).

