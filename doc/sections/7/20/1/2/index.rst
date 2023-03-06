.. _9899_7.20.1.2:

7.20.1.2 The atoi, atol, and atoll functions
''''''''''''''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.1.2p1:

.. container:: snum

   :ref:`1 <9899_7.20.1.2p1>`



::

    #include <stdlib.h>
    int atoi(const char *nptr);
    long int atol(const char *nptr);
    long long int atoll(const char *nptr);

.. rubric:: Description

.. _9899_7.20.1.2p2:

.. container:: snum

   :ref:`2 <9899_7.20.1.2p2>`

The atoi, atol, and atoll functions convert the initial portion of the string pointed to by nptr to int, long int, and long long int representation, respectively. Except for the behavior on error, they are equivalent to

::

    atoi: (int)strtol(nptr, (char **)NULL, 10)
    atol: strtol(nptr, (char **)NULL, 10)
    atoll: strtoll(nptr, (char **)NULL, 10)

.. rubric:: Returns

.. _9899_7.20.1.2p3:

.. container:: snum

   :ref:`3 <9899_7.20.1.2p3>`

The atoi, atol, and atoll functions return the converted value.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_7.20.1.4`

