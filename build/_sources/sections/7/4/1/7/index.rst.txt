.. _9899_7.4.1.7:

7.4.1.7 The islower function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.4.1.7p1:

.. container:: snum

   :ref:`1 <9899_7.4.1.7p1>`



::

    #include <ctype.h>
    int islower(int c);

.. rubric:: Description

.. _9899_7.4.1.7p2:

.. container:: snum

   :ref:`2 <9899_7.4.1.7p2>`

The islower function tests for any character that is a lowercase letter or is one of a locale-specific set of characters for which none of iscntrl, isdigit, ispunct, or isspace is true. In the "C" locale, islower returns true only for the lowercase letters (as defined in :ref:`5.2.1 <9899_5.2.1>`).

