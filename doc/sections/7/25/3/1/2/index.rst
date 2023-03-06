.. _9899_7.25.3.1.2:

7.25.3.1.2 The towupper function
""""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.25.3.1.2p1:

.. container:: snum

   :ref:`1 <9899_7.25.3.1.2p1>`



::

    #include <wctype.h>
    wint_t towupper(wint_t wc);

.. rubric:: Description

.. _9899_7.25.3.1.2p2:

.. container:: snum

   :ref:`2 <9899_7.25.3.1.2p2>`

The towupper function converts a lowercase letter to a corresponding uppercase letter.

.. rubric:: Returns

.. _9899_7.25.3.1.2p3:

.. container:: snum

   :ref:`3 <9899_7.25.3.1.2p3>`

If the argument is a wide character for which iswlower is true and there are one or more corresponding wide characters, as specified by the current locale, for which iswupper is true, the towupper function returns one of the corresponding wide characters (always the same one for any given locale); otherwise, the argument is returned unchanged.

