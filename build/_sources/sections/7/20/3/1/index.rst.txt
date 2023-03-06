.. _9899_7.20.3.1:

7.20.3.1 The calloc function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.3.1p1:

.. container:: snum

   :ref:`1 <9899_7.20.3.1p1>`



::

    #include <stdlib.h>
    void *calloc(size_t nmemb, size_t size);

.. rubric:: Description

.. _9899_7.20.3.1p2:

.. container:: snum

   :ref:`2 <9899_7.20.3.1p2>`

The calloc function allocates space for an array of nmemb objects, each of whose size is size. The space is initialized to all bits zero.\ [#9899_note261]_

.. rubric:: Returns

.. _9899_7.20.3.1p3:

.. container:: snum

   :ref:`3 <9899_7.20.3.1p3>`

The calloc function returns either a null pointer or a pointer to the allocated space.





.. rubric:: Footnotes

.. [#9899_note261] Note that this need not be the same as the representation of floating-point zero or a null pointer constant.
