.. _9899_7.12.2:

7.12.2 The FP_CONTRACT pragma
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Synopsis

.. _9899_7.12.2p1:

.. container:: snum

   :ref:`1 <9899_7.12.2p1>`



::

    #include <math.h>
    #pragma STDC FP_CONTRACT on-off-switch

.. rubric:: Description

.. _9899_7.12.2p2:

.. container:: snum

   :ref:`2 <9899_7.12.2p2>`

The FP_CONTRACT pragma can be used to allow (if the state is "on") or disallow (if the state is "off") the implementation to contract expressions (:ref:`6.5 <9899_6.5>`). Each pragma can occur either outside external declarations or preceding all explicit declarations and statements inside a compound statement. When outside external declarations, the pragma takes effect from its occurrence until another FP_CONTRACT pragma is encountered, or until the end of the translation unit. When inside a compound statement, the pragma takes effect from its occurrence until another FP_CONTRACT pragma is encountered (including within a nested compound statement), or until the end of the compound statement; at the end of a compound statement the state for the pragma is restored to its condition just before the compound statement. If this pragma is used in any other context, the behavior is undefined. The default state ("on" or "off") for the pragma is implementation-defined.

