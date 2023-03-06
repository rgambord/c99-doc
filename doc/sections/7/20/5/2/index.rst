.. _9899_7.20.5.2:

7.20.5.2 The qsort function
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.5.2p1:

.. container:: snum

   :ref:`1 <9899_7.20.5.2p1>`



::

    #include <stdlib.h>
    void qsort(void *base, size_t nmemb, size_t size,
         int (*compar)(const void *, const void *));

.. rubric:: Description

.. _9899_7.20.5.2p2:

.. container:: snum

   :ref:`2 <9899_7.20.5.2p2>`

The qsort function sorts an array of nmemb objects, the initial element of which is pointed to by base. The size of each object is specified by size.

.. _9899_7.20.5.2p3:

.. container:: snum

   :ref:`3 <9899_7.20.5.2p3>`

The contents of the array are sorted into ascending order according to a comparison function pointed to by compar, which is called with two arguments that point to the objects being compared. The function shall return an integer less than, equal to, or greater than zero if the first argument is considered to be respectively less than, equal to, or greater than the second.

.. _9899_7.20.5.2p4:

.. container:: snum

   :ref:`4 <9899_7.20.5.2p4>`

If two elements compare as equal, their order in the resulting sorted array is unspecified.

.. rubric:: Returns

.. _9899_7.20.5.2p5:

.. container:: snum

   :ref:`5 <9899_7.20.5.2p5>`

The qsort function returns no value.

