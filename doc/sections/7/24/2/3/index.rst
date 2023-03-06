.. _9899_7.24.2.3:

7.24.2.3 The swprintf function
''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.24.2.3p1:

.. container:: snum

   :ref:`1 <9899_7.24.2.3p1>`



::

    #include <wchar.h>
    int swprintf(wchar_t * restrict s,
         size_t n,
         const wchar_t * restrict format, ...);

.. rubric:: Description

.. _9899_7.24.2.3p2:

.. container:: snum

   :ref:`2 <9899_7.24.2.3p2>`

The swprintf function is equivalent to fwprintf, except that the argument s specifies an array of wide characters into which the generated output is to be written, rather than written to a stream. No more than n wide characters are written, including a terminating null wide character, which is always added (unless n is zero).

.. rubric:: Returns

.. _9899_7.24.2.3p3:

.. container:: snum

   :ref:`3 <9899_7.24.2.3p3>`

The swprintf function returns the number of wide characters written in the array, not counting the terminating null wide character, or a negative value if an encoding error occurred or if n or more wide characters were requested to be written.

