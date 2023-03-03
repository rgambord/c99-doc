.. _9899_7.24.3.8:

7.24.3.8 The putwc function
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.24.3.8p1:

:ref:`1 <9899_7.24.3.8p1>`

::

    #include <stdio.h>
    #include <wchar.h>
    wint_t putwc(wchar_t c, FILE *stream);

.. rubric:: Description

.. _9899_7.24.3.8p2:

:ref:`2 <9899_7.24.3.8p2>` The putwc function is equivalent to fputwc, except that if it is implemented as a macro, it may evaluate stream more than once, so that argument should never be an expression with side effects.

.. rubric:: Returns

.. _9899_7.24.3.8p3:

:ref:`3 <9899_7.24.3.8p3>` The putwc function returns the wide character written, or WEOF.

