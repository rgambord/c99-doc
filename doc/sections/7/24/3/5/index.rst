.. _9899_7.24.3.5:

7.24.3.5 The fwide function
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.24.3.5p1:

:ref:`1 <9899_7.24.3.5p1>`

::

    #include <stdio.h>
    #include <wchar.h>
    int fwide(FILE *stream, int mode);

.. rubric:: Description

.. _9899_7.24.3.5p2:

:ref:`2 <9899_7.24.3.5p2>` The fwide function determines the orientation of the stream pointed to by stream. If mode is greater than zero, the function first attempts to make the stream wide oriented. If mode is less than zero, the function first attempts to make the stream byte oriented.\ [#9899_note293]_ Otherwise, mode is zero and the function does not alter the orientation of the stream.

.. rubric:: Returns

.. _9899_7.24.3.5p3:

:ref:`3 <9899_7.24.3.5p3>` The fwide function returns a value greater than zero if, after the call, the stream has wide orientation, a value less than zero if the stream has byte orientation, or zero if the stream has no orientation.





.. rubric:: Footnotes

.. [#9899_note293] If the orientation of the stream has already been determined, fwide does not change it.
