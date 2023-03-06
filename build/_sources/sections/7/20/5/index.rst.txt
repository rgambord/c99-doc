.. _9899_7.20.5:

7.20.5 Searching and sorting utilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index


.. _9899_7.20.5p1:

.. container:: snum

   :ref:`1 <9899_7.20.5p1>`

These utilities make use of a comparison function to search or sort arrays of unspecified type. Where an argument declared as size_t nmemb specifies the length of the array for a function, nmemb can have the value zero on a call to that function; the comparison function is not called, a search finds no matching element, and sorting performs no rearrangement. Pointer arguments on such a call shall still have valid values, as described in :ref:`7.1.4 <9899_7.1.4>`.

.. _9899_7.20.5p2:

.. container:: snum

   :ref:`2 <9899_7.20.5p2>`

The implementation shall ensure that the second argument of the comparison function (when called from bsearch), or both arguments (when called from qsort), are pointers to elements of the array.\ [#9899_note263]_ The first argument when called from bsearch shall equal key.

.. _9899_7.20.5p3:

.. container:: snum

   :ref:`3 <9899_7.20.5p3>`

The comparison function shall not alter the contents of the array. The implementation may reorder elements of the array between calls to the comparison function, but shall not alter the contents of any individual element.

.. _9899_7.20.5p4:

.. container:: snum

   :ref:`4 <9899_7.20.5p4>`

When the same objects (consisting of size bytes, irrespective of their current positions in the array) are passed more than once to the comparison function, the results shall be consistent with one another. That is, for qsort they shall define a total ordering on the array, and for bsearch the same object shall always compare the same way with the key.

.. _9899_7.20.5p5:

.. container:: snum

   :ref:`5 <9899_7.20.5p5>`

A sequence point occurs immediately before and immediately after each call to the comparison function, and also between any call to the comparison function and any movement of the objects passed as arguments to that call.



::

    ((char *)p - (char *)base) % size == 0
    (char *)p >= (char *)base
    (char *)p < (char *)base + nmemb * size



.. rubric:: Footnotes

.. [#9899_note263] That is, if the value passed is p, then the following expressions are always nonzero:
