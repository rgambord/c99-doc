.. _9899_7.15:

7.15 Variable arguments \<stdarg.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. toctree::
   :maxdepth: 2

   1/index


.. _9899_7.15p1:

:ref:`1 <9899_7.15p1>` The header :ref:`\<stdarg.h> <9899_7.15>` declares a type and defines four macros, for advancing through a list of arguments whose number and types are not known to the called function when it is translated.

.. _9899_7.15p2:

:ref:`2 <9899_7.15p2>` A function may be called with a variable number of arguments of varying types. As described in :ref:`6.9.1 <9899_6.9.1>`, its parameter list contains one or more parameters. The rightmost parameter plays a special role in the access mechanism, and will be designated parmN in this description.

.. _9899_7.15p3:

:ref:`3 <9899_7.15p3>` The type declared is

::

    va_list

which is an object type suitable for holding information needed by the macros va_start, va_arg, va_end, and va_copy. If access to the varying arguments is desired, the called function shall declare an object (generally referred to as ap in this subclause) having type va_list. The object ap may be passed as an argument to another function; if that function invokes the va_arg macro with parameter ap, the value of ap in the calling function is indeterminate and shall be passed to the va_end macro prior to any further reference to ap.\ [#9899_note221]_





.. rubric:: Footnotes

.. [#9899_note221] It is permitted to create a pointer to a va_list and pass that pointer to another function, in which case the original function may make further use of the original list after the other function returns.
