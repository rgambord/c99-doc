.. _9899_7.18.1.2:

7.18.1.2 Minimum-width integer types
''''''''''''''''''''''''''''''''''''

.. _9899_7.18.1.2p1:

:ref:`1 <9899_7.18.1.2p1>` The typedef name int_leastN_t designates a signed integer type with a width of at least N , such that no signed integer type with lesser size has at least the specified width. Thus, int_least32_t denotes a signed integer type with a width of at least 32 bits.

.. _9899_7.18.1.2p2:

:ref:`2 <9899_7.18.1.2p2>` The typedef name uint_leastN_t designates an unsigned integer type with a width of at least N , such that no unsigned integer type with lesser size has at least the specified width. Thus, uint_least16_t denotes an unsigned integer type with a width of at least 16 bits.

.. _9899_7.18.1.2p3:

:ref:`3 <9899_7.18.1.2p3>` The following types are required:

::

    int_least8_t                                      uint_least8_t
    int_least16_t                                     uint_least16_t
    int_least32_t                                     uint_least32_t
    int_least64_t                                     uint_least64_t

All other types of this form are optional.

