.. _9899_7.11.2.1:

7.11.2.1 The localeconv function
''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.11.2.1p1:

.. container:: snum

   :ref:`1 <9899_7.11.2.1p1>`



::

    #include <locale.h>
    struct lconv *localeconv(void);

.. rubric:: Description

.. _9899_7.11.2.1p2:

.. container:: snum

   :ref:`2 <9899_7.11.2.1p2>`

The localeconv function sets the components of an object with type struct lconv with values appropriate for the formatting of numeric quantities (monetary and otherwise) according to the rules of the current locale.

.. _9899_7.11.2.1p3:

.. container:: snum

   :ref:`3 <9899_7.11.2.1p3>`

The members of the structure with type char \* are pointers to strings, any of which (except decimal_point) can point to "", to indicate that the value is not available in the current locale or is of zero length. Apart from grouping and mon_grouping, the strings shall start and end in the initial shift state. The members with type char are nonnegative numbers, any of which can be CHAR_MAX to indicate that the value is not available in the current locale. The members include the following:

char \*decimal_point
   The decimal-point character used to format nonmonetary quantities.
char \*thousands_sep
   The character used to separate groups of digits before the decimal-point character in formatted nonmonetary quantities.
char \*grouping
   A string whose elements indicate the size of each group of digits in formatted nonmonetary quantities.
char \*mon_decimal_point
   The decimal-point used to format monetary quantities.
char \*mon_thousands_sep
   The separator for groups of digits before the decimal-point in formatted monetary quantities.
char \*mon_grouping
   A string whose elements indicate the size of each group of digits in formatted monetary quantities.
char \*positive_sign
   The string used to indicate a nonnegative-valued formatted monetary quantity.
char \*negative_sign
   The string used to indicate a negative-valued formatted monetary quantity.
char \*currency_symbol
   The local currency symbol applicable to the current locale.
char frac_digits
   The number of fractional digits (those after the decimal-point) to be displayed in a locally formatted monetary quantity.
char p_cs_precedes
   Set to 1 or 0 if the currency_symbol respectively precedes or succeeds the value for a nonnegative locally formatted monetary quantity.
char n_cs_precedes
   Set to 1 or 0 if the currency_symbol respectively precedes or succeeds the value for a negative locally formatted monetary quantity.
char p_sep_by_space
   Set to a value indicating the separation of the currency_symbol, the sign string, and the value for a nonnegative locally formatted monetary quantity.
char n_sep_by_space
   Set to a value indicating the separation of the currency_symbol, the sign string, and the value for a negative locally formatted monetary quantity.
char p_sign_posn
   Set to a value indicating the positioning of the positive_sign for a nonnegative locally formatted monetary quantity.
char n_sign_posn
   Set to a value indicating the positioning of the negative_sign for a negative locally formatted monetary quantity.
char \*int_curr_symbol
   The international currency symbol applicable to the current locale. The first three characters contain the alphabetic international currency symbol in accordance with those specified in ISO 4217. The fourth character (immediately preceding the null character) is the character used to separate the international currency symbol from the monetary quantity.
char int_frac_digits
   The number of fractional digits (those after the decimal-point) to be displayed in an internationally formatted monetary quantity.
char int_p_cs_precedes
   Set to 1 or 0 if the int_curr_symbol respectively precedes or succeeds the value for a nonnegative internationally formatted monetary quantity.
char int_n_cs_precedes
   Set to 1 or 0 if the int_curr_symbol respectively precedes or succeeds the value for a negative internationally formatted monetary quantity.
char int_p_sep_by_space
   Set to a value indicating the separation of the int_curr_symbol, the sign string, and the value for a nonnegative internationally formatted monetary quantity.
char int_n_sep_by_space
   Set to a value indicating the separation of the int_curr_symbol, the sign string, and the value for a negative internationally formatted monetary quantity.
char int_p_sign_posn
   Set to a value indicating the positioning of the positive_sign for a nonnegative internationally formatted monetary quantity.
char int_n_sign_posn
   Set to a value indicating the positioning of the negative_sign for a negative internationally formatted monetary quantity.

.. _9899_7.11.2.1p4:

.. container:: snum

   :ref:`4 <9899_7.11.2.1p4>`

The elements of grouping and mon_grouping are interpreted according to the following:

CHAR_MAX
   No further grouping is to be performed.
0
   The previous element is to be repeatedly used for the remainder of the digits.
other
   The integer value is the number of digits that compose the current group. The next element is examined to determine the size of the next group of digits before the current group.

.. _9899_7.11.2.1p5:

.. container:: snum

   :ref:`5 <9899_7.11.2.1p5>`

The values of p_sep_by_space, n_sep_by_space, int_p_sep_by_space, and int_n_sep_by_space are interpreted according to the following:

0
   No space separates the currency symbol and value.
1
   If the currency symbol and sign string are adjacent, a space separates them from the value; otherwise, a space separates the currency symbol from the value.
2
   If the currency symbol and sign string are adjacent, a space separates them; otherwise, a space separates the sign string from the value.

For int_p_sep_by_space and int_n_sep_by_space, the fourth character of int_curr_symbol is used instead of a space.

.. _9899_7.11.2.1p6:

.. container:: snum

   :ref:`6 <9899_7.11.2.1p6>`

The values of p_sign_posn, n_sign_posn, int_p_sign_posn, and int_n_sign_posn are interpreted according to the following:

0
   Parentheses surround the quantity and currency symbol.
1
   The sign string precedes the quantity and currency symbol.
2
   The sign string succeeds the quantity and currency symbol.
3
   The sign string immediately precedes the currency symbol.
4
   The sign string immediately succeeds the currency symbol.

.. _9899_7.11.2.1p7:

.. container:: snum

   :ref:`7 <9899_7.11.2.1p7>`

The implementation shall behave as if no library function calls the localeconv function.

.. rubric:: Returns

.. _9899_7.11.2.1p8:

.. container:: snum

   :ref:`8 <9899_7.11.2.1p8>`

The localeconv function returns a pointer to the filled-in object. The structure pointed to by the return value shall not be modified by the program, but may be overwritten by a subsequent call to the localeconv function. In addition, calls to the setlocale function with categories LC_ALL, LC_MONETARY, or LC_NUMERIC may overwrite the contents of the structure.

.. _9899_7.11.2.1p9:

.. container:: snum

   :ref:`9 <9899_7.11.2.1p9>`

EXAMPLE 1 The following table illustrates rules which may well be used by four countries to format monetary quantities.

.. code-block:: text

    Local format                                     International format
    
    Country        Positive                  Negative                    Positive               Negative
    
    Country1     1.234,56 mk             -1.234,56 mk                  FIM   1.234,56         FIM -1.234,56
    Country2     L.1.234                 -L.1.234                      ITL   1.234            -ITL 1.234
    Country3     fl. 1.234,56            fl. -1.234,56                 NLG   1.234,56         NLG -1.234,56
    Country4     SFrs.1,234.56           SFrs.1,234.56C                CHF   1,234.56         CHF 1,234.56C

.. _9899_7.11.2.1p10:

.. container:: snum

   :ref:`10 <9899_7.11.2.1p10>`

For these four countries, the respective values for the monetary members of the structure returned by localeconv could be:

.. code-block:: text

    Country1              Country2              Country3            Country4
    
    mon_decimal_point                 ","                   ""                   ","                 "."
    mon_thousands_sep                 "."                   "."                  "."                 ","
    mon_grouping                      "\3"                  "\3"                 "\3"                "\3"
    positive_sign                     ""                    ""                   ""                  ""
    negative_sign                     "-"                   "-"                  "-"                 "C"
    currency_symbol                   "mk"                  "L."                 "\u0192"            "SFrs."
    frac_digits                       2                     0                    2                   2
    p_cs_precedes                     0                     1                    1                   1
    n_cs_precedes                     0                     1                    1                   1
    p_sep_by_space                    1                     0                    1                   0
    n_sep_by_space                    1                     0                    2                   0
    p_sign_posn                       1                     1                    1                   1
    n_sign_posn                       1                     1                    4                   2
    int_curr_symbol                   "FIM "                "ITL "               "NLG "              "CHF "
    int_frac_digits                   2                     0                    2                   2
    int_p_cs_precedes                 1                     1                    1                   1
    int_n_cs_precedes                 1                     1                    1                   1
    int_p_sep_by_space                1                     1                    1                   1
    int_n_sep_by_space                2                     1                    2                   1
    int_p_sign_posn                   1                     1                    1                   1
    int_n_sign_posn                   4                     1                    4                   2

.. _9899_7.11.2.1p11:

.. container:: snum

   :ref:`11 <9899_7.11.2.1p11>`

EXAMPLE 2 The following table illustrates how the cs_precedes, sep_by_space, and sign_posn members affect the formatted value.

.. code-block:: text

    p_sep_by_space
    p_cs_precedes           p_sign_posn          0                   1                  2

               0                    0         (1.25$)            (1.25 $)            (1.25$)
                                    1         +1.25$             +1.25 $             + 1.25$
                                    2         1.25$+             1.25 $+             1.25$ +
                                    3         1.25+$             1.25 +$             1.25+ $
                                    4         1.25$+             1.25 $+             1.25$ +

               1                    0         ($1.25)            ($ 1.25)            ($1.25)
                                    1         +$1.25             +$ 1.25             + $1.25
                                    2         $1.25+             $ 1.25+             $1.25 +
                                    3         +$1.25             +$ 1.25             + $1.25
                                    4         $+1.25             $+ 1.25             $ +1.25

