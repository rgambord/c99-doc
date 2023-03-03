.. _9899_7.11:

7.11 Localization \<locale.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. toctree::
   :maxdepth: 2

   1/index
   2/index


.. _9899_7.11p1:

:ref:`1 <9899_7.11p1>` The header :ref:`\<locale.h> <9899_7.11>` declares two functions, one type, and defines several macros.

.. _9899_7.11p2:

:ref:`2 <9899_7.11p2>` The type is

::

    struct lconv

which contains members related to the formatting of numeric values. The structure shall contain at least the following members, in any order. The semantics of the members and their normal ranges are explained in :ref:`7.11.2.1 <9899_7.11.2.1>`. In the "C" locale, the members shall have the values specified in the comments.

::

    char   *decimal_point;                 //   "."
    char   *thousands_sep;                 //   ""
    char   *grouping;                      //   ""
    char   *mon_decimal_point;             //   ""
    char   *mon_thousands_sep;             //   ""
    char   *mon_grouping;                  //   ""
    char   *positive_sign;                 //   ""
    char   *negative_sign;                 //   ""
    char   *currency_symbol;               //   ""
    char   frac_digits;                    //   CHAR_MAX
    char   p_cs_precedes;                  //   CHAR_MAX
    char   n_cs_precedes;                  //   CHAR_MAX
    char   p_sep_by_space;                 //   CHAR_MAX
    char   n_sep_by_space;                 //   CHAR_MAX
    char   p_sign_posn;                    //   CHAR_MAX
    char   n_sign_posn;                    //   CHAR_MAX
    char   *int_curr_symbol;               //   ""
    char   int_frac_digits;                //   CHAR_MAX
    char   int_p_cs_precedes;              //   CHAR_MAX
    char   int_n_cs_precedes;              //   CHAR_MAX
    char   int_p_sep_by_space;             //   CHAR_MAX
    char   int_n_sep_by_space;             //   CHAR_MAX
    char   int_p_sign_posn;                //   CHAR_MAX
    char   int_n_sign_posn;                //   CHAR_MAX

.. _9899_7.11p3:

:ref:`3 <9899_7.11p3>` The macros defined are NULL (described in :ref:`7.17 <9899_7.17>`); and

::

    LC_ALL
    LC_COLLATE
    LC_CTYPE
    LC_MONETARY
    LC_NUMERIC
    LC_TIME

which expand to integer constant expressions with distinct values, suitable for use as the first argument to the setlocale function.\ [#9899_note194]_ Additional macro definitions, beginning with the characters LC\_ and an uppercase letter,\ [#9899_note195]_ may also be specified by the implementation.






.. rubric:: Footnotes

.. [#9899_note194] ISO/IEC 9945-2 specifies locale and charmap formats that may be used to specify locales for C.
.. [#9899_note195] See ''future library directions'' (:ref:`7.26.5 <9899_7.26.5>`).
