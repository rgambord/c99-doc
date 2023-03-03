.. _9899_7.21.4.1:

7.21.4.1 The memcmp function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.21.4.1p1:

:ref:`1 <9899_7.21.4.1p1>`

::

    #include <string.h>
    int memcmp(const void *s1, const void *s2, size_t n);

.. rubric:: Description

.. _9899_7.21.4.1p2:

:ref:`2 <9899_7.21.4.1p2>` The memcmp function compares the first n characters of the object pointed to by s1 to the first n characters of the object pointed to by s2.\ [#9899_note271]_

.. rubric:: Returns

.. _9899_7.21.4.1p3:

:ref:`3 <9899_7.21.4.1p3>` The memcmp function returns an integer greater than, equal to, or less than zero, accordingly as the object pointed to by s1 is greater than, equal to, or less than the object pointed to by s2.





.. rubric:: Footnotes

.. [#9899_note271] The contents of ''holes'' used as padding for purposes of alignment within structure objects are indeterminate. Strings shorter than their allocated space and unions may also cause problems in comparison.
