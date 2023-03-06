.. _9899_7.24.6.4.1:

7.24.6.4.1 The mbsrtowcs function
"""""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.6.4.1p1:

.. container:: snum

   :ref:`1 <9899_7.24.6.4.1p1>`



::

    #include <wchar.h>
    size_t mbsrtowcs(wchar_t * restrict dst,
         const char ** restrict src,
         size_t len,
         mbstate_t * restrict ps);

.. rubric:: Description

.. _9899_7.24.6.4.1p2:

.. container:: snum

   :ref:`2 <9899_7.24.6.4.1p2>`

The mbsrtowcs function converts a sequence of multibyte characters that begins in the conversion state described by the object pointed to by ps, from the array indirectly pointed to by src into a sequence of corresponding wide characters. If dst is not a null pointer, the converted characters are stored into the array pointed to by dst. Conversion continues up to and including a terminating null character, which is also stored. Conversion stops earlier in two cases: when a sequence of bytes is encountered that does not form a valid multibyte character, or (if dst is not a null pointer) when len wide characters have been stored into the array pointed to by dst.\ [#9899_note301]_ Each conversion takes place as if by a call to the mbrtowc function.

.. _9899_7.24.6.4.1p3:

.. container:: snum

   :ref:`3 <9899_7.24.6.4.1p3>`

If dst is not a null pointer, the pointer object pointed to by src is assigned either a null pointer (if conversion stopped due to reaching a terminating null character) or the address just past the last multibyte character converted (if any). If conversion stopped due to reaching a terminating null character and if dst is not a null pointer, the resulting state described is the initial conversion state.

.. rubric:: Returns

.. _9899_7.24.6.4.1p4:

.. container:: snum

   :ref:`4 <9899_7.24.6.4.1p4>`

If the input conversion encounters a sequence of bytes that do not form a valid multibyte character, an encoding error occurs: the mbsrtowcs function stores the value of the macro EILSEQ in errno and returns (size_t)(-1); the conversion state is unspecified. Otherwise, it returns the number of multibyte characters successfully converted, not including the terminating null character (if any).





.. rubric:: Footnotes

.. [#9899_note301] Thus, the value of len is ignored if dst is a null pointer.
