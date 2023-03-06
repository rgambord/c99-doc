.. _9899_7.15.1.2:

7.15.1.2 The va_copy macro
''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.15.1.2p1:

.. container:: snum

   :ref:`1 <9899_7.15.1.2p1>`



::

    #include <stdarg.h>
    void va_copy(va_list dest, va_list src);

.. rubric:: Description

.. _9899_7.15.1.2p2:

.. container:: snum

   :ref:`2 <9899_7.15.1.2p2>`

The va_copy macro initializes dest as a copy of src, as if the va_start macro had been applied to dest followed by the same sequence of uses of the va_arg macro as had previously been used to reach the present state of src. Neither the va_copy nor va_start macro shall be invoked to reinitialize dest without an intervening invocation of the va_end macro for the same dest.

.. rubric:: Returns

.. _9899_7.15.1.2p3:

.. container:: snum

   :ref:`3 <9899_7.15.1.2p3>`

The va_copy macro returns no value.

