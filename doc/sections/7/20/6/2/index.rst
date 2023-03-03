.. _9899_7.20.6.2:

7.20.6.2 The div, ldiv, and lldiv functions
'''''''''''''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.6.2p1:

:ref:`1 <9899_7.20.6.2p1>`

::

    #include <stdlib.h>
    div_t div(int numer, int denom);
    ldiv_t ldiv(long int numer, long int denom);
    lldiv_t lldiv(long long int numer, long long int denom);

.. rubric:: Description

.. _9899_7.20.6.2p2:

:ref:`2 <9899_7.20.6.2p2>` The div, ldiv, and lldiv, functions compute numer / denom and numer % denom in a single operation.

.. rubric:: Returns

.. _9899_7.20.6.2p3:

:ref:`3 <9899_7.20.6.2p3>` The div, ldiv, and lldiv functions return a structure of type div_t, ldiv_t, and lldiv_t, respectively, comprising both the quotient and the remainder. The structures shall contain (in either order) the members quot (the quotient) and rem (the remainder), each of which has the same type as the arguments numer and denom. If either part of the result cannot be represented, the behavior is undefined.

