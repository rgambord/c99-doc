.. _9899_7.20.4.1:

7.20.4.1 The abort function
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.4.1p1:

.. container:: snum

   :ref:`1 <9899_7.20.4.1p1>`



::

    #include <stdlib.h>
    void abort(void);

.. rubric:: Description

.. _9899_7.20.4.1p2:

.. container:: snum

   :ref:`2 <9899_7.20.4.1p2>`

The abort function causes abnormal program termination to occur, unless the signal SIGABRT is being caught and the signal handler does not return. Whether open streams with unwritten buffered data are flushed, open streams are closed, or temporary files are removed is implementation-defined. An implementation-defined form of the status unsuccessful termination is returned to the host environment by means of the function call raise(SIGABRT).

.. rubric:: Returns

.. _9899_7.20.4.1p3:

.. container:: snum

   :ref:`3 <9899_7.20.4.1p3>`

The abort function does not return to its caller.

