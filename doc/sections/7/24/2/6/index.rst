.. _9899_7.24.2.6:

7.24.2.6 The vfwscanf function
''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.24.2.6p1:

:ref:`1 <9899_7.24.2.6p1>`

::

    #include <stdarg.h>
    #include <stdio.h>
    #include <wchar.h>
    int vfwscanf(FILE * restrict stream,
         const wchar_t * restrict format,
         va_list arg);

.. rubric:: Description

.. _9899_7.24.2.6p2:

:ref:`2 <9899_7.24.2.6p2>` The vfwscanf function is equivalent to fwscanf, with the variable argument list replaced by arg, which shall have been initialized by the va_start macro (and possibly subsequent va_arg calls). The vfwscanf function does not invoke the va_end macro.\ [#9899_note291]_

.. rubric:: Returns

.. _9899_7.24.2.6p3:

:ref:`3 <9899_7.24.2.6p3>` The vfwscanf function returns the value of the macro EOF if an input failure occurs before any conversion. Otherwise, the vfwscanf function returns the number of input items assigned, which can be fewer than provided for, or even zero, in the event of an early matching failure.



.. rubric:: Footnotes

.. [#9899_note291] As the functions vfwprintf, vswprintf, vfwscanf, vwprintf, vwscanf, and vswscanf invoke the va_arg macro, the value of arg after the return is indeterminate.
