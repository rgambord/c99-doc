.. _9899_7.20.6.1:

7.20.6.1 The abs, labs and llabs functions
''''''''''''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.6.1p1:

:ref:`1 <9899_7.20.6.1p1>`

::

    #include <stdlib.h>
    int abs(int j);
    long int labs(long int j);
    long long int llabs(long long int j);

.. rubric:: Description

.. _9899_7.20.6.1p2:

:ref:`2 <9899_7.20.6.1p2>` The abs, labs, and llabs functions compute the absolute value of an integer j. If the result cannot be represented, the behavior is undefined.\ [#9899_note265]_

.. rubric:: Returns

.. _9899_7.20.6.1p3:

:ref:`3 <9899_7.20.6.1p3>` The abs, labs, and llabs, functions return the absolute value.





.. rubric:: Footnotes

.. [#9899_note265] The absolute value of the most negative number cannot be represented in two's complement.
