.. _9899_7.12.3.6:

7.12.3.6 The signbit macro
''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.3.6p1:

.. container:: snum

   :ref:`1 <9899_7.12.3.6p1>`



::

    #include <math.h>
    int signbit(real-floating x);

.. rubric:: Description

.. _9899_7.12.3.6p2:

.. container:: snum

   :ref:`2 <9899_7.12.3.6p2>`

The signbit macro determines whether the sign of its argument value is negative.\ [#9899_note207]_

.. rubric:: Returns

.. _9899_7.12.3.6p3:

.. container:: snum

   :ref:`3 <9899_7.12.3.6p3>`

The signbit macro returns a nonzero value if and only if the sign of its argument value is negative.



.. _9899_7.12.4:



.. rubric:: Footnotes

.. [#9899_note207] The signbit macro reports the sign of all values, including infinities, zeros, and NaNs. If zero is unsigned, it is treated as positive.
