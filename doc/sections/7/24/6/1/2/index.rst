.. _9899_7.24.6.1.2:

7.24.6.1.2 The wctob function
"""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.6.1.2p1:

:ref:`1 <9899_7.24.6.1.2p1>`

::

    #include <stdio.h>
    #include <wchar.h>
    int wctob(wint_t c);

.. rubric:: Description

.. _9899_7.24.6.1.2p2:

:ref:`2 <9899_7.24.6.1.2p2>` The wctob function determines whether c corresponds to a member of the extended character set whose multibyte character representation is a single byte when in the initial shift state.

.. rubric:: Returns

.. _9899_7.24.6.1.2p3:

:ref:`3 <9899_7.24.6.1.2p3>` The wctob function returns EOF if c does not correspond to a multibyte character with length one in the initial shift state. Otherwise, it returns the single-byte representation of that character as an unsigned char converted to an int.

