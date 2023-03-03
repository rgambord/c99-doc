.. _9899_B.10:

B.10 Localization \<locale.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    struct lconv    LC_ALL            LC_CTYPE          LC_NUMERIC
    NULL            LC_COLLATE        LC_MONETARY       LC_TIME

    char *setlocale(int category, const char *locale);
    struct lconv *localeconv(void);

