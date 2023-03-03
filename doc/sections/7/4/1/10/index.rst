.. _9899_7.4.1.10:

7.4.1.10 The isspace function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.4.1.10p1:

:ref:`1 <9899_7.4.1.10p1>`

::

    #include <ctype.h>
    int isspace(int c);

.. rubric:: Description

.. _9899_7.4.1.10p2:

:ref:`2 <9899_7.4.1.10p2>` The isspace function tests for any character that is a standard white-space character or is one of a locale-specific set of characters for which isalnum is false. The standard white-space characters are the following: space (' '), form feed ('\\f'), new-line ('\\n'), carriage return ('\\r'), horizontal tab ('\\t'), and vertical tab ('\\v'). In the "C" locale, isspace returns true only for the standard white-space characters.

