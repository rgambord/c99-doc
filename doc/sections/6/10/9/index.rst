.. _9899_6.10.9:

6.10.9 Pragma operator
^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Semantics

.. _9899_6.10.9p1:

:ref:`1 <9899_6.10.9p1>` A unary operator expression of the form:

.. code-block:: text

    _Pragma ( string-literal )

is processed as follows: The string literal is destringized by deleting the L prefix, if present, deleting the leading and trailing double-quotes, replacing each escape sequence \\" by a double-quote, and replacing each escape sequence \\\\ by a single backslash. The resulting sequence of characters is processed through translation phase 3 to produce preprocessing tokens that are executed as if they were the pp-tokens in a pragma directive. The original four preprocessing tokens in the unary operator expression are removed.

.. _9899_6.10.9p2:

:ref:`2 <9899_6.10.9p2>` EXAMPLE A directive of the form:

::

    #pragma listing on "..\listing.dir"

can also be expressed as:

::

    _Pragma ( "listing on \"..\\listing.dir\"" )

The latter form is processed in the same way whether it appears literally as shown, or results from macro replacement, as in:

.. code-block:: text

    #define LISTING(x) PRAGMA(listing on #x)
    #define PRAGMA(x) _Pragma(#x)
    LISTING ( ..\listing.dir )

