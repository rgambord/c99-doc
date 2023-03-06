.. _9899_7.20.4.5:

7.20.4.5 The getenv function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.4.5p1:

.. container:: snum

   :ref:`1 <9899_7.20.4.5p1>`



::

    #include <stdlib.h>
    char *getenv(const char *name);

.. rubric:: Description

.. _9899_7.20.4.5p2:

.. container:: snum

   :ref:`2 <9899_7.20.4.5p2>`

The getenv function searches an environment list, provided by the host environment, for a string that matches the string pointed to by name. The set of environment names and the method for altering the environment list are implementation-defined.

.. _9899_7.20.4.5p3:

.. container:: snum

   :ref:`3 <9899_7.20.4.5p3>`

The implementation shall behave as if no library function calls the getenv function.

.. rubric:: Returns

.. _9899_7.20.4.5p4:

.. container:: snum

   :ref:`4 <9899_7.20.4.5p4>`

The getenv function returns a pointer to a string associated with the matched list member. The string pointed to shall not be modified by the program, but may be overwritten by a subsequent call to the getenv function. If the specified name cannot be found, a null pointer is returned.

