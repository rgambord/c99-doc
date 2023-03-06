.. _9899_7.20.7.1:

7.20.7.1 The mblen function
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.7.1p1:

.. container:: snum

   :ref:`1 <9899_7.20.7.1p1>`



::

    #include <stdlib.h>
    int mblen(const char *s, size_t n);

.. rubric:: Description

.. _9899_7.20.7.1p2:

.. container:: snum

   :ref:`2 <9899_7.20.7.1p2>`

If s is not a null pointer, the mblen function determines the number of bytes contained in the multibyte character pointed to by s. Except that the conversion state of the mbtowc function is not affected, it is equivalent to

::

    mbtowc((wchar_t *)0, s, n);

.. _9899_7.20.7.1p3:

.. container:: snum

   :ref:`3 <9899_7.20.7.1p3>`

The implementation shall behave as if no library function calls the mblen function.

.. rubric:: Returns

.. _9899_7.20.7.1p4:

.. container:: snum

   :ref:`4 <9899_7.20.7.1p4>`

If s is a null pointer, the mblen function returns a nonzero or zero value, if multibyte character encodings, respectively, do or do not have state-dependent encodings. If s is not a null pointer, the mblen function either returns 0 (if s points to the null character), or returns the number of bytes that are contained in the multibyte character (if the next n or fewer bytes form a valid multibyte character), or returns -1 (if they do not form a valid multibyte character).

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_7.20.7.2`

