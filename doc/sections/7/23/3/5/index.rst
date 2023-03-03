.. _9899_7.23.3.5:

7.23.3.5 The strftime function
''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.23.3.5p1:

:ref:`1 <9899_7.23.3.5p1>`

::

    #include <time.h>
    size_t strftime(char * restrict s,
         size_t maxsize,
         const char * restrict format,
         const struct tm * restrict timeptr);

.. rubric:: Description

.. _9899_7.23.3.5p2:

:ref:`2 <9899_7.23.3.5p2>` The strftime function places characters into the array pointed to by s as controlled by the string pointed to by format. The format shall be a multibyte character sequence, beginning and ending in its initial shift state. The format string consists of zero or more conversion specifiers and ordinary multibyte characters. A conversion specifier consists of a % character, possibly followed by an E or O modifier character (described below), followed by a character that determines the behavior of the conversion specifier. All ordinary multibyte characters (including the terminating null character) are copied unchanged into the array. If copying takes place between objects that overlap, the behavior is undefined. No more than maxsize characters are placed into the array.

.. _9899_7.23.3.5p3:

:ref:`3 <9899_7.23.3.5p3>` Each conversion specifier is replaced by appropriate characters as described in the following list. The appropriate characters are determined using the LC_TIME category of the current locale and by the values of zero or more members of the broken-down time structure pointed to by timeptr, as specified in brackets in the description. If any of the specified values is outside the normal range, the characters stored are unspecified.

%a
   is replaced by the locale's abbreviated weekday name. [tm_wday]
%A
   is replaced by the locale's full weekday name. [tm_wday]
%b
   is replaced by the locale's abbreviated month name. [tm_mon]
%B
   is replaced by the locale's full month name. [tm_mon]
%c
   is replaced by the locale's appropriate date and time representation. [all specified in :ref:`7.23.1 <9899_7.23.1>`]
%C
   is replaced by the year divided by 100 and truncated to an integer, as a decimal number (00-99). [tm_year]
%d
   is replaced by the day of the month as a decimal number (01-31). [tm_mday]
%D
   is equivalent to ''%m/%d/%y''. [tm_mon, tm_mday, tm_year]
%e
   is replaced by the day of the month as a decimal number (1-31); a single digit is preceded by a space. [tm_mday]
%F
   is equivalent to ''%Y-%m-%d'' (the ISO 8601 date format). [tm_year, tm_mon, tm_mday]
%g
   is replaced by the last 2 digits of the week-based year (see below) as a decimal number (00-99). [tm_year, tm_wday, tm_yday]
%G
   is replaced by the week-based year (see below) as a decimal number (e.g., 1997). [tm_year, tm_wday, tm_yday]
%h
   is equivalent to ''%b''. [tm_mon]
%H
   is replaced by the hour (24-hour clock) as a decimal number (00-23). [tm_hour]
%I
   is replaced by the hour (12-hour clock) as a decimal number (01-12). [tm_hour]
%j
   is replaced by the day of the year as a decimal number (001-366). [tm_yday]
%m
   is replaced by the month as a decimal number (01-12). [tm_mon]
%M
   is replaced by the minute as a decimal number (00-59). [tm_min]
%n
   is replaced by a new-line character.
%p
   is replaced by the locale's equivalent of the AM/PM designations associated with a 12-hour clock. [tm_hour]
%r
   is replaced by the locale's 12-hour clock time. [tm_hour, tm_min, tm_sec]
%R
   is equivalent to ''%H:%M''. [tm_hour, tm_min]
%S
   is replaced by the second as a decimal number (00-60). [tm_sec]
%t
   is replaced by a horizontal-tab character.
%T
   is equivalent to ''%H:%M:%S'' (the ISO 8601 time format). [tm_hour, tm_min, tm_sec]
%u
   is replaced by the ISO 8601 weekday as a decimal number (1-7), where Monday is 1. [tm_wday]
%U
   is replaced by the week number of the year (the first Sunday as the first day of week 1) as a decimal number (00-53). [tm_year, tm_wday, tm_yday]
%V
   is replaced by the ISO 8601 week number (see below) as a decimal number (01-53). [tm_year, tm_wday, tm_yday]
%w
   is replaced by the weekday as a decimal number (0-6), where Sunday is 0. [tm_wday]
%W
   is replaced by the week number of the year (the first Monday as the first day of week 1) as a decimal number (00-53). [tm_year, tm_wday, tm_yday]
%x
   is replaced by the locale's appropriate date representation. [all specified in :ref:`7.23.1 <9899_7.23.1>`]
%X
   is replaced by the locale's appropriate time representation. [all specified in :ref:`7.23.1 <9899_7.23.1>`]
%y
   is replaced by the last 2 digits of the year as a decimal number (00-99). [tm_year]
%Y
   is replaced by the year as a decimal number (e.g., 1997). [tm_year]
%z
   is replaced by the offset from UTC in the ISO 8601 format ''-0430'' (meaning 4 hours 30 minutes behind UTC, west of Greenwich), or by no characters if no time zone is determinable. [tm_isdst]
%Z
   is replaced by the locale's time zone name or abbreviation, or by no characters if no time zone is determinable. [tm_isdst]
\%\%
   is replaced by %.

.. _9899_7.23.3.5p4:

:ref:`4 <9899_7.23.3.5p4>` Some conversion specifiers can be modified by the inclusion of an E or O modifier character to indicate an alternative format or specification. If the alternative format or specification does not exist for the current locale, the modifier is ignored.

%Ec
   is replaced by the locale's alternative date and time representation.
%EC
   is replaced by the name of the base year (period) in the locale's alternative representation.
%Ex
   is replaced by the locale's alternative date representation.
%EX
   is replaced by the locale's alternative time representation.
%Ey
   is replaced by the offset from %EC (year only) in the locale's alternative representation.
%EY
   is replaced by the locale's full alternative year representation.
%Od
   is replaced by the day of the month, using the locale's alternative numeric symbols (filled as needed with leading zeros, or with leading spaces if there is no alternative symbol for zero).
%Oe
   is replaced by the day of the month, using the locale's alternative numeric symbols (filled as needed with leading spaces).
%OH
   is replaced by the hour (24-hour clock), using the locale's alternative numeric symbols.
%OI
   is replaced by the hour (12-hour clock), using the locale's alternative numeric symbols.
%Om
   is replaced by the month, using the locale's alternative numeric symbols.
%OM
   is replaced by the minutes, using the locale's alternative numeric symbols.
%OS
   is replaced by the seconds, using the locale's alternative numeric symbols.
%Ou
   is replaced by the ISO 8601 weekday as a number in the locale's alternative representation, where Monday is 1.
%OU
   is replaced by the week number, using the locale's alternative numeric symbols.
%OV
   is replaced by the ISO 8601 week number, using the locale's alternative numeric symbols.
%Ow
   is replaced by the weekday as a number, using the locale's alternative numeric symbols.
%OW
   is replaced by the week number of the year, using the locale's alternative numeric symbols.
%Oy
   is replaced by the last 2 digits of the year, using the locale's alternative numeric symbols.

.. _9899_7.23.3.5p5:

:ref:`5 <9899_7.23.3.5p5>` %g, %G, and %V give values according to the ISO 8601 week-based year. In this system, weeks begin on a Monday and week 1 of the year is the week that includes January 4th, which is also the week that includes the first Thursday of the year, and is also the first week that contains at least four days in the year. If the first Monday of January is the 2nd, 3rd, or 4th, the preceding days are part of the last week of the preceding year; thus, for Saturday 2nd January 1999, %G is replaced by 1998 and %V is replaced by 53. If December 29th, 30th, or 31st is a Monday, it and any following days are part of week 1 of the following year. Thus, for Tuesday 30th December 1997, %G is replaced by 1998 and %V is replaced by 01.

.. _9899_7.23.3.5p6:

:ref:`6 <9899_7.23.3.5p6>` If a conversion specifier is not one of the above, the behavior is undefined.

.. _9899_7.23.3.5p7:

:ref:`7 <9899_7.23.3.5p7>` In the "C" locale, the E and O modifiers are ignored and the replacement strings for the following specifiers are:

%a
   the first three characters of %A.
%A
   one of ''Sunday'', ''Monday'', \.\.\. , ''Saturday''.
%b
   the first three characters of %B.
%B
   one of ''January'', ''February'', \.\.\. , ''December''.
%c
   equivalent to ''%a %b %e %T %Y''.
%p
   one of ''AM'' or ''PM''.
%r
   equivalent to ''%I:%M:%S %p''.
%x
   equivalent to ''%m/%d/%y''.
%X
   equivalent to %T.
%Z
   implementation-defined.

.. rubric:: Returns

.. _9899_7.23.3.5p8:

:ref:`8 <9899_7.23.3.5p8>` If the total number of resulting characters including the terminating null character is not more than maxsize, the strftime function returns the number of characters placed into the array pointed to by s not including the terminating null character. Otherwise, zero is returned and the contents of the array are indeterminate.

