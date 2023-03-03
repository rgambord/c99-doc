.. _9899_7.24.4.1.2:

7.24.4.1.2 The wcstol, wcstoll, wcstoul, and wcstoull functions
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.4.1.2p1:

:ref:`1 <9899_7.24.4.1.2p1>`

::

    #include <wchar.h>
    long int wcstol(
         const wchar_t * restrict nptr,
         wchar_t ** restrict endptr,
         int base);
    long long int wcstoll(
         const wchar_t * restrict nptr,
         wchar_t ** restrict endptr,
         int base);
    unsigned long int wcstoul(
         const wchar_t * restrict nptr,
         wchar_t ** restrict endptr,
         int base);
    unsigned long long int wcstoull(
         const wchar_t * restrict nptr,
         wchar_t ** restrict endptr,
         int base);

.. rubric:: Description

.. _9899_7.24.4.1.2p2:

:ref:`2 <9899_7.24.4.1.2p2>` The wcstol, wcstoll, wcstoul, and wcstoull functions convert the initial portion of the wide string pointed to by nptr to long int, long long int, unsigned long int, and unsigned long long int representation, respectively. First, they decompose the input string into three parts: an initial, possibly empty, sequence of white-space wide characters (as specified by the iswspace function), a subject sequence resembling an integer represented in some radix determined by the value of base, and a final wide string of one or more unrecognized wide characters, including the terminating null wide character of the input wide string. Then, they attempt to convert the subject sequence to an integer, and return the result.

.. _9899_7.24.4.1.2p3:

:ref:`3 <9899_7.24.4.1.2p3>` If the value of base is zero, the expected form of the subject sequence is that of an integer constant as described for the corresponding single-byte characters in :ref:`6.4.4.1 <9899_6.4.4.1>`, optionally preceded by a plus or minus sign, but not including an integer suffix. If the value of base is between 2 and 36 (inclusive), the expected form of the subject sequence is a sequence of letters and digits representing an integer with the radix specified by base, optionally preceded by a plus or minus sign, but not including an integer suffix. The letters from a (or A) through z (or Z) are ascribed the values 10 through 35; only letters and digits whose ascribed values are less than that of base are permitted. If the value of base is 16, the wide characters 0x or 0X may optionally precede the sequence of letters and digits, following the sign if present.

.. _9899_7.24.4.1.2p4:

:ref:`4 <9899_7.24.4.1.2p4>` The subject sequence is defined as the longest initial subsequence of the input wide string, starting with the first non-white-space wide character, that is of the expected form. The subject sequence contains no wide characters if the input wide string is empty or consists entirely of white space, or if the first non-white-space wide character is other than a sign or a permissible letter or digit.

.. _9899_7.24.4.1.2p5:

:ref:`5 <9899_7.24.4.1.2p5>` If the subject sequence has the expected form and the value of base is zero, the sequence of wide characters starting with the first digit is interpreted as an integer constant according to the rules of :ref:`6.4.4.1 <9899_6.4.4.1>`. If the subject sequence has the expected form and the value of base is between 2 and 36, it is used as the base for conversion, ascribing to each letter its value as given above. If the subject sequence begins with a minus sign, the value resulting from the conversion is negated (in the return type). A pointer to the final wide string is stored in the object pointed to by endptr, provided that endptr is not a null pointer.

.. _9899_7.24.4.1.2p6:

:ref:`6 <9899_7.24.4.1.2p6>` In other than the "C" locale, additional locale-specific subject sequence forms may be accepted.

.. _9899_7.24.4.1.2p7:

:ref:`7 <9899_7.24.4.1.2p7>` If the subject sequence is empty or does not have the expected form, no conversion is performed; the value of nptr is stored in the object pointed to by endptr, provided that endptr is not a null pointer.

.. rubric:: Returns

.. _9899_7.24.4.1.2p8:

:ref:`8 <9899_7.24.4.1.2p8>` The wcstol, wcstoll, wcstoul, and wcstoull functions return the converted value, if any. If no conversion could be performed, zero is returned. If the correct value is outside the range of representable values, LONG_MIN, LONG_MAX, LLONG_MIN, LLONG_MAX, ULONG_MAX, or ULLONG_MAX is returned (according to the return type sign of the value, if any), and the value of the macro ERANGE is stored in errno.

