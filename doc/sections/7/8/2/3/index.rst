.. _9899_7.8.2.3:

7.8.2.3 The strtoimax and strtoumax functions
'''''''''''''''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.8.2.3p1:

:ref:`1 <9899_7.8.2.3p1>`

::

    #include <inttypes.h>
    intmax_t strtoimax(const char * restrict nptr,
         char ** restrict endptr, int base);
    uintmax_t strtoumax(const char * restrict nptr,
         char ** restrict endptr, int base);

.. rubric:: Description

.. _9899_7.8.2.3p2:

:ref:`2 <9899_7.8.2.3p2>` The strtoimax and strtoumax functions are equivalent to the strtol, strtoll, strtoul, and strtoull functions, except that the initial portion of the string is converted to intmax_t and uintmax_t representation, respectively.

.. rubric:: Returns

.. _9899_7.8.2.3p3:

:ref:`3 <9899_7.8.2.3p3>` The strtoimax and strtoumax functions return the converted value, if any. If no conversion could be performed, zero is returned. If the correct value is outside the range of representable values, INTMAX_MAX, INTMAX_MIN, or UINTMAX_MAX is returned (according to the return type and sign of the value, if any), and the value of the macro ERANGE is stored in errno.

**Forward references**: the strtol, strtoll, strtoul, and strtoull functions (:ref:`7.20.1.4 <9899_7.20.1.4>`).

