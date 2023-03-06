.. _9899_7.4.1.3:

7.4.1.3 The isblank function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.4.1.3p1:

.. container:: snum

   :ref:`1 <9899_7.4.1.3p1>`



::

    #include <ctype.h>
    int isblank(int c);

.. rubric:: Description

.. _9899_7.4.1.3p2:

.. container:: snum

   :ref:`2 <9899_7.4.1.3p2>`

The isblank function tests for any character that is a standard blank character or is one of a locale-specific set of characters for which isspace is true and that is used to separate words within a line of text. The standard blank characters are the following: space (' '), and horizontal tab ('\\t'). In the "C" locale, isblank returns true only for the standard blank characters.

