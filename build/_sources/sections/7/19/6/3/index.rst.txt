.. _9899_7.19.6.3:

7.19.6.3 The printf function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.6.3p1:

.. container:: snum

   :ref:`1 <9899_7.19.6.3p1>`



::

    #include <stdio.h>
    int printf(const char * restrict format, ...);

.. rubric:: Description

.. _9899_7.19.6.3p2:

.. container:: snum

   :ref:`2 <9899_7.19.6.3p2>`

The printf function is equivalent to fprintf with the argument stdout interposed before the arguments to printf.

.. rubric:: Returns

.. _9899_7.19.6.3p3:

.. container:: snum

   :ref:`3 <9899_7.19.6.3p3>`

The printf function returns the number of characters transmitted, or a negative value if an output or encoding error occurred.

