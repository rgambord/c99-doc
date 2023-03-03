.. _9899_7.19.4.1:

7.19.4.1 The remove function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.4.1p1:

:ref:`1 <9899_7.19.4.1p1>`

::

    #include <stdio.h>
    int remove(const char *filename);

.. rubric:: Description

.. _9899_7.19.4.1p2:

:ref:`2 <9899_7.19.4.1p2>` The remove function causes the file whose name is the string pointed to by filename to be no longer accessible by that name. A subsequent attempt to open that file using that name will fail, unless it is created anew. If the file is open, the behavior of the remove function is implementation-defined.

.. rubric:: Returns

.. _9899_7.19.4.1p3:

:ref:`3 <9899_7.19.4.1p3>` The remove function returns zero if the operation succeeds, nonzero if it fails.

