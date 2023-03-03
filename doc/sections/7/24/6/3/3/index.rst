.. _9899_7.24.6.3.3:

7.24.6.3.3 The wcrtomb function
"""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.6.3.3p1:

:ref:`1 <9899_7.24.6.3.3p1>`

::

    #include <wchar.h>
    size_t wcrtomb(char * restrict s,
         wchar_t wc,
         mbstate_t * restrict ps);

.. rubric:: Description

.. _9899_7.24.6.3.3p2:

:ref:`2 <9899_7.24.6.3.3p2>` If s is a null pointer, the wcrtomb function is equivalent to the call

::

    wcrtomb(buf, L'\0', ps)

where buf is an internal buffer.

.. _9899_7.24.6.3.3p3:

:ref:`3 <9899_7.24.6.3.3p3>` If s is not a null pointer, the wcrtomb function determines the number of bytes needed to represent the multibyte character that corresponds to the wide character given by wc (including any shift sequences), and stores the multibyte character representation in the array whose first element is pointed to by s. At most MB_CUR_MAX bytes are stored. If wc is a null wide character, a null byte is stored, preceded by any shift sequence needed to restore the initial shift state; the resulting state described is the initial conversion state.

.. rubric:: Returns

.. _9899_7.24.6.3.3p4:

:ref:`4 <9899_7.24.6.3.3p4>` The wcrtomb function returns the number of bytes stored in the array object (including any shift sequences). When wc is not a valid wide character, an encoding error occurs: the function stores the value of the macro EILSEQ in errno and returns (size_t)(-1); the conversion state is unspecified.

