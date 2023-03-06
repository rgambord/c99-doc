.. _9899_7.24.4.2.2:

7.24.4.2.2 The wcsncpy function
"""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.4.2.2p1:

.. container:: snum

   :ref:`1 <9899_7.24.4.2.2p1>`



::

    #include <wchar.h>
    wchar_t *wcsncpy(wchar_t * restrict s1,
         const wchar_t * restrict s2,
         size_t n);

.. rubric:: Description

.. _9899_7.24.4.2.2p2:

.. container:: snum

   :ref:`2 <9899_7.24.4.2.2p2>`

The wcsncpy function copies not more than n wide characters (those that follow a null wide character are not copied) from the array pointed to by s2 to the array pointed to by s1.\ [#9899_note297]_

.. _9899_7.24.4.2.2p3:

.. container:: snum

   :ref:`3 <9899_7.24.4.2.2p3>`

If the array pointed to by s2 is a wide string that is shorter than n wide characters, null wide characters are appended to the copy in the array pointed to by s1, until n wide characters in all have been written.

.. rubric:: Returns

.. _9899_7.24.4.2.2p4:

.. container:: snum

   :ref:`4 <9899_7.24.4.2.2p4>`

The wcsncpy function returns the value of s1.





.. rubric:: Footnotes

.. [#9899_note297] Thus, if there is no null wide character in the first n wide characters of the array pointed to by s2, the result will not be null-terminated.
