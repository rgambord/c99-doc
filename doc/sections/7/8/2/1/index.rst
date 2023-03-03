.. _9899_7.8.2.1:

7.8.2.1 The imaxabs function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.8.2.1p1:

:ref:`1 <9899_7.8.2.1p1>`

::

    #include <inttypes.h>
    intmax_t imaxabs(intmax_t j);

.. rubric:: Description

.. _9899_7.8.2.1p2:

:ref:`2 <9899_7.8.2.1p2>` The imaxabs function computes the absolute value of an integer j. If the result cannot be represented, the behavior is undefined.\ [#9899_note193]_

.. rubric:: Returns

.. _9899_7.8.2.1p3:

:ref:`3 <9899_7.8.2.1p3>` The imaxabs function returns the absolute value.





.. rubric:: Footnotes

.. [#9899_note193] The absolute value of the most negative number cannot be represented in two's complement.
