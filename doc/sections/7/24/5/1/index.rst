.. _9899_7.24.5.1:

7.24.5.1 The wcsftime function
''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.24.5.1p1:

:ref:`1 <9899_7.24.5.1p1>`

::

    #include <time.h>
    #include <wchar.h>
    size_t wcsftime(wchar_t * restrict s,
         size_t maxsize,
         const wchar_t * restrict format,
         const struct tm * restrict timeptr);

.. rubric:: Description

.. _9899_7.24.5.1p2:

:ref:`2 <9899_7.24.5.1p2>` The wcsftime function is equivalent to the strftime function, except that:

-  The argument s points to the initial element of an array of wide characters into which the generated output is to be placed.
-  The argument maxsize indicates the limiting number of wide characters.
-  The argument format is a wide string and the conversion specifiers are replaced by corresponding sequences of wide characters.
-  The return value indicates the number of wide characters.

.. rubric:: Returns

.. _9899_7.24.5.1p3:

:ref:`3 <9899_7.24.5.1p3>` If the total number of resulting wide characters including the terminating null wide character is not more than maxsize, the wcsftime function returns the number of wide characters placed into the array pointed to by s not including the terminating null wide character. Otherwise, zero is returned and the contents of the array are indeterminate.

