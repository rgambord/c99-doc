.. _9899_7.12.11.2:

7.12.11.2 The nan functions
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.11.2p1:

:ref:`1 <9899_7.12.11.2p1>`

::

    #include <math.h>
    double nan(const char *tagp);
    float nanf(const char *tagp);
    long double nanl(const char *tagp);

.. rubric:: Description

.. _9899_7.12.11.2p2:

:ref:`2 <9899_7.12.11.2p2>` The call nan("n-char-sequence") is equivalent to strtod("NAN(n-char- sequence)", (char*\*) NULL); the call nan("") is equivalent to strtod("NAN()", (char*\*) NULL). If tagp does not point to an n-char sequence or an empty string, the call is equivalent to strtod("NAN", (char*\*) NULL). Calls to nanf and nanl are equivalent to the corresponding calls to strtof and strtold.

.. rubric:: Returns

.. _9899_7.12.11.2p3:

:ref:`3 <9899_7.12.11.2p3>` The nan functions return a quiet NaN, if available, with content indicated through tagp. If the implementation does not support quiet NaNs, the functions return zero.

**Forward references**: the strtod, strtof, and strtold functions (:ref:`7.20.1.3 <9899_7.20.1.3>`).

