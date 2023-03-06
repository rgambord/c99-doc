.. _9899_7.24.2.7:

7.24.2.7 The vswprintf function
'''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.24.2.7p1:

.. container:: snum

   :ref:`1 <9899_7.24.2.7p1>`



::

    #include <stdarg.h>
    #include <wchar.h>
    int vswprintf(wchar_t * restrict s,
         size_t n,
         const wchar_t * restrict format,
         va_list arg);

.. rubric:: Description

.. _9899_7.24.2.7p2:

.. container:: snum

   :ref:`2 <9899_7.24.2.7p2>`

The vswprintf function is equivalent to swprintf, with the variable argument list replaced by arg, which shall have been initialized by the va_start macro (and possibly subsequent va_arg calls). The vswprintf function does not invoke the va_end macro.\ [#9899_note291]_

.. rubric:: Returns

.. _9899_7.24.2.7p3:

.. container:: snum

   :ref:`3 <9899_7.24.2.7p3>`

The vswprintf function returns the number of wide characters written in the array, not counting the terminating null wide character, or a negative value if an encoding error occurred or if n or more wide characters were requested to be generated.



.. rubric:: Footnotes

.. [#9899_note291] As the functions vfwprintf, vswprintf, vfwscanf, vwprintf, vwscanf, and vswscanf invoke the va_arg macro, the value of arg after the return is indeterminate.
