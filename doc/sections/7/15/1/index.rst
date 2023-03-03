.. _9899_7.15.1:

7.15.1 Variable argument list access macros
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index
   4/index


.. _9899_7.15.1p1:

:ref:`1 <9899_7.15.1p1>` The va_start and va_arg macros described in this subclause shall be implemented as macros, not functions. It is unspecified whether va_copy and va_end are macros or identifiers declared with external linkage. If a macro definition is suppressed in order to access an actual function, or a program defines an external identifier with the same name, the behavior is undefined. Each invocation of the va_start and va_copy macros shall be matched by a corresponding invocation of the va_end macro in the same function.

