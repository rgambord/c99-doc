.. _9899_7.25.3.2.2:

7.25.3.2.2 The wctrans function
"""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.25.3.2.2p1:

.. container:: snum

   :ref:`1 <9899_7.25.3.2.2p1>`



::

    #include <wctype.h>
    wctrans_t wctrans(const char *property);

.. rubric:: Description

.. _9899_7.25.3.2.2p2:

.. container:: snum

   :ref:`2 <9899_7.25.3.2.2p2>`

The wctrans function constructs a value with type wctrans_t that describes a mapping between wide characters identified by the string argument property.

.. _9899_7.25.3.2.2p3:

.. container:: snum

   :ref:`3 <9899_7.25.3.2.2p3>`

The strings listed in the description of the towctrans function shall be valid in all locales as property arguments to the wctrans function.

.. rubric:: Returns

.. _9899_7.25.3.2.2p4:

.. container:: snum

   :ref:`4 <9899_7.25.3.2.2p4>`

If property identifies a valid mapping of wide characters according to the LC_CTYPE category of the current locale, the wctrans function returns a nonzero value that is valid as the second argument to the towctrans function; otherwise, it returns zero.

