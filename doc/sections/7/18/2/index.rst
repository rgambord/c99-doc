.. _9899_7.18.2:

7.18.2 Limits of specified-width integer types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index
   4/index
   5/index


.. _9899_7.18.2p1:

:ref:`1 <9899_7.18.2p1>` The following object-like macros\ [#9899_note226]_ specify the minimum and maximum limits of the types declared in :ref:`\<stdint.h> <9899_7.18>`. Each macro name corresponds to a similar type name in :ref:`7.18.1 <9899_7.18.1>`.

.. _9899_7.18.2p2:

:ref:`2 <9899_7.18.2p2>` Each instance of any defined macro shall be replaced by a constant expression suitable for use in #if preprocessing directives, and this expression shall have the same type as would an expression that is an object of the corresponding type converted according to the integer promotions. Its implementation-defined value shall be equal to or greater in magnitude (absolute value) than the corresponding value given below, with the same sign, except where stated to be exactly the given value.





.. rubric:: Footnotes

.. [#9899_note226] C++ implementations should define these macros only when \__STDC_LIMIT_MACROS is defined before :ref:`\<stdint.h> <9899_7.18>` is included.
