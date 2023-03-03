.. _9899_7.20.5.1:

7.20.5.1 The bsearch function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.5.1p1:

:ref:`1 <9899_7.20.5.1p1>`

::

    #include <stdlib.h>
    void *bsearch(const void *key, const void *base,
         size_t nmemb, size_t size,
         int (*compar)(const void *, const void *));

.. rubric:: Description

.. _9899_7.20.5.1p2:

:ref:`2 <9899_7.20.5.1p2>` The bsearch function searches an array of nmemb objects, the initial element of which is pointed to by base, for an element that matches the object pointed to by key. The size of each element of the array is specified by size.

.. _9899_7.20.5.1p3:

:ref:`3 <9899_7.20.5.1p3>` The comparison function pointed to by compar is called with two arguments that point to the key object and to an array element, in that order. The function shall return an integer less than, equal to, or greater than zero if the key object is considered, respectively, to be less than, to match, or to be greater than the array element. The array shall consist of: all the elements that compare less than, all the elements that compare equal to, and all the elements that compare greater than the key object, in that order.\ [#9899_note264]_

.. rubric:: Returns

.. _9899_7.20.5.1p4:

:ref:`4 <9899_7.20.5.1p4>` The bsearch function returns a pointer to a matching element of the array, or a null pointer if no match is found. If two elements compare as equal, which element is matched is unspecified.





.. rubric:: Footnotes

.. [#9899_note264] In practice, the entire array is sorted according to the comparison function.
