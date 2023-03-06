.. _9899_7.25.2.1.1:

7.25.2.1.1 The iswalnum function
""""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.25.2.1.1p1:

.. container:: snum

   :ref:`1 <9899_7.25.2.1.1p1>`



::

    #include <wctype.h>
    int iswalnum(wint_t wc);

.. rubric:: Description

.. _9899_7.25.2.1.1p2:

.. container:: snum

   :ref:`2 <9899_7.25.2.1.1p2>`

The iswalnum function tests for any wide character for which iswalpha or iswdigit is true.

