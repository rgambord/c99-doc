.. _9899_7.24.3.6:

7.24.3.6 The getwc function
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.24.3.6p1:

.. container:: snum

   :ref:`1 <9899_7.24.3.6p1>`



::

    #include <stdio.h>
    #include <wchar.h>
    wint_t getwc(FILE *stream);

.. rubric:: Description

.. _9899_7.24.3.6p2:

.. container:: snum

   :ref:`2 <9899_7.24.3.6p2>`

The getwc function is equivalent to fgetwc, except that if it is implemented as a macro, it may evaluate stream more than once, so the argument should never be an expression with side effects.

.. rubric:: Returns

.. _9899_7.24.3.6p3:

.. container:: snum

   :ref:`3 <9899_7.24.3.6p3>`

The getwc function returns the next wide character from the input stream pointed to by stream, or WEOF.

