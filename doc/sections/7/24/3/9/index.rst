.. _9899_7.24.3.9:

7.24.3.9 The putwchar function
''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.24.3.9p1:

:ref:`1 <9899_7.24.3.9p1>`

::

    #include <wchar.h>
    wint_t putwchar(wchar_t c);

.. rubric:: Description

.. _9899_7.24.3.9p2:

:ref:`2 <9899_7.24.3.9p2>` The putwchar function is equivalent to putwc with the second argument stdout.

.. rubric:: Returns

.. _9899_7.24.3.9p3:

:ref:`3 <9899_7.24.3.9p3>` The putwchar function returns the character written, or WEOF.

