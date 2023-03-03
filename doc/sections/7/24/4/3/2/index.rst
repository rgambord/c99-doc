.. _9899_7.24.4.3.2:

7.24.4.3.2 The wcsncat function
"""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.4.3.2p1:

:ref:`1 <9899_7.24.4.3.2p1>`

::

    #include <wchar.h>
    wchar_t *wcsncat(wchar_t * restrict s1,
         const wchar_t * restrict s2,
         size_t n);

.. rubric:: Description

.. _9899_7.24.4.3.2p2:

:ref:`2 <9899_7.24.4.3.2p2>` The wcsncat function appends not more than n wide characters (a null wide character and those that follow it are not appended) from the array pointed to by s2 to the end of the wide string pointed to by s1. The initial wide character of s2 overwrites the null wide character at the end of s1. A terminating null wide character is always appended to the result.\ [#9899_note298]_

.. rubric:: Returns

.. _9899_7.24.4.3.2p3:

:ref:`3 <9899_7.24.4.3.2p3>` The wcsncat function returns the value of s1.





.. rubric:: Footnotes

.. [#9899_note298] Thus, the maximum number of wide characters that can end up in the array pointed to by s1 is wcslen(s1)+n+1.
