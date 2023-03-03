.. _9899_6.10.2:

6.10.2 Source file inclusion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Constraints

.. _9899_6.10.2p1:

:ref:`1 <9899_6.10.2p1>` A #include directive shall identify a header or source file that can be processed by the implementation.

.. rubric:: Semantics

.. _9899_6.10.2p2:

:ref:`2 <9899_6.10.2p2>` A preprocessing directive of the form

.. code-block:: text

    # include <h-char-sequence> new-line

searches a sequence of implementation-defined places for a header identified uniquely by the specified sequence between the < and > delimiters, and causes the replacement of that directive by the entire contents of the header. How the places are specified or the header identified is implementation-defined.

.. _9899_6.10.2p3:

:ref:`3 <9899_6.10.2p3>` A preprocessing directive of the form

.. code-block:: text

    # include "q-char-sequence" new-line

causes the replacement of that directive by the entire contents of the source file identified by the specified sequence between the " delimiters. The named source file is searched for in an implementation-defined manner. If this search is not supported, or if the search fails, the directive is reprocessed as if it read

.. code-block:: text

    # include <h-char-sequence> new-line

with the identical contained sequence (including > characters, if any) from the original directive.

.. _9899_6.10.2p4:

:ref:`4 <9899_6.10.2p4>` A preprocessing directive of the form

.. code-block:: text

    # include pp-tokens new-line

(that does not match one of the two previous forms) is permitted. The preprocessing tokens after include in the directive are processed just as in normal text. (Each identifier currently defined as a macro name is replaced by its replacement list of preprocessing tokens.) The directive resulting after all replacements shall match one of the two previous forms.\ [#9899_note148]_ The method by which a sequence of preprocessing tokens between a < and a > preprocessing token pair or a pair of " characters is combined into a single header name preprocessing token is implementation-defined.

.. _9899_6.10.2p5:

:ref:`5 <9899_6.10.2p5>` The implementation shall provide unique mappings for sequences consisting of one or more nondigits or digits (:ref:`6.4.2.1 <9899_6.4.2.1>`) followed by a period (.) and a single nondigit. The first character shall not be a digit. The implementation may ignore distinctions of alphabetical case and restrict the mapping to eight significant characters before the period.

.. _9899_6.10.2p6:

:ref:`6 <9899_6.10.2p6>` A #include preprocessing directive may appear in a source file that has been read because of a #include directive in another file, up to an implementation-defined nesting limit (see :ref:`5.2.4.1 <9899_5.2.4.1>`).

.. _9899_6.10.2p7:

:ref:`7 <9899_6.10.2p7>` EXAMPLE 1 The most common uses of #include preprocessing directives are as in the following:

::

    #include <stdio.h>
    #include "myprog.h"

.. _9899_6.10.2p8:

:ref:`8 <9899_6.10.2p8>` EXAMPLE 2 This illustrates macro-replaced #include directives:

::

    #if VERSION == 1
          #define INCFILE        "vers1.h"
    #elif VERSION == 2
          #define INCFILE        "vers2.h"      // and so on
    #else
          #define INCFILE        "versN.h"
    #endif
    #include INCFILE

**Forward references**: macro replacement (:ref:`6.10.3 <9899_6.10.3>`).





.. rubric:: Footnotes

.. [#9899_note148] Note that adjacent string literals are not concatenated into a single string literal (see the translation phases in :ref:`5.1.1.2 <9899_5.1.1.2>`); thus, an expansion that results in two string literals is an invalid directive.
