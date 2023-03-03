.. _9899_7.24.2.10:

7.24.2.10 The vwscanf function
''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.24.2.10p1:

:ref:`1 <9899_7.24.2.10p1>`

::

    #include <stdarg.h>
    #include <wchar.h>
    int vwscanf(const wchar_t * restrict format,
         va_list arg);

.. rubric:: Description

.. _9899_7.24.2.10p2:

:ref:`2 <9899_7.24.2.10p2>` The vwscanf function is equivalent to wscanf, with the variable argument list replaced by arg, which shall have been initialized by the va_start macro (and possibly subsequent va_arg calls). The vwscanf function does not invoke the va_end macro.\ [#9899_note291]_

.. rubric:: Returns

.. _9899_7.24.2.10p3:

:ref:`3 <9899_7.24.2.10p3>` The vwscanf function returns the value of the macro EOF if an input failure occurs before any conversion. Otherwise, the vwscanf function returns the number of input items assigned, which can be fewer than provided for, or even zero, in the event of an early matching failure.



.. rubric:: Footnotes

.. [#9899_note291] As the functions vfwprintf, vswprintf, vfwscanf, vwprintf, vwscanf, and vswscanf invoke the va_arg macro, the value of arg after the return is indeterminate.
