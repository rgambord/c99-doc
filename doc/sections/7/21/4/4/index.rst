.. _9899_7.21.4.4:

7.21.4.4 The strncmp function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.21.4.4p1:

.. container:: snum

   :ref:`1 <9899_7.21.4.4p1>`



::

    #include <string.h>
    int strncmp(const char *s1, const char *s2, size_t n);

.. rubric:: Description

.. _9899_7.21.4.4p2:

.. container:: snum

   :ref:`2 <9899_7.21.4.4p2>`

The strncmp function compares not more than n characters (characters that follow a null character are not compared) from the array pointed to by s1 to the array pointed to by s2.

.. rubric:: Returns

.. _9899_7.21.4.4p3:

.. container:: snum

   :ref:`3 <9899_7.21.4.4p3>`

The strncmp function returns an integer greater than, equal to, or less than zero, accordingly as the possibly null-terminated array pointed to by s1 is greater than, equal to, or less than the possibly null-terminated array pointed to by s2.

