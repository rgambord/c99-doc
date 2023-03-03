.. _9899_7.4.1.2:

7.4.1.2 The isalpha function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.4.1.2p1:

:ref:`1 <9899_7.4.1.2p1>`

::

    #include <ctype.h>
    int isalpha(int c);

.. rubric:: Description

.. _9899_7.4.1.2p2:

:ref:`2 <9899_7.4.1.2p2>` The isalpha function tests for any character for which isupper or islower is true, or any character that is one of a locale-specific set of alphabetic characters for which none of iscntrl, isdigit, ispunct, or isspace is true.\ [#9899_note174]_ In the "C" locale, isalpha returns true only for the characters for which isupper or islower is true.





.. rubric:: Footnotes

.. [#9899_note174] The functions islower and isupper test true or false separately for each of these additional characters; all four combinations are possible.
