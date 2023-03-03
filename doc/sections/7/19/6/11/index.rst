.. _9899_7.19.6.11:

7.19.6.11 The vscanf function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.6.11p1:

:ref:`1 <9899_7.19.6.11p1>`

::

    #include <stdarg.h>
    #include <stdio.h>
    int vscanf(const char * restrict format,
         va_list arg);

.. rubric:: Description

.. _9899_7.19.6.11p2:

:ref:`2 <9899_7.19.6.11p2>` The vscanf function is equivalent to scanf, with the variable argument list replaced by arg, which shall have been initialized by the va_start macro (and possibly subsequent va_arg calls). The vscanf function does not invoke the va_end macro.\ [#9899_note254]_

.. rubric:: Returns

.. _9899_7.19.6.11p3:

:ref:`3 <9899_7.19.6.11p3>` The vscanf function returns the value of the macro EOF if an input failure occurs before any conversion. Otherwise, the vscanf function returns the number of input items assigned, which can be fewer than provided for, or even zero, in the event of an early matching failure.



.. rubric:: Footnotes

.. [#9899_note254] As the functions vfprintf, vfscanf, vprintf, vscanf, vsnprintf, vsprintf, and vsscanf invoke the va_arg macro, the value of arg after the return is indeterminate.
