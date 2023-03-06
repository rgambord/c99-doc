.. _9899_7.19.10.2:

7.19.10.2 The feof function
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.10.2p1:

.. container:: snum

   :ref:`1 <9899_7.19.10.2p1>`



::

    #include <stdio.h>
    int feof(FILE *stream);

.. rubric:: Description

.. _9899_7.19.10.2p2:

.. container:: snum

   :ref:`2 <9899_7.19.10.2p2>`

The feof function tests the end-of-file indicator for the stream pointed to by stream.

.. rubric:: Returns

.. _9899_7.19.10.2p3:

.. container:: snum

   :ref:`3 <9899_7.19.10.2p3>`

The feof function returns nonzero if and only if the end-of-file indicator is set for stream.

