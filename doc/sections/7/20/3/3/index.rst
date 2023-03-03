.. _9899_7.20.3.3:

7.20.3.3 The malloc function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.3.3p1:

:ref:`1 <9899_7.20.3.3p1>`

::

    #include <stdlib.h>
    void *malloc(size_t size);

.. rubric:: Description

.. _9899_7.20.3.3p2:

:ref:`2 <9899_7.20.3.3p2>` The malloc function allocates space for an object whose size is specified by size and whose value is indeterminate.

.. rubric:: Returns

.. _9899_7.20.3.3p3:

:ref:`3 <9899_7.20.3.3p3>` The malloc function returns either a null pointer or a pointer to the allocated space.

