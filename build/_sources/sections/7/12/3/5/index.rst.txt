.. _9899_7.12.3.5:

7.12.3.5 The isnormal macro
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.3.5p1:

.. container:: snum

   :ref:`1 <9899_7.12.3.5p1>`



::

    #include <math.h>
    int isnormal(real-floating x);

.. rubric:: Description

.. _9899_7.12.3.5p2:

.. container:: snum

   :ref:`2 <9899_7.12.3.5p2>`

The isnormal macro determines whether its argument value is normal (neither zero, subnormal, infinite, nor NaN). First, an argument represented in a format wider than its semantic type is converted to its semantic type. Then determination is based on the type of the argument.

.. rubric:: Returns

.. _9899_7.12.3.5p3:

.. container:: snum

   :ref:`3 <9899_7.12.3.5p3>`

The isnormal macro returns a nonzero value if and only if its argument has a normal value.

