.. _9899_H.2.2:

H.2.2 Integer types
^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index


.. _9899_H.2.2p1:

:ref:`1 <9899_H.2.2p1>` The signed C integer types int, long int, long long int, and the corresponding unsigned types are compatible with LIA-1. If an implementation adds support for the LIA-1 exceptional values ''integer_overflow'' and ''undefined'', then those types are LIA-1 conformant types. C's unsigned integer types are ''modulo'' in the LIA-1 sense in that overflows or out-of-bounds results silently wrap. An implementation that defines signed integer types as also being modulo need not detect integer overflow, in which case, only integer divide-by-zero need be detected.

.. _9899_H.2.2p2:

:ref:`2 <9899_H.2.2p2>` The parameters for the integer data types can be accessed by the following:

.. code-block:: text

    maxint        INT_MAX, LONG_MAX, LLONG_MAX, UINT_MAX, ULONG_MAX,
                  ULLONG_MAX
    minint        INT_MIN, LONG_MIN, LLONG_MIN

.. _9899_H.2.2p3:

:ref:`3 <9899_H.2.2p3>` The parameter ''bounded'' is always true, and is not provided. The parameter ''minint'' is always 0 for the unsigned types, and is not provided for those types.

