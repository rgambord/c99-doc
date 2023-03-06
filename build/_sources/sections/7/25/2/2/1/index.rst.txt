.. _9899_7.25.2.2.1:

7.25.2.2.1 The iswctype function
""""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.25.2.2.1p1:

.. container:: snum

   :ref:`1 <9899_7.25.2.2.1p1>`



::

    #include <wctype.h>
    int iswctype(wint_t wc, wctype_t desc);

.. rubric:: Description

.. _9899_7.25.2.2.1p2:

.. container:: snum

   :ref:`2 <9899_7.25.2.2.1p2>`

The iswctype function determines whether the wide character wc has the property described by desc. The current setting of the LC_CTYPE category shall be the same as during the call to wctype that returned the value desc.

.. _9899_7.25.2.2.1p3:

.. container:: snum

   :ref:`3 <9899_7.25.2.2.1p3>`

Each of the following expressions has a truth-value equivalent to the call to the wide character classification function (:ref:`7.25.2.1 <9899_7.25.2.1>`) in the comment that follows the expression:

::

    iswctype(wc,       wctype("alnum"))             //   iswalnum(wc)
    iswctype(wc,       wctype("alpha"))             //   iswalpha(wc)
    iswctype(wc,       wctype("blank"))             //   iswblank(wc)
    iswctype(wc,       wctype("cntrl"))             //   iswcntrl(wc)
    iswctype(wc,       wctype("digit"))             //   iswdigit(wc)
    iswctype(wc,       wctype("graph"))             //   iswgraph(wc)
    iswctype(wc,       wctype("lower"))             //   iswlower(wc)
    iswctype(wc,       wctype("print"))             //   iswprint(wc)
    iswctype(wc,       wctype("punct"))             //   iswpunct(wc)
    iswctype(wc,       wctype("space"))             //   iswspace(wc)
    iswctype(wc,       wctype("upper"))             //   iswupper(wc)
    iswctype(wc,       wctype("xdigit"))            //   iswxdigit(wc)

.. rubric:: Returns

.. _9899_7.25.2.2.1p4:

.. container:: snum

   :ref:`4 <9899_7.25.2.2.1p4>`

The iswctype function returns nonzero (true) if and only if the value of the wide character wc has the property described by desc.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_7.25.2.2.2`

