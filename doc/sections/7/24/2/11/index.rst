.. _9899_7.24.2.11:

7.24.2.11 The wprintf function
''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.24.2.11p1:

:ref:`1 <9899_7.24.2.11p1>`

::

    #include <wchar.h>
    int wprintf(const wchar_t * restrict format, ...);

.. rubric:: Description

.. _9899_7.24.2.11p2:

:ref:`2 <9899_7.24.2.11p2>` The wprintf function is equivalent to fwprintf with the argument stdout interposed before the arguments to wprintf.

.. rubric:: Returns

.. _9899_7.24.2.11p3:

:ref:`3 <9899_7.24.2.11p3>` The wprintf function returns the number of wide characters transmitted, or a negative value if an output or encoding error occurred.

