.. _9899_7.12.3.3:

7.12.3.3 The isinf macro
''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.3.3p1:

.. container:: snum

   :ref:`1 <9899_7.12.3.3p1>`



::

    #include <math.h>
    int isinf(real-floating x);

.. rubric:: Description

.. _9899_7.12.3.3p2:

.. container:: snum

   :ref:`2 <9899_7.12.3.3p2>`

The isinf macro determines whether its argument value is an infinity (positive or negative). First, an argument represented in a format wider than its semantic type is converted to its semantic type. Then determination is based on the type of the argument.

.. rubric:: Returns

.. _9899_7.12.3.3p3:

.. container:: snum

   :ref:`3 <9899_7.12.3.3p3>`

The isinf macro returns a nonzero value if and only if its argument has an infinite value.

