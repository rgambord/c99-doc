.. _9899_7.19.6.9:

7.19.6.9 The vfscanf function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.6.9p1:

.. container:: snum

   :ref:`1 <9899_7.19.6.9p1>`



::

    #include <stdarg.h>
    #include <stdio.h>
    int vfscanf(FILE * restrict stream,
         const char * restrict format,
         va_list arg);

.. rubric:: Description

.. _9899_7.19.6.9p2:

.. container:: snum

   :ref:`2 <9899_7.19.6.9p2>`

The vfscanf function is equivalent to fscanf, with the variable argument list replaced by arg, which shall have been initialized by the va_start macro (and possibly subsequent va_arg calls). The vfscanf function does not invoke the va_end macro.\ [#9899_note254]_

.. rubric:: Returns

.. _9899_7.19.6.9p3:

.. container:: snum

   :ref:`3 <9899_7.19.6.9p3>`

The vfscanf function returns the value of the macro EOF if an input failure occurs before any conversion. Otherwise, the vfscanf function returns the number of input items assigned, which can be fewer than provided for, or even zero, in the event of an early matching failure.



.. rubric:: Footnotes

.. [#9899_note254] As the functions vfprintf, vfscanf, vprintf, vscanf, vsnprintf, vsprintf, and vsscanf invoke the va_arg macro, the value of arg after the return is indeterminate.
