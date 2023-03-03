.. _9899_7.11.1.1:

7.11.1.1 The setlocale function
'''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.11.1.1p1:

:ref:`1 <9899_7.11.1.1p1>`

::

    #include <locale.h>
    char *setlocale(int category, const char *locale);

.. rubric:: Description

.. _9899_7.11.1.1p2:

:ref:`2 <9899_7.11.1.1p2>` The setlocale function selects the appropriate portion of the program's locale as specified by the category and locale arguments. The setlocale function may be used to change or query the program's entire current locale or portions thereof. The value LC_ALL for category names the program's entire locale; the other values for category name only a portion of the program's locale. LC_COLLATE affects the behavior of the strcoll and strxfrm functions. LC_CTYPE affects the behavior of the character handling functions\ [#9899_note196]_ and the multibyte and wide character functions. LC_MONETARY affects the monetary formatting information returned by the localeconv function. LC_NUMERIC affects the decimal-point character for the formatted input/output functions and the string conversion functions, as well as the nonmonetary formatting information returned by the localeconv function. LC_TIME affects the behavior of the strftime and wcsftime functions.

.. _9899_7.11.1.1p3:

:ref:`3 <9899_7.11.1.1p3>` A value of "C" for locale specifies the minimal environment for C translation; a value of "" for locale specifies the locale-specific native environment. Other implementation-defined strings may be passed as the second argument to setlocale.

.. _9899_7.11.1.1p4:

:ref:`4 <9899_7.11.1.1p4>` At program startup, the equivalent of

::

    setlocale(LC_ALL, "C");

is executed.

.. _9899_7.11.1.1p5:

:ref:`5 <9899_7.11.1.1p5>` The implementation shall behave as if no library function calls the setlocale function.

.. rubric:: Returns

.. _9899_7.11.1.1p6:

:ref:`6 <9899_7.11.1.1p6>` If a pointer to a string is given for locale and the selection can be honored, the setlocale function returns a pointer to the string associated with the specified category for the new locale. If the selection cannot be honored, the setlocale function returns a null pointer and the program's locale is not changed.

.. _9899_7.11.1.1p7:

:ref:`7 <9899_7.11.1.1p7>` A null pointer for locale causes the setlocale function to return a pointer to the string associated with the category for the program's current locale; the program's locale is not changed.\ [#9899_note197]_

.. _9899_7.11.1.1p8:

:ref:`8 <9899_7.11.1.1p8>` The pointer to string returned by the setlocale function is such that a subsequent call with that string value and its associated category will restore that part of the program's locale. The string pointed to shall not be modified by the program, but may be overwritten by a subsequent call to the setlocale function.

**Forward references**: formatted input/output functions (:ref:`7.19.6 <9899_7.19.6>`), multibyte/wide character conversion functions (:ref:`7.20.7 <9899_7.20.7>`), multibyte/wide string conversion functions (:ref:`7.20.8 <9899_7.20.8>`), numeric conversion functions (:ref:`7.20.1 <9899_7.20.1>`), the strcoll function (:ref:`7.21.4.3 <9899_7.21.4.3>`), the strftime function (:ref:`7.23.3.5 <9899_7.23.3.5>`), the strxfrm function (:ref:`7.21.4.5 <9899_7.21.4.5>`).






.. rubric:: Footnotes

.. [#9899_note196] The only functions in :ref:`7.4 <9899_7.4>` whose behavior is not affected by the current locale are isdigit and isxdigit.
.. [#9899_note197] The implementation shall arrange to encode in a string the various categories due to a heterogeneous locale when category has the value LC_ALL.
