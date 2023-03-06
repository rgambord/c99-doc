.. _9899_7.21.4.3:

7.21.4.3 The strcoll function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.21.4.3p1:

.. container:: snum

   :ref:`1 <9899_7.21.4.3p1>`



::

    #include <string.h>
    int strcoll(const char *s1, const char *s2);

.. rubric:: Description

.. _9899_7.21.4.3p2:

.. container:: snum

   :ref:`2 <9899_7.21.4.3p2>`

The strcoll function compares the string pointed to by s1 to the string pointed to by s2, both interpreted as appropriate to the LC_COLLATE category of the current locale.

.. rubric:: Returns

.. _9899_7.21.4.3p3:

.. container:: snum

   :ref:`3 <9899_7.21.4.3p3>`

The strcoll function returns an integer greater than, equal to, or less than zero, accordingly as the string pointed to by s1 is greater than, equal to, or less than the string pointed to by s2 when both are interpreted as appropriate to the current locale.

