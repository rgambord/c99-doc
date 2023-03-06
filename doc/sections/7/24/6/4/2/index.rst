.. _9899_7.24.6.4.2:

7.24.6.4.2 The wcsrtombs function
"""""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.6.4.2p1:

.. container:: snum

   :ref:`1 <9899_7.24.6.4.2p1>`



::

    #include <wchar.h>
    size_t wcsrtombs(char * restrict dst,
         const wchar_t ** restrict src,
         size_t len,
         mbstate_t * restrict ps);

.. rubric:: Description

.. _9899_7.24.6.4.2p2:

.. container:: snum

   :ref:`2 <9899_7.24.6.4.2p2>`

The wcsrtombs function converts a sequence of wide characters from the array indirectly pointed to by src into a sequence of corresponding multibyte characters that begins in the conversion state described by the object pointed to by ps. If dst is not a null pointer, the converted characters are then stored into the array pointed to by dst. Conversion continues up to and including a terminating null wide character, which is also stored. Conversion stops earlier in two cases: when a wide character is reached that does not correspond to a valid multibyte character, or (if dst is not a null pointer) when the next multibyte character would exceed the limit of len total bytes to be stored into the array pointed to by dst. Each conversion takes place as if by a call to the wcrtomb function.\ [#9899_note302]_

.. _9899_7.24.6.4.2p3:

.. container:: snum

   :ref:`3 <9899_7.24.6.4.2p3>`

If dst is not a null pointer, the pointer object pointed to by src is assigned either a null pointer (if conversion stopped due to reaching a terminating null wide character) or the address just past the last wide character converted (if any). If conversion stopped due to reaching a terminating null wide character, the resulting state described is the initial conversion state.

.. rubric:: Returns

.. _9899_7.24.6.4.2p4:

.. container:: snum

   :ref:`4 <9899_7.24.6.4.2p4>`

If conversion stops because a wide character is reached that does not correspond to a valid multibyte character, an encoding error occurs: the wcsrtombs function stores the value of the macro EILSEQ in errno and returns (size_t)(-1); the conversion state is unspecified. Otherwise, it returns the number of bytes in the resulting multibyte character sequence, not including the terminating null character (if any).





.. rubric:: Footnotes

.. [#9899_note302] If conversion stops because a terminating null wide character has been reached, the bytes stored include those necessary to reach the initial shift state immediately before the null byte.
