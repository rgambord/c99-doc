.. _9899_7.12.14:

7.12.14 Comparison macros
^^^^^^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index
   4/index
   5/index
   6/index


.. _9899_7.12.14p1:

.. container:: snum

   :ref:`1 <9899_7.12.14p1>`

The relational and equality operators support the usual mathematical relationships between numeric values. For any ordered pair of numeric values exactly one of the relationships -- less, greater, and equal -- is true. Relational operators may raise the "invalid" floating-point exception when argument values are NaNs. For a NaN and a numeric value, or for two NaNs, just the unordered relationship is true.\ [#9899_note215]_ The following subclauses provide macros that are quiet (non floating-point exception raising) versions of the relational operators, and other comparison macros that facilitate writing efficient code that accounts for NaNs without suffering the "invalid" floating-point exception. In the synopses in this subclause, real-floating indicates that the argument shall be an expression of real floating type.





.. rubric:: Footnotes

.. [#9899_note215] IEC 60559 requires that the built-in relational operators raise the "invalid" floating-point exception if the operands compare unordered, as an error indicator for programs written without consideration of NaNs; the result in these cases is false.
