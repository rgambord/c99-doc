.. _9899_7.19.4.3:

7.19.4.3 The tmpfile function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.4.3p1:

:ref:`1 <9899_7.19.4.3p1>`

::

    #include <stdio.h>
    FILE *tmpfile(void);

.. rubric:: Description

.. _9899_7.19.4.3p2:

:ref:`2 <9899_7.19.4.3p2>` The tmpfile function creates a temporary binary file that is different from any other existing file and that will automatically be removed when it is closed or at program termination. If the program terminates abnormally, whether an open temporary file is removed is implementation-defined. The file is opened for update with "wb+" mode.

.. rubric:: Recommended practice

.. _9899_7.19.4.3p3:

:ref:`3 <9899_7.19.4.3p3>` It should be possible to open at least TMP_MAX temporary files during the lifetime of the program (this limit may be shared with tmpnam) and there should be no limit on the number simultaneously open other than this limit and any limit on the number of open files (FOPEN_MAX).

.. rubric:: Returns

.. _9899_7.19.4.3p4:

:ref:`4 <9899_7.19.4.3p4>` The tmpfile function returns a pointer to the stream of the file that it created. If the file cannot be created, the tmpfile function returns a null pointer.

**Forward references**: the fopen function (:ref:`7.19.5.3 <9899_7.19.5.3>`).

