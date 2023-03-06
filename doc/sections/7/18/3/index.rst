.. _9899_7.18.3:

7.18.3 Limits of other integer types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_7.18.3p1:

.. container:: snum

   :ref:`1 <9899_7.18.3p1>`

The following object-like macros\ [#9899_note227]_ specify the minimum and maximum limits of integer types corresponding to types defined in other standard headers.

.. _9899_7.18.3p2:

.. container:: snum

   :ref:`2 <9899_7.18.3p2>`

Each instance of these macros shall be replaced by a constant expression suitable for use in `#if` preprocessing directives, and this expression shall have the same type as would an expression that is an object of the corresponding type converted according to the integer promotions. Its implementation-defined value shall be equal to or greater in magnitude (absolute value) than the corresponding value given below, with the same sign. An implementation shall define only the macros corresponding to those typedef names it actually provides.\ [#9899_note228]_

-  limits of ptrdiff_t

::

    PTRDIFF_MIN                                            -65535
    PTRDIFF_MAX                                            +65535

-  limits of sig_atomic_t

::

    SIG_ATOMIC_MIN                                         see below
    SIG_ATOMIC_MAX                                         see below

-  limit of size_t

::

    SIZE_MAX                                               65535

-  limits of wchar_t

::

    WCHAR_MIN                                              see below
    WCHAR_MAX                                              see below

-  limits of wint_t

::

    WINT_MIN                                               see below
    WINT_MAX                                               see below

.. _9899_7.18.3p3:

.. container:: snum

   :ref:`3 <9899_7.18.3p3>`

If sig_atomic_t (see :ref:`7.14 <9899_7.14>`) is defined as a signed integer type, the value of SIG_ATOMIC_MIN shall be no greater than -127 and the value of SIG_ATOMIC_MAX shall be no less than 127; otherwise, sig_atomic_t is defined as an unsigned integer type, and the value of SIG_ATOMIC_MIN shall be 0 and the value of SIG_ATOMIC_MAX shall be no less than 255.

.. _9899_7.18.3p4:

.. container:: snum

   :ref:`4 <9899_7.18.3p4>`

If wchar_t (see :ref:`7.17 <9899_7.17>`) is defined as a signed integer type, the value of WCHAR_MIN shall be no greater than -127 and the value of WCHAR_MAX shall be no less than 127; otherwise, wchar_t is defined as an unsigned integer type, and the value of WCHAR_MIN shall be 0 and the value of WCHAR_MAX shall be no less than 255.\ [#9899_note229]_

.. _9899_7.18.3p5:

.. container:: snum

   :ref:`5 <9899_7.18.3p5>`

If wint_t (see :ref:`7.24 <9899_7.24>`) is defined as a signed integer type, the value of WINT_MIN shall be no greater than -32767 and the value of WINT_MAX shall be no less than 32767; otherwise, wint_t is defined as an unsigned integer type, and the value of WINT_MIN shall be 0 and the value of WINT_MAX shall be no less than 65535.







.. rubric:: Footnotes

.. [#9899_note227] C++ implementations should define these macros only when \__STDC_LIMIT_MACROS is defined before :ref:`\<stdint.h> <9899_7.18>` is included.
.. [#9899_note228] A freestanding implementation need not provide all of these types.
.. [#9899_note229] The values WCHAR_MIN and WCHAR_MAX do not necessarily correspond to members of the extended character set.
