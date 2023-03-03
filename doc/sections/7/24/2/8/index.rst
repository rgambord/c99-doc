.. _9899_7.24.2.8:

7.24.2.8 The vswscanf function
''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.24.2.8p1:

:ref:`1 <9899_7.24.2.8p1>`

::

    #include <stdarg.h>
    #include <wchar.h>
    int vswscanf(const wchar_t * restrict s,
         const wchar_t * restrict format,
         va_list arg);

.. rubric:: Description

.. _9899_7.24.2.8p2:

:ref:`2 <9899_7.24.2.8p2>` The vswscanf function is equivalent to swscanf, with the variable argument list replaced by arg, which shall have been initialized by the va_start macro (and possibly subsequent va_arg calls). The vswscanf function does not invoke the va_end macro.\ [#9899_note291]_

.. rubric:: Returns

.. _9899_7.24.2.8p3:

:ref:`3 <9899_7.24.2.8p3>` The vswscanf function returns the value of the macro EOF if an input failure occurs before any conversion. Otherwise, the vswscanf function returns the number of input items assigned, which can be fewer than provided for, or even zero, in the event of an early matching failure.



.. rubric:: Footnotes

.. [#9899_note291] As the functions vfwprintf, vswprintf, vfwscanf, vwprintf, vwscanf, and vswscanf invoke the va_arg macro, the value of arg after the return is indeterminate.
