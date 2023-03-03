.. _9899_7.19.7.7:

7.19.7.7 The gets function
''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.7.7p1:

:ref:`1 <9899_7.19.7.7p1>`

::

    #include <stdio.h>
    char *gets(char *s);

.. rubric:: Description

.. _9899_7.19.7.7p2:

:ref:`2 <9899_7.19.7.7p2>` The gets function reads characters from the input stream pointed to by stdin, into the array pointed to by s, until end-of-file is encountered or a new-line character is read. Any new-line character is discarded, and a null character is written immediately after the last character read into the array.

.. rubric:: Returns

.. _9899_7.19.7.7p3:

:ref:`3 <9899_7.19.7.7p3>` The gets function returns s if successful. If end-of-file is encountered and no characters have been read into the array, the contents of the array remain unchanged and a null pointer is returned. If a read error occurs during the operation, the array contents are indeterminate and a null pointer is returned.

**Forward references**: future library directions (:ref:`7.26.9 <9899_7.26.9>`).

