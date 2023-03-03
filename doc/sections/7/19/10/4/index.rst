.. _9899_7.19.10.4:

7.19.10.4 The perror function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.10.4p1:

:ref:`1 <9899_7.19.10.4p1>`

::

    #include <stdio.h>
    void perror(const char *s);

.. rubric:: Description

.. _9899_7.19.10.4p2:

:ref:`2 <9899_7.19.10.4p2>` The perror function maps the error number in the integer expression errno to an error message. It writes a sequence of characters to the standard error stream thus: first (if s is not a null pointer and the character pointed to by s is not the null character), the string pointed to by s followed by a colon (:) and a space; then an appropriate error message string followed by a new-line character. The contents of the error message strings are the same as those returned by the strerror function with argument errno.

.. rubric:: Returns

.. _9899_7.19.10.4p3:

:ref:`3 <9899_7.19.10.4p3>` The perror function returns no value.

**Forward references**: the strerror function (:ref:`7.21.6.2 <9899_7.21.6.2>`).

