.. _9899_7.24.2.12:

7.24.2.12 The wscanf function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.24.2.12p1:

.. container:: snum

   :ref:`1 <9899_7.24.2.12p1>`



::

    #include <wchar.h>
    int wscanf(const wchar_t * restrict format, ...);

.. rubric:: Description

.. _9899_7.24.2.12p2:

.. container:: snum

   :ref:`2 <9899_7.24.2.12p2>`

The wscanf function is equivalent to fwscanf with the argument stdin interposed before the arguments to wscanf.

.. rubric:: Returns

.. _9899_7.24.2.12p3:

.. container:: snum

   :ref:`3 <9899_7.24.2.12p3>`

The wscanf function returns the value of the macro EOF if an input failure occurs before any conversion. Otherwise, the wscanf function returns the number of input items assigned, which can be fewer than provided for, or even zero, in the event of an early matching failure.

