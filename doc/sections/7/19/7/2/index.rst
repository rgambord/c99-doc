.. _9899_7.19.7.2:

7.19.7.2 The fgets function
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.7.2p1:

:ref:`1 <9899_7.19.7.2p1>`

::

    #include <stdio.h>
    char *fgets(char * restrict s, int n,
         FILE * restrict stream);

.. rubric:: Description

.. _9899_7.19.7.2p2:

:ref:`2 <9899_7.19.7.2p2>` The fgets function reads at most one less than the number of characters specified by n from the stream pointed to by stream into the array pointed to by s. No additional characters are read after a new-line character (which is retained) or after end-of-file. A null character is written immediately after the last character read into the array.

.. rubric:: Returns

.. _9899_7.19.7.2p3:

:ref:`3 <9899_7.19.7.2p3>` The fgets function returns s if successful. If end-of-file is encountered and no characters have been read into the array, the contents of the array remain unchanged and a null pointer is returned. If a read error occurs during the operation, the array contents are indeterminate and a null pointer is returned.

