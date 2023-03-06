.. _9899_7.12.3.2:

7.12.3.2 The isfinite macro
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.3.2p1:

.. container:: snum

   :ref:`1 <9899_7.12.3.2p1>`



::

    #include <math.h>
    int isfinite(real-floating x);

.. rubric:: Description

.. _9899_7.12.3.2p2:

.. container:: snum

   :ref:`2 <9899_7.12.3.2p2>`

The isfinite macro determines whether its argument has a finite value (zero, subnormal, or normal, and not infinite or NaN). First, an argument represented in a format wider than its semantic type is converted to its semantic type. Then determination is based on the type of the argument.

.. rubric:: Returns

.. _9899_7.12.3.2p3:

.. container:: snum

   :ref:`3 <9899_7.12.3.2p3>`

The isfinite macro returns a nonzero value if and only if its argument has a finite value.

