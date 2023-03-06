.. _9899_7.19.5.3:

7.19.5.3 The fopen function
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.5.3p1:

.. container:: snum

   :ref:`1 <9899_7.19.5.3p1>`



::

    #include <stdio.h>
    FILE *fopen(const char * restrict filename,
         const char * restrict mode);

.. rubric:: Description

.. _9899_7.19.5.3p2:

.. container:: snum

   :ref:`2 <9899_7.19.5.3p2>`

The fopen function opens the file whose name is the string pointed to by filename, and associates a stream with it.

.. _9899_7.19.5.3p3:

.. container:: snum

   :ref:`3 <9899_7.19.5.3p3>`

The argument mode points to a string. If the string is one of the following, the file is open in the indicated mode. Otherwise, the behavior is undefined.\ [#9899_note237]_

r
   open text file for reading
w
   truncate to zero length or create text file for writing
a
   append; open or create text file for writing at end-of-file
rb
   open binary file for reading
wb
   truncate to zero length or create binary file for writing
ab
   append; open or create binary file for writing at end-of-file
r+
   open text file for update (reading and writing)
w+
   truncate to zero length or create text file for update
a+
   append; open or create text file for update, writing at end-of-file
r+b or rb+
   open binary file for update (reading and writing)
w+b or wb+
   truncate to zero length or create binary file for update
a+b or ab+
   append; open or create binary file for update, writing at end-of-file

.. _9899_7.19.5.3p4:

.. container:: snum

   :ref:`4 <9899_7.19.5.3p4>`

Opening a file with read mode ('r' as the first character in the mode argument) fails if the file does not exist or cannot be read.

.. _9899_7.19.5.3p5:

.. container:: snum

   :ref:`5 <9899_7.19.5.3p5>`

Opening a file with append mode ('a' as the first character in the mode argument) causes all subsequent writes to the file to be forced to the then current end-of-file, regardless of intervening calls to the fseek function. In some implementations, opening a binary file with append mode ('b' as the second or third character in the above list of mode argument values) may initially position the file position indicator for the stream beyond the last data written, because of null character padding.

.. _9899_7.19.5.3p6:

.. container:: snum

   :ref:`6 <9899_7.19.5.3p6>`

When a file is opened with update mode ('+' as the second or third character in the above list of mode argument values), both input and output may be performed on the associated stream. However, output shall not be directly followed by input without an intervening call to the fflush function or to a file positioning function (fseek, fsetpos, or rewind), and input shall not be directly followed by output without an intervening call to a file positioning function, unless the input operation encounters end- of-file. Opening (or creating) a text file with update mode may instead open (or create) a binary stream in some implementations.

.. _9899_7.19.5.3p7:

.. container:: snum

   :ref:`7 <9899_7.19.5.3p7>`

When opened, a stream is fully buffered if and only if it can be determined not to refer to an interactive device. The error and end-of-file indicators for the stream are cleared.

.. rubric:: Returns

.. _9899_7.19.5.3p8:

.. container:: snum

   :ref:`8 <9899_7.19.5.3p8>`

The fopen function returns a pointer to the object controlling the stream. If the open operation fails, fopen returns a null pointer.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_7.19.9`





.. rubric:: Footnotes

.. [#9899_note237] If the string begins with one of the above sequences, the implementation might choose to ignore the remaining characters, or it might use them to select different kinds of a file (some of which might not conform to the properties in :ref:`7.19.2 <9899_7.19.2>`).
