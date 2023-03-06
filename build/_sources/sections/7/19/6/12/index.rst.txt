.. _9899_7.19.6.12:

7.19.6.12 The vsnprintf function
''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.6.12p1:

.. container:: snum

   :ref:`1 <9899_7.19.6.12p1>`



::

    #include <stdarg.h>
    #include <stdio.h>
    int vsnprintf(char * restrict s, size_t n,
         const char * restrict format,
         va_list arg);

.. rubric:: Description

.. _9899_7.19.6.12p2:

.. container:: snum

   :ref:`2 <9899_7.19.6.12p2>`

The vsnprintf function is equivalent to snprintf, with the variable argument list replaced by arg, which shall have been initialized by the va_start macro (and possibly subsequent va_arg calls). The vsnprintf function does not invoke the va_end macro.\ [#9899_note254]_ If copying takes place between objects that overlap, the behavior is undefined.

.. rubric:: Returns

.. _9899_7.19.6.12p3:

.. container:: snum

   :ref:`3 <9899_7.19.6.12p3>`

The vsnprintf function returns the number of characters that would have been written had n been sufficiently large, not counting the terminating null character, or a negative value if an encoding error occurred. Thus, the null-terminated output has been completely written if and only if the returned value is nonnegative and less than n.



.. rubric:: Footnotes

.. [#9899_note254] As the functions vfprintf, vfscanf, vprintf, vscanf, vsnprintf, vsprintf, and vsscanf invoke the va_arg macro, the value of arg after the return is indeterminate.
