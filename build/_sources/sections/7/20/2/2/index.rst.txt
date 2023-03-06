.. _9899_7.20.2.2:

7.20.2.2 The srand function
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.2.2p1:

.. container:: snum

   :ref:`1 <9899_7.20.2.2p1>`



::

    #include <stdlib.h>
    void srand(unsigned int seed);

.. rubric:: Description

.. _9899_7.20.2.2p2:

.. container:: snum

   :ref:`2 <9899_7.20.2.2p2>`

The srand function uses the argument as a seed for a new sequence of pseudo-random numbers to be returned by subsequent calls to rand. If srand is then called with the same seed value, the sequence of pseudo-random numbers shall be repeated. If rand is called before any calls to srand have been made, the same sequence shall be generated as when srand is first called with a seed value of 1.

.. _9899_7.20.2.2p3:

.. container:: snum

   :ref:`3 <9899_7.20.2.2p3>`

The implementation shall behave as if no library function calls the srand function.

.. rubric:: Returns

.. _9899_7.20.2.2p4:

.. container:: snum

   :ref:`4 <9899_7.20.2.2p4>`

The srand function returns no value.

.. _9899_7.20.2.2p5:

.. container:: snum

   :ref:`5 <9899_7.20.2.2p5>`

EXAMPLE The following functions define a portable implementation of rand and srand.

::

    static unsigned long int next = 1;
    int rand(void)   // RAND_MAX assumed to be 32767
    {
          next = next * 1103515245 + 12345;
          return (unsigned int)(next/65536) % 32768;
    }
    void srand(unsigned int seed)
    {
          next = seed;
    }

