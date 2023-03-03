.. _9899_7.19.6.13:

7.19.6.13 The vsprintf function
'''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.6.13p1:

:ref:`1 <9899_7.19.6.13p1>`

::

    #include <stdarg.h>
    #include <stdio.h>
    int vsprintf(char * restrict s,
         const char * restrict format,
         va_list arg);

.. rubric:: Description

.. _9899_7.19.6.13p2:

:ref:`2 <9899_7.19.6.13p2>` The vsprintf function is equivalent to sprintf, with the variable argument list replaced by arg, which shall have been initialized by the va_start macro (and possibly subsequent va_arg calls). The vsprintf function does not invoke the va_end macro.\ [#9899_note254]_ If copying takes place between objects that overlap, the behavior is undefined.

.. rubric:: Returns

.. _9899_7.19.6.13p3:

:ref:`3 <9899_7.19.6.13p3>` The vsprintf function returns the number of characters written in the array, not counting the terminating null character, or a negative value if an encoding error occurred.



.. rubric:: Footnotes

.. [#9899_note254] As the functions vfprintf, vfscanf, vprintf, vscanf, vsnprintf, vsprintf, and vsscanf invoke the va_arg macro, the value of arg after the return is indeterminate.
