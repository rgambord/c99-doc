.. _9899_7.18.4.1:

7.18.4.1 Macros for minimum-width integer constants
'''''''''''''''''''''''''''''''''''''''''''''''''''

.. _9899_7.18.4.1p1:

:ref:`1 <9899_7.18.4.1p1>` The macro INTN_C(value) shall expand to an integer constant expression corresponding to the type int_leastN_t. The macro UINTN_C(value) shall expand to an integer constant expression corresponding to the type uint_leastN_t. For example, if uint_least64_t is a name for the type unsigned long long int, then UINT64_C(0x123) might expand to the integer constant 0x123ULL.

