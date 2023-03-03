.. _9899_7.8.2.2:

7.8.2.2 The imaxdiv function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.8.2.2p1:

:ref:`1 <9899_7.8.2.2p1>`

::

    #include <inttypes.h>
    imaxdiv_t imaxdiv(intmax_t numer, intmax_t denom);

.. rubric:: Description

.. _9899_7.8.2.2p2:

:ref:`2 <9899_7.8.2.2p2>` The imaxdiv function computes numer / denom and numer % denom in a single operation.

.. rubric:: Returns

.. _9899_7.8.2.2p3:

:ref:`3 <9899_7.8.2.2p3>` The imaxdiv function returns a structure of type imaxdiv_t comprising both the quotient and the remainder. The structure shall contain (in either order) the members quot (the quotient) and rem (the remainder), each of which has type intmax_t. If either part of the result cannot be represented, the behavior is undefined.

