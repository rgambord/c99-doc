.. _9899_7.15.1.3:

7.15.1.3 The va_end macro
'''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.15.1.3p1:

.. container:: snum

   :ref:`1 <9899_7.15.1.3p1>`



::

    #include <stdarg.h>
    void va_end(va_list ap);

.. rubric:: Description

.. _9899_7.15.1.3p2:

.. container:: snum

   :ref:`2 <9899_7.15.1.3p2>`

The va_end macro facilitates a normal return from the function whose variable argument list was referred to by the expansion of the va_start macro, or the function containing the expansion of the va_copy macro, that initialized the va_list ap. The va_end macro may modify ap so that it is no longer usable (without being reinitialized by the va_start or va_copy macro). If there is no corresponding invocation of the va_start or va_copy macro, or if the va_end macro is not invoked before the return, the behavior is undefined.

.. rubric:: Returns

.. _9899_7.15.1.3p3:

.. container:: snum

   :ref:`3 <9899_7.15.1.3p3>`

The va_end macro returns no value.

