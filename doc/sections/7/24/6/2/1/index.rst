.. _9899_7.24.6.2.1:

7.24.6.2.1 The mbsinit function
"""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.6.2.1p1:

:ref:`1 <9899_7.24.6.2.1p1>`

::

    #include <wchar.h>
    int mbsinit(const mbstate_t *ps);

.. rubric:: Description

.. _9899_7.24.6.2.1p2:

:ref:`2 <9899_7.24.6.2.1p2>` If ps is not a null pointer, the mbsinit function determines whether the pointed-to mbstate_t object describes an initial conversion state.

.. rubric:: Returns

.. _9899_7.24.6.2.1p3:

:ref:`3 <9899_7.24.6.2.1p3>` The mbsinit function returns nonzero if ps is a null pointer or if the pointed-to object describes an initial conversion state; otherwise, it returns zero.

