.. _9899_7.21.6.2:

7.21.6.2 The strerror function
''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.21.6.2p1:

.. container:: snum

   :ref:`1 <9899_7.21.6.2p1>`



::

    #include <string.h>
    char *strerror(int errnum);

.. rubric:: Description

.. _9899_7.21.6.2p2:

.. container:: snum

   :ref:`2 <9899_7.21.6.2p2>`

The strerror function maps the number in errnum to a message string. Typically, the values for errnum come from errno, but strerror shall map any value of type int to a message.

.. _9899_7.21.6.2p3:

.. container:: snum

   :ref:`3 <9899_7.21.6.2p3>`

The implementation shall behave as if no library function calls the strerror function.

.. rubric:: Returns

.. _9899_7.21.6.2p4:

.. container:: snum

   :ref:`4 <9899_7.21.6.2p4>`

The strerror function returns a pointer to the string, the contents of which are locale- specific. The array pointed to shall not be modified by the program, but may be overwritten by a subsequent call to the strerror function.

