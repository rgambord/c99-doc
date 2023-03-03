.. _9899_7.19.4.2:

7.19.4.2 The rename function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.4.2p1:

:ref:`1 <9899_7.19.4.2p1>`

::

    #include <stdio.h>
    int rename(const char *old, const char *new);

.. rubric:: Description

.. _9899_7.19.4.2p2:

:ref:`2 <9899_7.19.4.2p2>` The rename function causes the file whose name is the string pointed to by old to be henceforth known by the name given by the string pointed to by new. The file named old is no longer accessible by that name. If a file named by the string pointed to by new exists prior to the call to the rename function, the behavior is implementation-defined.

.. rubric:: Returns

.. _9899_7.19.4.2p3:

:ref:`3 <9899_7.19.4.2p3>` The rename function returns zero if the operation succeeds, nonzero if it fails,\ [#9899_note235]_ in which case if the file existed previously it is still known by its original name.





.. rubric:: Footnotes

.. [#9899_note235] Among the reasons the implementation may cause the rename function to fail are that the file is open or that it is necessary to copy its contents to effectuate its renaming.
