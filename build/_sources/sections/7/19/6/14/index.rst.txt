.. _9899_7.19.6.14:

7.19.6.14 The vsscanf function
''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.6.14p1:

.. container:: snum

   :ref:`1 <9899_7.19.6.14p1>`



::

    #include <stdarg.h>
    #include <stdio.h>
    int vsscanf(const char * restrict s,
         const char * restrict format,
         va_list arg);

.. rubric:: Description

.. _9899_7.19.6.14p2:

.. container:: snum

   :ref:`2 <9899_7.19.6.14p2>`

The vsscanf function is equivalent to sscanf, with the variable argument list replaced by arg, which shall have been initialized by the va_start macro (and possibly subsequent va_arg calls). The vsscanf function does not invoke the va_end macro.\ [#9899_note254]_

.. rubric:: Returns

.. _9899_7.19.6.14p3:

.. container:: snum

   :ref:`3 <9899_7.19.6.14p3>`

The vsscanf function returns the value of the macro EOF if an input failure occurs before any conversion. Otherwise, the vsscanf function returns the number of input items assigned, which can be fewer than provided for, or even zero, in the event of an early matching failure.



.. rubric:: Footnotes

.. [#9899_note254] As the functions vfprintf, vfscanf, vprintf, vscanf, vsnprintf, vsprintf, and vsscanf invoke the va_arg macro, the value of arg after the return is indeterminate.
