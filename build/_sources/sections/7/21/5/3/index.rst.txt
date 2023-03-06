.. _9899_7.21.5.3:

7.21.5.3 The strcspn function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.21.5.3p1:

.. container:: snum

   :ref:`1 <9899_7.21.5.3p1>`



::

    #include <string.h>
    size_t strcspn(const char *s1, const char *s2);

.. rubric:: Description

.. _9899_7.21.5.3p2:

.. container:: snum

   :ref:`2 <9899_7.21.5.3p2>`

The strcspn function computes the length of the maximum initial segment of the string pointed to by s1 which consists entirely of characters not from the string pointed to by s2.

.. rubric:: Returns

.. _9899_7.21.5.3p3:

.. container:: snum

   :ref:`3 <9899_7.21.5.3p3>`

The strcspn function returns the length of the segment.

