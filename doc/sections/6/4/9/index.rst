.. _9899_6.4.9:

6.4.9 Comments
^^^^^^^^^^^^^^

.. _9899_6.4.9p1:

:ref:`1 <9899_6.4.9p1>` Except within a character constant, a string literal, or a comment, the characters /\* introduce a comment. The contents of such a comment are examined only to identify multibyte characters and to find the characters \*/ that terminate it.\ [#9899_note71]_

.. _9899_6.4.9p2:

:ref:`2 <9899_6.4.9p2>` Except within a character constant, a string literal, or a comment, the characters // introduce a comment that includes all multibyte characters up to, but not including, the next new-line character. The contents of such a comment are examined only to identify multibyte characters and to find the terminating new-line character.

.. _9899_6.4.9p3:

:ref:`3 <9899_6.4.9p3>` EXAMPLE

::

    "a//b"                              //   four-character string literal
    #include "//e"                      //   undefined behavior
    // */                               //   comment, not syntax error
    f = g/**//h;                        //   equivalent to f = g / h;
    //\
    i();                                // part of a two-line comment
    /\
    / j();                              // part of a two-line comment
    #define glue(x,y) x##y
    glue(/,/) k();                      // syntax error, not comment
    /*//*/ l();                         // equivalent to l();
    m = n//**/o
       + p;                             // equivalent to m = n + p;





.. rubric:: Footnotes

.. [#9899_note71] Thus, /\* \.\.\. \*/ comments do not nest.
