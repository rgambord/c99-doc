.. _9899_7.24.3.2:

7.24.3.2 The fgetws function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.24.3.2p1:

:ref:`1 <9899_7.24.3.2p1>`

::

    #include <stdio.h>
    #include <wchar.h>
    wchar_t *fgetws(wchar_t * restrict s,
         int n, FILE * restrict stream);

.. rubric:: Description

.. _9899_7.24.3.2p2:

:ref:`2 <9899_7.24.3.2p2>` The fgetws function reads at most one less than the number of wide characters specified by n from the stream pointed to by stream into the array pointed to by s. No additional wide characters are read after a new-line wide character (which is retained) or after end-of-file. A null wide character is written immediately after the last wide character read into the array.

.. rubric:: Returns

.. _9899_7.24.3.2p3:

:ref:`3 <9899_7.24.3.2p3>` The fgetws function returns s if successful. If end-of-file is encountered and no characters have been read into the array, the contents of the array remain unchanged and a null pointer is returned. If a read or encoding error occurs during the operation, the array contents are indeterminate and a null pointer is returned.

