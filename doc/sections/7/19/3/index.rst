.. _9899_7.19.3:

7.19.3 Files
^^^^^^^^^^^^

.. _9899_7.19.3p1:

.. container:: snum

   :ref:`1 <9899_7.19.3p1>`

A stream is associated with an external file (which may be a physical device) by opening a file, which may involve creating a new file. Creating an existing file causes its former contents to be discarded, if necessary. If a file can support positioning requests (such as a disk file, as opposed to a terminal), then a file position indicator associated with the stream is positioned at the start (character number zero) of the file, unless the file is opened with append mode in which case it is implementation-defined whether the file position indicator is initially positioned at the beginning or the end of the file. The file position indicator is maintained by subsequent reads, writes, and positioning requests, to facilitate an orderly progression through the file.

.. _9899_7.19.3p2:

.. container:: snum

   :ref:`2 <9899_7.19.3p2>`

Binary files are not truncated, except as defined in :ref:`7.19.5.3 <9899_7.19.5.3>`. Whether a write on a text stream causes the associated file to be truncated beyond that point is implementation- defined.

.. _9899_7.19.3p3:

.. container:: snum

   :ref:`3 <9899_7.19.3p3>`

When a stream is unbuffered, characters are intended to appear from the source or at the destination as soon as possible. Otherwise characters may be accumulated and transmitted to or from the host environment as a block. When a stream is fully buffered, characters are intended to be transmitted to or from the host environment as a block when a buffer is filled. When a stream is line buffered, characters are intended to be transmitted to or from the host environment as a block when a new-line character is encountered. Furthermore, characters are intended to be transmitted as a block to the host environment when a buffer is filled, when input is requested on an unbuffered stream, or when input is requested on a line buffered stream that requires the transmission of characters from the host environment. Support for these characteristics is implementation-defined, and may be affected via the setbuf and setvbuf functions.

.. _9899_7.19.3p4:

.. container:: snum

   :ref:`4 <9899_7.19.3p4>`

A file may be disassociated from a controlling stream by closing the file. Output streams are flushed (any unwritten buffer contents are transmitted to the host environment) before the stream is disassociated from the file. The value of a pointer to a FILE object is indeterminate after the associated file is closed (including the standard text streams). Whether a file of zero length (on which no characters have been written by an output stream) actually exists is implementation-defined.

.. _9899_7.19.3p5:

.. container:: snum

   :ref:`5 <9899_7.19.3p5>`

The file may be subsequently reopened, by the same or another program execution, and its contents reclaimed or modified (if it can be repositioned at its start). If the main function returns to its original caller, or if the exit function is called, all open files are closed (hence all output streams are flushed) before program termination. Other paths to program termination, such as calling the abort function, need not close all files properly.

.. _9899_7.19.3p6:

.. container:: snum

   :ref:`6 <9899_7.19.3p6>`

The address of the FILE object used to control a stream may be significant; a copy of a FILE object need not serve in place of the original.

.. _9899_7.19.3p7:

.. container:: snum

   :ref:`7 <9899_7.19.3p7>`

At program startup, three text streams are predefined and need not be opened explicitly -- standard input (for reading conventional input), standard output (for writing conventional output), and standard error (for writing diagnostic output). As initially opened, the standard error stream is not fully buffered; the standard input and standard output streams are fully buffered if and only if the stream can be determined not to refer to an interactive device.

.. _9899_7.19.3p8:

.. container:: snum

   :ref:`8 <9899_7.19.3p8>`

Functions that open additional (nontemporary) files require a file name, which is a string. The rules for composing valid file names are implementation-defined. Whether the same file can be simultaneously open multiple times is also implementation-defined.

.. _9899_7.19.3p9:

.. container:: snum

   :ref:`9 <9899_7.19.3p9>`

Although both text and binary wide-oriented streams are conceptually sequences of wide characters, the external file associated with a wide-oriented stream is a sequence of multibyte characters, generalized as follows:

-  Multibyte encodings within files may contain embedded null bytes (unlike multibyte encodings valid for use internal to the program).
-  A file need not begin nor end in the initial shift state.\ [#9899_note234]_

.. _9899_7.19.3p10:

.. container:: snum

   :ref:`10 <9899_7.19.3p10>`

Moreover, the encodings used for multibyte characters may differ among files. Both the nature and choice of such encodings are implementation-defined.

.. _9899_7.19.3p11:

.. container:: snum

   :ref:`11 <9899_7.19.3p11>`

The wide character input functions read multibyte characters from the stream and convert them to wide characters as if they were read by successive calls to the fgetwc function. Each conversion occurs as if by a call to the mbrtowc function, with the conversion state described by the stream's own mbstate_t object. The byte input functions read characters from the stream as if by successive calls to the fgetc function.

.. _9899_7.19.3p12:

.. container:: snum

   :ref:`12 <9899_7.19.3p12>`

The wide character output functions convert wide characters to multibyte characters and write them to the stream as if they were written by successive calls to the fputwc function. Each conversion occurs as if by a call to the wcrtomb function, with the conversion state described by the stream's own mbstate_t object. The byte output functions write characters to the stream as if by successive calls to the fputc function.

.. _9899_7.19.3p13:

.. container:: snum

   :ref:`13 <9899_7.19.3p13>`

In some cases, some of the byte input/output functions also perform conversions between multibyte characters and wide characters. These conversions also occur as if by calls to the mbrtowc and wcrtomb functions.

.. _9899_7.19.3p14:

.. container:: snum

   :ref:`14 <9899_7.19.3p14>`

An encoding error occurs if the character sequence presented to the underlying mbrtowc function does not form a valid (generalized) multibyte character, or if the code value passed to the underlying wcrtomb does not correspond to a valid (generalized) multibyte character. The wide character input/output functions and the byte input/output functions store the value of the macro EILSEQ in errno if and only if an encoding error occurs.

.. rubric:: Environmental limits

.. _9899_7.19.3p15:

.. container:: snum

   :ref:`15 <9899_7.19.3p15>`

The value of FOPEN_MAX shall be at least eight, including the three standard text streams.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_7.20.4.3`
   - :ref:`9899_7.19.7.1`
   - :ref:`9899_7.19.5.3`
   - :ref:`9899_7.19.7.3`
   - :ref:`9899_7.19.5.5`
   - :ref:`9899_7.19.5.6`
   - :ref:`9899_7.24.3.1`
   - :ref:`9899_7.24.3.3`
   - :ref:`9899_7.24.6`
   - :ref:`9899_7.24.6.3.2`
   - :ref:`9899_7.24.6.3.3`





.. rubric:: Footnotes

.. [#9899_note234] Setting the file position indicator to end-of-file, as with fseek(file, 0, SEEK_END), has undefined behavior for a binary stream (because of possible trailing null characters) or for any stream with state-dependent encoding that does not assuredly end in the initial shift state.
