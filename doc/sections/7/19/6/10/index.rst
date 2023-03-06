.. _9899_7.19.6.10:

7.19.6.10 The vprintf function
''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.6.10p1:

.. container:: snum

   :ref:`1 <9899_7.19.6.10p1>`



::

    #include <stdarg.h>
    #include <stdio.h>
    int vprintf(const char * restrict format,
         va_list arg);

.. rubric:: Description

.. _9899_7.19.6.10p2:

.. container:: snum

   :ref:`2 <9899_7.19.6.10p2>`

The vprintf function is equivalent to printf, with the variable argument list replaced by arg, which shall have been initialized by the va_start macro (and possibly subsequent va_arg calls). The vprintf function does not invoke the va_end macro.\ [#9899_note254]_

.. rubric:: Returns

.. _9899_7.19.6.10p3:

.. container:: snum

   :ref:`3 <9899_7.19.6.10p3>`

The vprintf function returns the number of characters transmitted, or a negative value if an output or encoding error occurred.



.. rubric:: Footnotes

.. [#9899_note254] As the functions vfprintf, vfscanf, vprintf, vscanf, vsnprintf, vsprintf, and vsscanf invoke the va_arg macro, the value of arg after the return is indeterminate.
