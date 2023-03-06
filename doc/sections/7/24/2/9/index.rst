.. _9899_7.24.2.9:

7.24.2.9 The vwprintf function
''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.24.2.9p1:

.. container:: snum

   :ref:`1 <9899_7.24.2.9p1>`



::

    #include <stdarg.h>
    #include <wchar.h>
    int vwprintf(const wchar_t * restrict format,
         va_list arg);

.. rubric:: Description

.. _9899_7.24.2.9p2:

.. container:: snum

   :ref:`2 <9899_7.24.2.9p2>`

The vwprintf function is equivalent to wprintf, with the variable argument list replaced by arg, which shall have been initialized by the va_start macro (and possibly subsequent va_arg calls). The vwprintf function does not invoke the va_end macro.\ [#9899_note291]_

.. rubric:: Returns

.. _9899_7.24.2.9p3:

.. container:: snum

   :ref:`3 <9899_7.24.2.9p3>`

The vwprintf function returns the number of wide characters transmitted, or a negative value if an output or encoding error occurred.



.. rubric:: Footnotes

.. [#9899_note291] As the functions vfwprintf, vswprintf, vfwscanf, vwprintf, vwscanf, and vswscanf invoke the va_arg macro, the value of arg after the return is indeterminate.
