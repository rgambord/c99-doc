.. _9899_7.18.4:

7.18.4 Macros for integer constants
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index


.. _9899_7.18.4p1:

:ref:`1 <9899_7.18.4p1>` The following function-like macros\ [#9899_note230]_ expand to integer constants suitable for initializing objects that have integer types corresponding to types defined in :ref:`\<stdint.h> <9899_7.18>`. Each macro name corresponds to a similar type name in :ref:`7.18.1.2 <9899_7.18.1.2>` or :ref:`7.18.1.5 <9899_7.18.1.5>`.

.. _9899_7.18.4p2:

:ref:`2 <9899_7.18.4p2>` The argument in any instance of these macros shall be an unsuffixed integer constant (as defined in :ref:`6.4.4.1 <9899_6.4.4.1>`) with a value that does not exceed the limits for the corresponding type.

.. _9899_7.18.4p3:

:ref:`3 <9899_7.18.4p3>` Each invocation of one of these macros shall expand to an integer constant expression suitable for use in #if preprocessing directives. The type of the expression shall have the same type as would an expression of the corresponding type converted according to the integer promotions. The value of the expression shall be that of the argument.





.. rubric:: Footnotes

.. [#9899_note230] C++ implementations should define these macros only when \__STDC_CONSTANT_MACROS is defined before :ref:`\<stdint.h> <9899_7.18>` is included.
