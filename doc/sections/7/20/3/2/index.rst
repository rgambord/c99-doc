.. _9899_7.20.3.2:

7.20.3.2 The free function
''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.3.2p1:

:ref:`1 <9899_7.20.3.2p1>`

::

    #include <stdlib.h>
    void free(void *ptr);

.. rubric:: Description

.. _9899_7.20.3.2p2:

:ref:`2 <9899_7.20.3.2p2>` The free function causes the space pointed to by ptr to be deallocated, that is, made available for further allocation. If ptr is a null pointer, no action occurs. Otherwise, if the argument does not match a pointer earlier returned by the calloc, malloc, or realloc function, or if the space has been deallocated by a call to free or realloc, the behavior is undefined.

.. rubric:: Returns

.. _9899_7.20.3.2p3:

:ref:`3 <9899_7.20.3.2p3>` The free function returns no value.

