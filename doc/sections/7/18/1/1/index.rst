.. _9899_7.18.1.1:

7.18.1.1 Exact-width integer types
''''''''''''''''''''''''''''''''''

.. _9899_7.18.1.1p1:

:ref:`1 <9899_7.18.1.1p1>` The typedef name intN_t designates a signed integer type with width N , no padding bits, and a two's complement representation. Thus, int8_t denotes a signed integer type with a width of exactly 8 bits.

.. _9899_7.18.1.1p2:

:ref:`2 <9899_7.18.1.1p2>` The typedef name uintN_t designates an unsigned integer type with width N . Thus, uint24_t denotes an unsigned integer type with a width of exactly 24 bits.

.. _9899_7.18.1.1p3:

:ref:`3 <9899_7.18.1.1p3>` These types are optional. However, if an implementation provides integer types with widths of 8, 16, 32, or 64 bits, no padding bits, and (for the signed types) that have a two's complement representation, it shall define the corresponding typedef names.

