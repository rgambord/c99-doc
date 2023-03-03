.. _9899_7.4.2.1:

7.4.2.1 The tolower function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.4.2.1p1:

:ref:`1 <9899_7.4.2.1p1>`

::

    #include <ctype.h>
    int tolower(int c);

.. rubric:: Description

.. _9899_7.4.2.1p2:

:ref:`2 <9899_7.4.2.1p2>` The tolower function converts an uppercase letter to a corresponding lowercase letter.

.. rubric:: Returns

.. _9899_7.4.2.1p3:

:ref:`3 <9899_7.4.2.1p3>` If the argument is a character for which isupper is true and there are one or more corresponding characters, as specified by the current locale, for which islower is true, the tolower function returns one of the corresponding characters (always the same one for any given locale); otherwise, the argument is returned unchanged.

