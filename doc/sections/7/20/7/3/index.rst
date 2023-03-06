.. _9899_7.20.7.3:

7.20.7.3 The wctomb function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.7.3p1:

.. container:: snum

   :ref:`1 <9899_7.20.7.3p1>`



::

    #include <stdlib.h>
    int wctomb(char *s, wchar_t wc);

.. rubric:: Description

.. _9899_7.20.7.3p2:

.. container:: snum

   :ref:`2 <9899_7.20.7.3p2>`

The wctomb function determines the number of bytes needed to represent the multibyte character corresponding to the wide character given by wc (including any shift sequences), and stores the multibyte character representation in the array whose first element is pointed to by s (if s is not a null pointer). At most MB_CUR_MAX characters are stored. If wc is a null wide character, a null byte is stored, preceded by any shift sequence needed to restore the initial shift state, and the function is left in the initial conversion state.

.. _9899_7.20.7.3p3:

.. container:: snum

   :ref:`3 <9899_7.20.7.3p3>`

The implementation shall behave as if no library function calls the wctomb function.

.. rubric:: Returns

.. _9899_7.20.7.3p4:

.. container:: snum

   :ref:`4 <9899_7.20.7.3p4>`

If s is a null pointer, the wctomb function returns a nonzero or zero value, if multibyte character encodings, respectively, do or do not have state-dependent encodings. If s is not a null pointer, the wctomb function returns -1 if the value of wc does not correspond to a valid multibyte character, or returns the number of bytes that are contained in the multibyte character corresponding to the value of wc.

.. _9899_7.20.7.3p5:

.. container:: snum

   :ref:`5 <9899_7.20.7.3p5>`

In no case will the value returned be greater than the value of the MB_CUR_MAX macro.

