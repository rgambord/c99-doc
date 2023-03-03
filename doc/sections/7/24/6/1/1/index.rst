.. _9899_7.24.6.1.1:

7.24.6.1.1 The btowc function
"""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.6.1.1p1:

:ref:`1 <9899_7.24.6.1.1p1>`

::

    #include <stdio.h>
    #include <wchar.h>
    wint_t btowc(int c);

.. rubric:: Description

.. _9899_7.24.6.1.1p2:

:ref:`2 <9899_7.24.6.1.1p2>` The btowc function determines whether c constitutes a valid single-byte character in the initial shift state.

.. rubric:: Returns

.. _9899_7.24.6.1.1p3:

:ref:`3 <9899_7.24.6.1.1p3>` The btowc function returns WEOF if c has the value EOF or if (unsigned char)c does not constitute a valid single-byte character in the initial shift state. Otherwise, it returns the wide character representation of that character.

