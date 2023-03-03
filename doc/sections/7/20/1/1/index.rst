.. _9899_7.20.1.1:

7.20.1.1 The atof function
''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.1.1p1:

:ref:`1 <9899_7.20.1.1p1>`

::

    #include <stdlib.h>
    double atof(const char *nptr);

.. rubric:: Description

.. _9899_7.20.1.1p2:

:ref:`2 <9899_7.20.1.1p2>` The atof function converts the initial portion of the string pointed to by nptr to double representation. Except for the behavior on error, it is equivalent to

::

    strtod(nptr, (char **)NULL)

.. rubric:: Returns

.. _9899_7.20.1.1p3:

:ref:`3 <9899_7.20.1.1p3>` The atof function returns the converted value.

**Forward references**: the strtod, strtof, and strtold functions (:ref:`7.20.1.3 <9899_7.20.1.3>`).

