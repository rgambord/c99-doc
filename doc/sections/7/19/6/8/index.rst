.. _9899_7.19.6.8:

7.19.6.8 The vfprintf function
''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.6.8p1:

:ref:`1 <9899_7.19.6.8p1>`

::

    #include <stdarg.h>
    #include <stdio.h>
    int vfprintf(FILE * restrict stream,
         const char * restrict format,
         va_list arg);

.. rubric:: Description

.. _9899_7.19.6.8p2:

:ref:`2 <9899_7.19.6.8p2>` The vfprintf function is equivalent to fprintf, with the variable argument list replaced by arg, which shall have been initialized by the va_start macro (and possibly subsequent va_arg calls). The vfprintf function does not invoke the va_end macro.\ [#9899_note254]_

.. rubric:: Returns

.. _9899_7.19.6.8p3:

:ref:`3 <9899_7.19.6.8p3>` The vfprintf function returns the number of characters transmitted, or a negative value if an output or encoding error occurred.

.. _9899_7.19.6.8p4:

:ref:`4 <9899_7.19.6.8p4>` EXAMPLE The following shows the use of the vfprintf function in a general error-reporting routine.

::

    #include <stdarg.h>
    #include <stdio.h>
    void error(char *function_name, char *format, ...)
    {
          va_list args;
             va_start(args, format);
             // print out name of function causing error
             fprintf(stderr, "ERROR in %s: ", function_name);
             // print out remainder of message
             vfprintf(stderr, format, args);
             va_end(args);
    }





.. rubric:: Footnotes

.. [#9899_note254] As the functions vfprintf, vfscanf, vprintf, vscanf, vsnprintf, vsprintf, and vsscanf invoke the va_arg macro, the value of arg after the return is indeterminate.
