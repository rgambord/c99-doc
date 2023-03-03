.. _9899_7.20.8.1:

7.20.8.1 The mbstowcs function
''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.8.1p1:

:ref:`1 <9899_7.20.8.1p1>`

::

    #include <stdlib.h>
    size_t mbstowcs(wchar_t * restrict pwcs,
         const char * restrict s,
         size_t n);

.. rubric:: Description

.. _9899_7.20.8.1p2:

:ref:`2 <9899_7.20.8.1p2>` The mbstowcs function converts a sequence of multibyte characters that begins in the initial shift state from the array pointed to by s into a sequence of corresponding wide characters and stores not more than n wide characters into the array pointed to by pwcs. No multibyte characters that follow a null character (which is converted into a null wide character) will be examined or converted. Each multibyte character is converted as if by a call to the mbtowc function, except that the conversion state of the mbtowc function is not affected.

.. _9899_7.20.8.1p3:

:ref:`3 <9899_7.20.8.1p3>` No more than n elements will be modified in the array pointed to by pwcs. If copying takes place between objects that overlap, the behavior is undefined.

.. rubric:: Returns

.. _9899_7.20.8.1p4:

:ref:`4 <9899_7.20.8.1p4>` If an invalid multibyte character is encountered, the mbstowcs function returns (size_t)(-1). Otherwise, the mbstowcs function returns the number of array elements modified, not including a terminating null wide character, if any.\ [#9899_note267]_





.. rubric:: Footnotes

.. [#9899_note267] The array will not be null-terminated if the value returned is n.
