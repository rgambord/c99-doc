.. _9899_7.25.3.1.1:

7.25.3.1.1 The towlower function
""""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.25.3.1.1p1:

.. container:: snum

   :ref:`1 <9899_7.25.3.1.1p1>`



::

    #include <wctype.h>
    wint_t towlower(wint_t wc);

.. rubric:: Description

.. _9899_7.25.3.1.1p2:

.. container:: snum

   :ref:`2 <9899_7.25.3.1.1p2>`

The towlower function converts an uppercase letter to a corresponding lowercase letter.

.. rubric:: Returns

.. _9899_7.25.3.1.1p3:

.. container:: snum

   :ref:`3 <9899_7.25.3.1.1p3>`

If the argument is a wide character for which iswupper is true and there are one or more corresponding wide characters, as specified by the current locale, for which iswlower is true, the towlower function returns one of the corresponding wide characters (always the same one for any given locale); otherwise, the argument is returned unchanged.

