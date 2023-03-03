.. _9899_7.19.6.5:

7.19.6.5 The snprintf function
''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.6.5p1:

:ref:`1 <9899_7.19.6.5p1>`

::

    #include <stdio.h>
    int snprintf(char * restrict s, size_t n,
         const char * restrict format, ...);

.. rubric:: Description

.. _9899_7.19.6.5p2:

:ref:`2 <9899_7.19.6.5p2>` The snprintf function is equivalent to fprintf, except that the output is written into an array (specified by argument s) rather than to a stream. If n is zero, nothing is written, and s may be a null pointer. Otherwise, output characters beyond the n-1st are discarded rather than being written to the array, and a null character is written at the end of the characters actually written into the array. If copying takes place between objects that overlap, the behavior is undefined.

.. rubric:: Returns

.. _9899_7.19.6.5p3:

:ref:`3 <9899_7.19.6.5p3>` The snprintf function returns the number of characters that would have been written had n been sufficiently large, not counting the terminating null character, or a negative value if an encoding error occurred. Thus, the null-terminated output has been completely written if and only if the returned value is nonnegative and less than n.

