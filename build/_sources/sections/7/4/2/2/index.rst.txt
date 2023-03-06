.. _9899_7.4.2.2:

7.4.2.2 The toupper function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.4.2.2p1:

.. container:: snum

   :ref:`1 <9899_7.4.2.2p1>`



::

    #include <ctype.h>
    int toupper(int c);

.. rubric:: Description

.. _9899_7.4.2.2p2:

.. container:: snum

   :ref:`2 <9899_7.4.2.2p2>`

The toupper function converts a lowercase letter to a corresponding uppercase letter.

.. rubric:: Returns

.. _9899_7.4.2.2p3:

.. container:: snum

   :ref:`3 <9899_7.4.2.2p3>`

If the argument is a character for which islower is true and there are one or more corresponding characters, as specified by the current locale, for which isupper is true, the toupper function returns one of the corresponding characters (always the same one for any given locale); otherwise, the argument is returned unchanged.

