.. _9899_7.25.3.2.1:

7.25.3.2.1 The towctrans function
"""""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.25.3.2.1p1:

.. container:: snum

   :ref:`1 <9899_7.25.3.2.1p1>`



::

    #include <wctype.h>
    wint_t towctrans(wint_t wc, wctrans_t desc);

.. rubric:: Description

.. _9899_7.25.3.2.1p2:

.. container:: snum

   :ref:`2 <9899_7.25.3.2.1p2>`

The towctrans function maps the wide character wc using the mapping described by desc. The current setting of the LC_CTYPE category shall be the same as during the call to wctrans that returned the value desc.

.. _9899_7.25.3.2.1p3:

.. container:: snum

   :ref:`3 <9899_7.25.3.2.1p3>`

Each of the following expressions behaves the same as the call to the wide character case mapping function (:ref:`7.25.3.1 <9899_7.25.3.1>`) in the comment that follows the expression:

::

    towctrans(wc, wctrans("tolower"))                      // towlower(wc)
    towctrans(wc, wctrans("toupper"))                      // towupper(wc)

.. rubric:: Returns

.. _9899_7.25.3.2.1p4:

.. container:: snum

   :ref:`4 <9899_7.25.3.2.1p4>`

The towctrans function returns the mapped value of wc using the mapping described by desc.

