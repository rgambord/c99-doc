.. _9899_7.12.3.4:

7.12.3.4 The isnan macro
''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.3.4p1:

.. container:: snum

   :ref:`1 <9899_7.12.3.4p1>`



::

    #include <math.h>
    int isnan(real-floating x);

.. rubric:: Description

.. _9899_7.12.3.4p2:

.. container:: snum

   :ref:`2 <9899_7.12.3.4p2>`

The isnan macro determines whether its argument value is a NaN. First, an argument represented in a format wider than its semantic type is converted to its semantic type. Then determination is based on the type of the argument.\ [#9899_note206]_

.. rubric:: Returns

.. _9899_7.12.3.4p3:

.. container:: snum

   :ref:`3 <9899_7.12.3.4p3>`

The isnan macro returns a nonzero value if and only if its argument has a NaN value.





.. rubric:: Footnotes

.. [#9899_note206] For the isnan macro, the type for determination does not matter unless the implementation supports NaNs in the evaluation type but not in the semantic type.
