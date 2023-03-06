.. _9899_7.24.2.5:

7.24.2.5 The vfwprintf function
'''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.24.2.5p1:

.. container:: snum

   :ref:`1 <9899_7.24.2.5p1>`



::

    #include <stdarg.h>
    #include <stdio.h>
    #include <wchar.h>
    int vfwprintf(FILE * restrict stream,
         const wchar_t * restrict format,
         va_list arg);

.. rubric:: Description

.. _9899_7.24.2.5p2:

.. container:: snum

   :ref:`2 <9899_7.24.2.5p2>`

The vfwprintf function is equivalent to fwprintf, with the variable argument list replaced by arg, which shall have been initialized by the va_start macro (and possibly subsequent va_arg calls). The vfwprintf function does not invoke the va_end macro.\ [#9899_note291]_

.. rubric:: Returns

.. _9899_7.24.2.5p3:

.. container:: snum

   :ref:`3 <9899_7.24.2.5p3>`

The vfwprintf function returns the number of wide characters transmitted, or a negative value if an output or encoding error occurred.

.. _9899_7.24.2.5p4:

.. container:: snum

   :ref:`4 <9899_7.24.2.5p4>`

EXAMPLE The following shows the use of the vfwprintf function in a general error-reporting routine.

::

    #include <stdarg.h>
    #include <stdio.h>
    #include <wchar.h>
    void error(char *function_name, wchar_t *format, ...)
    {
          va_list args;
             va_start(args, format);
             // print out name of function causing error
             fwprintf(stderr, L"ERROR in %s: ", function_name);
             // print out remainder of message
             vfwprintf(stderr, format, args);
             va_end(args);
    }





.. rubric:: Footnotes

.. [#9899_note291] As the functions vfwprintf, vswprintf, vfwscanf, vwprintf, vwscanf, and vswscanf invoke the va_arg macro, the value of arg after the return is indeterminate.
