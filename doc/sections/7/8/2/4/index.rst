.. _9899_7.8.2.4:

7.8.2.4 The wcstoimax and wcstoumax functions
'''''''''''''''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.8.2.4p1:

.. container:: snum

   :ref:`1 <9899_7.8.2.4p1>`



::

    #include <stddef.h>           // for wchar_t
    #include <inttypes.h>
    intmax_t wcstoimax(const wchar_t * restrict nptr,
         wchar_t ** restrict endptr, int base);
    uintmax_t wcstoumax(const wchar_t * restrict nptr,
         wchar_t ** restrict endptr, int base);

.. rubric:: Description

.. _9899_7.8.2.4p2:

.. container:: snum

   :ref:`2 <9899_7.8.2.4p2>`

The wcstoimax and wcstoumax functions are equivalent to the wcstol, wcstoll, wcstoul, and wcstoull functions except that the initial portion of the wide string is converted to intmax_t and uintmax_t representation, respectively.

.. rubric:: Returns

.. _9899_7.8.2.4p3:

.. container:: snum

   :ref:`3 <9899_7.8.2.4p3>`

The wcstoimax function returns the converted value, if any. If no conversion could be performed, zero is returned. If the correct value is outside the range of representable values, INTMAX_MAX, INTMAX_MIN, or UINTMAX_MAX is returned (according to the return type and sign of the value, if any), and the value of the macro ERANGE is stored in errno.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_7.24.4.1.2`

