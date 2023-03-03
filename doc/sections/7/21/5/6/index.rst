.. _9899_7.21.5.6:

7.21.5.6 The strspn function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.21.5.6p1:

:ref:`1 <9899_7.21.5.6p1>`

::

    #include <string.h>
    size_t strspn(const char *s1, const char *s2);

.. rubric:: Description

.. _9899_7.21.5.6p2:

:ref:`2 <9899_7.21.5.6p2>` The strspn function computes the length of the maximum initial segment of the string pointed to by s1 which consists entirely of characters from the string pointed to by s2.

.. rubric:: Returns

.. _9899_7.21.5.6p3:

:ref:`3 <9899_7.21.5.6p3>` The strspn function returns the length of the segment.

