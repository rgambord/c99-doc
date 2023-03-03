.. _9899_7.24.3.7:

7.24.3.7 The getwchar function
''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.24.3.7p1:

:ref:`1 <9899_7.24.3.7p1>`

::

    #include <wchar.h>
    wint_t getwchar(void);

.. rubric:: Description

.. _9899_7.24.3.7p2:

:ref:`2 <9899_7.24.3.7p2>` The getwchar function is equivalent to getwc with the argument stdin.

.. rubric:: Returns

.. _9899_7.24.3.7p3:

:ref:`3 <9899_7.24.3.7p3>` The getwchar function returns the next wide character from the input stream pointed to by stdin, or WEOF.

