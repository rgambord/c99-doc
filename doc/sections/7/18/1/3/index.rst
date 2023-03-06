.. _9899_7.18.1.3:

7.18.1.3 Fastest minimum-width integer types
''''''''''''''''''''''''''''''''''''''''''''

.. _9899_7.18.1.3p1:

.. container:: snum

   :ref:`1 <9899_7.18.1.3p1>`

Each of the following types designates an integer type that is usually fastest\ [#9899_note225]_ to operate with among all integer types that have at least the specified width.

.. _9899_7.18.1.3p2:

.. container:: snum

   :ref:`2 <9899_7.18.1.3p2>`

The typedef name int_fastN_t designates the fastest signed integer type with a width of at least N . The typedef name uint_fastN_t designates the fastest unsigned integer type with a width of at least N .

.. _9899_7.18.1.3p3:

.. container:: snum

   :ref:`3 <9899_7.18.1.3p3>`

The following types are required:

::

    int_fast8_t                                 uint_fast8_t
    int_fast16_t                                uint_fast16_t
    int_fast32_t                                uint_fast32_t
    int_fast64_t                                uint_fast64_t

All other types of this form are optional.





.. rubric:: Footnotes

.. [#9899_note225] The designated type is not guaranteed to be fastest for all purposes; if the implementation has no clear grounds for choosing one type over another, it will simply pick some integer type satisfying the signedness and width requirements.
