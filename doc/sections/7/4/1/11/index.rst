.. _9899_7.4.1.11:

7.4.1.11 The isupper function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.4.1.11p1:

:ref:`1 <9899_7.4.1.11p1>`

::

    #include <ctype.h>
    int isupper(int c);

.. rubric:: Description

.. _9899_7.4.1.11p2:

:ref:`2 <9899_7.4.1.11p2>` The isupper function tests for any character that is an uppercase letter or is one of a locale-specific set of characters for which none of iscntrl, isdigit, ispunct, or isspace is true. In the "C" locale, isupper returns true only for the uppercase letters (as defined in :ref:`5.2.1 <9899_5.2.1>`).

