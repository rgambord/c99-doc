.. _9899_7.20.1.4:

7.20.1.4 The strtol, strtoll, strtoul, and strtoull functions
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.1.4p1:

.. container:: snum

   :ref:`1 <9899_7.20.1.4p1>`



::

    #include <stdlib.h>
    long int strtol(
         const char * restrict nptr,
         char ** restrict endptr,
         int base);
    long long int strtoll(
         const char * restrict nptr,
         char ** restrict endptr,
         int base);
    unsigned long int strtoul(
         const char * restrict nptr,
         char ** restrict endptr,
         int base);
    unsigned long long int strtoull(
         const char * restrict nptr,
         char ** restrict endptr,
         int base);

.. rubric:: Description

.. _9899_7.20.1.4p2:

.. container:: snum

   :ref:`2 <9899_7.20.1.4p2>`

The strtol, strtoll, strtoul, and strtoull functions convert the initial portion of the string pointed to by nptr to long int, long long int, unsigned long int, and unsigned long long int representation, respectively. First, they decompose the input string into three parts: an initial, possibly empty, sequence of white-space characters (as specified by the isspace function), a subject sequence resembling an integer represented in some radix determined by the value of base, and a final string of one or more unrecognized characters, including the terminating null character of the input string. Then, they attempt to convert the subject sequence to an integer, and return the result.

.. _9899_7.20.1.4p3:

.. container:: snum

   :ref:`3 <9899_7.20.1.4p3>`

If the value of base is zero, the expected form of the subject sequence is that of an integer constant as described in :ref:`6.4.4.1 <9899_6.4.4.1>`, optionally preceded by a plus or minus sign, but not including an integer suffix. If the value of base is between 2 and 36 (inclusive), the expected form of the subject sequence is a sequence of letters and digits representing an integer with the radix specified by base, optionally preceded by a plus or minus sign, but not including an integer suffix. The letters from a (or A) through z (or Z) are ascribed the values 10 through 35; only letters and digits whose ascribed values are less than that of base are permitted. If the value of base is 16, the characters 0x or 0X may optionally precede the sequence of letters and digits, following the sign if present.

.. _9899_7.20.1.4p4:

.. container:: snum

   :ref:`4 <9899_7.20.1.4p4>`

The subject sequence is defined as the longest initial subsequence of the input string, starting with the first non-white-space character, that is of the expected form. The subject sequence contains no characters if the input string is empty or consists entirely of white space, or if the first non-white-space character is other than a sign or a permissible letter or digit.

.. _9899_7.20.1.4p5:

.. container:: snum

   :ref:`5 <9899_7.20.1.4p5>`

If the subject sequence has the expected form and the value of base is zero, the sequence of characters starting with the first digit is interpreted as an integer constant according to the rules of :ref:`6.4.4.1 <9899_6.4.4.1>`. If the subject sequence has the expected form and the value of base is between 2 and 36, it is used as the base for conversion, ascribing to each letter its value as given above. If the subject sequence begins with a minus sign, the value resulting from the conversion is negated (in the return type). A pointer to the final string is stored in the object pointed to by endptr, provided that endptr is not a null pointer.

.. _9899_7.20.1.4p6:

.. container:: snum

   :ref:`6 <9899_7.20.1.4p6>`

In other than the "C" locale, additional locale-specific subject sequence forms may be accepted.

.. _9899_7.20.1.4p7:

.. container:: snum

   :ref:`7 <9899_7.20.1.4p7>`

If the subject sequence is empty or does not have the expected form, no conversion is performed; the value of nptr is stored in the object pointed to by endptr, provided that endptr is not a null pointer.

.. rubric:: Returns

.. _9899_7.20.1.4p8:

.. container:: snum

   :ref:`8 <9899_7.20.1.4p8>`

The strtol, strtoll, strtoul, and strtoull functions return the converted value, if any. If no conversion could be performed, zero is returned. If the correct value is outside the range of representable values, LONG_MIN, LONG_MAX, LLONG_MIN, LLONG_MAX, ULONG_MAX, or ULLONG_MAX is returned (according to the return type and sign of the value, if any), and the value of the macro ERANGE is stored in errno.

