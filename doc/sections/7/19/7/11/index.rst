.. _9899_7.19.7.11:

7.19.7.11 The ungetc function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.7.11p1:

.. container:: snum

   :ref:`1 <9899_7.19.7.11p1>`



::

    #include <stdio.h>
    int ungetc(int c, FILE *stream);

.. rubric:: Description

.. _9899_7.19.7.11p2:

.. container:: snum

   :ref:`2 <9899_7.19.7.11p2>`

The ungetc function pushes the character specified by c (converted to an unsigned char) back onto the input stream pointed to by stream. Pushed-back characters will be returned by subsequent reads on that stream in the reverse order of their pushing. A successful intervening call (with the stream pointed to by stream) to a file positioning function (fseek, fsetpos, or rewind) discards any pushed-back characters for the stream. The external storage corresponding to the stream is unchanged.

.. _9899_7.19.7.11p3:

.. container:: snum

   :ref:`3 <9899_7.19.7.11p3>`

One character of pushback is guaranteed. If the ungetc function is called too many times on the same stream without an intervening read or file positioning operation on that stream, the operation may fail.

.. _9899_7.19.7.11p4:

.. container:: snum

   :ref:`4 <9899_7.19.7.11p4>`

If the value of c equals that of the macro EOF, the operation fails and the input stream is unchanged.

.. _9899_7.19.7.11p5:

.. container:: snum

   :ref:`5 <9899_7.19.7.11p5>`

A successful call to the ungetc function clears the end-of-file indicator for the stream. The value of the file position indicator for the stream after reading or discarding all pushed-back characters shall be the same as it was before the characters were pushed back. For a text stream, the value of its file position indicator after a successful call to the ungetc function is unspecified until all pushed-back characters are read or discarded. For a binary stream, its file position indicator is decremented by each successful call to the ungetc function; if its value was zero before a call, it is indeterminate after the call.\ [#9899_note256]_

.. rubric:: Returns

.. _9899_7.19.7.11p6:

.. container:: snum

   :ref:`6 <9899_7.19.7.11p6>`

The ungetc function returns the character pushed back after conversion, or EOF if the operation fails.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_7.19.9`





.. rubric:: Footnotes

.. [#9899_note256] See "future library directions" (:ref:`7.26.9 <9899_7.26.9>`).
