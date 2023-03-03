.. _9899_7.24.4.1.1:

7.24.4.1.1 The wcstod, wcstof, and wcstold functions
""""""""""""""""""""""""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.4.1.1p1:

:ref:`1 <9899_7.24.4.1.1p1>`

::

    #include <wchar.h>
    double wcstod(const wchar_t * restrict nptr,
         wchar_t ** restrict endptr);
    float wcstof(const wchar_t * restrict nptr,
         wchar_t ** restrict endptr);
    long double wcstold(const wchar_t * restrict nptr,
         wchar_t ** restrict endptr);

.. rubric:: Description

.. _9899_7.24.4.1.1p2:

:ref:`2 <9899_7.24.4.1.1p2>` The wcstod, wcstof, and wcstold functions convert the initial portion of the wide string pointed to by nptr to double, float, and long double representation, respectively. First, they decompose the input string into three parts: an initial, possibly empty, sequence of white-space wide characters (as specified by the iswspace function), a subject sequence resembling a floating-point constant or representing an infinity or NaN; and a final wide string of one or more unrecognized wide characters, including the terminating null wide character of the input wide string. Then, they attempt to convert the subject sequence to a floating-point number, and return the result.

.. _9899_7.24.4.1.1p3:

:ref:`3 <9899_7.24.4.1.1p3>` The expected form of the subject sequence is an optional plus or minus sign, then one of the following:

-  a nonempty sequence of decimal digits optionally containing a decimal-point wide character, then an optional exponent part as defined for the corresponding single-byte characters in :ref:`6.4.4.2 <9899_6.4.4.2>`;

-  a 0x or 0X, then a nonempty sequence of hexadecimal digits optionally containing a decimal-point wide character, then an optional binary exponent part as defined in :ref:`6.4.4.2 <9899_6.4.4.2>`;

-  INF or INFINITY, or any other wide string equivalent except for case

-  NAN or NAN(n-wchar-sequence\ :sub:`opt`), or any other wide string equivalent except for case in the NAN part, where:

::

    n-wchar-sequence:
          digit
          nondigit
          n-wchar-sequence digit
          n-wchar-sequence nondigit

The subject sequence is defined as the longest initial subsequence of the input wide string, starting with the first non-white-space wide character, that is of the expected form. The subject sequence contains no wide characters if the input wide string is not of the expected form.

.. _9899_7.24.4.1.1p4:

:ref:`4 <9899_7.24.4.1.1p4>` If the subject sequence has the expected form for a floating-point number, the sequence of wide characters starting with the first digit or the decimal-point wide character (whichever occurs first) is interpreted as a floating constant according to the rules of :ref:`6.4.4.2 <9899_6.4.4.2>`, except that the decimal-point wide character is used in place of a period, and that if neither an exponent part nor a decimal-point wide character appears in a decimal floating point number, or if a binary exponent part does not appear in a hexadecimal floating point number, an exponent part of the appropriate type with value zero is assumed to follow the last digit in the string. If the subject sequence begins with a minus sign, the sequence is interpreted as negated.\ [#9899_note294]_ A wide character sequence INF or INFINITY is interpreted as an infinity, if representable in the return type, else like a floating constant that is too large for the range of the return type. A wide character sequence NAN or NAN(n-wchar-sequence\ :sub:`opt`) is interpreted as a quiet NaN, if supported in the return type, else like a subject sequence part that does not have the expected form; the meaning of the n-wchar sequences is implementation-defined.\ `295) <note295>` A pointer to the final wide string is stored in the object pointed to by endptr, provided that endptr is not a null pointer.

.. _9899_7.24.4.1.1p5:

:ref:`5 <9899_7.24.4.1.1p5>` If the subject sequence has the hexadecimal form and FLT_RADIX is a power of 2, the value resulting from the conversion is correctly rounded.

.. _9899_7.24.4.1.1p6:

:ref:`6 <9899_7.24.4.1.1p6>` In other than the "C" locale, additional locale-specific subject sequence forms may be accepted.

.. _9899_7.24.4.1.1p7:

:ref:`7 <9899_7.24.4.1.1p7>` If the subject sequence is empty or does not have the expected form, no conversion is performed; the value of nptr is stored in the object pointed to by endptr, provided that endptr is not a null pointer.

.. rubric:: Recommended practice

.. _9899_7.24.4.1.1p8:

:ref:`8 <9899_7.24.4.1.1p8>` If the subject sequence has the hexadecimal form, FLT_RADIX is not a power of 2, and the result is not exactly representable, the result should be one of the two numbers in the appropriate internal format that are adjacent to the hexadecimal floating source value, with the extra stipulation that the error should have a correct sign for the current rounding direction.

.. _9899_7.24.4.1.1p9:

:ref:`9 <9899_7.24.4.1.1p9>` If the subject sequence has the decimal form and at most DECIMAL_DIG (defined in :ref:`\<float.h> <9899_7.7>`) significant digits, the result should be correctly rounded. If the subject sequence D has the decimal form and more than DECIMAL_DIG significant digits, consider the two bounding, adjacent decimal strings L and U, both having DECIMAL_DIG significant digits, such that the values of L, D, and U satisfy L \<= D <= U. The result should be one of the (equal or adjacent) values that would be obtained by correctly rounding L and U according to the current rounding direction, with the extra stipulation that the error with respect to D should have a correct sign for the current rounding direction.\ [#9899_note296]_

.. rubric:: Returns

.. _9899_7.24.4.1.1p10:

:ref:`10 <9899_7.24.4.1.1p10>` The functions return the converted value, if any. If no conversion could be performed, zero is returned. If the correct value is outside the range of representable values, plus or minus HUGE_VAL, HUGE_VALF, or HUGE_VALL is returned (according to the return type and sign of the value), and the value of the macro ERANGE is stored in errno. If the result underflows (:ref:`7.12.1 <9899_7.12.1>`), the functions return a value whose magnitude is no greater than the smallest normalized positive number in the return type; whether errno acquires the value ERANGE is implementation-defined.







.. rubric:: Footnotes

.. [#9899_note294] It is unspecified whether a minus-signed sequence is converted to a negative number directly or by negating the value resulting from converting the corresponding unsigned sequence (see :ref:`F.5 <9899_F.5>`); the two methods may yield different results if rounding is toward positive or negative infinity. In either case, the functions honor the sign of zero if floating-point arithmetic supports signed zeros.
.. [#9899_note296] DECIMAL_DIG, defined in :ref:`\<float.h> <9899_7.7>`, should be sufficiently large that L and U will usually round to the same internal floating value, but if not will round to adjacent values.
