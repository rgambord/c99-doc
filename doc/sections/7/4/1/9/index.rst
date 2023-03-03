.. _9899_7.4.1.9:

7.4.1.9 The ispunct function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.4.1.9p1:

:ref:`1 <9899_7.4.1.9p1>`

::

    #include <ctype.h>
    int ispunct(int c);

.. rubric:: Description

.. _9899_7.4.1.9p2:

:ref:`2 <9899_7.4.1.9p2>` The ispunct function tests for any printing character that is one of a locale-specific set of punctuation characters for which neither isspace nor isalnum is true. In the "C" locale, ispunct returns true for every printing character for which neither isspace nor isalnum is true.

