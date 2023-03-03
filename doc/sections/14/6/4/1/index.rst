.. _9899_G.6.4.1:

G.6.4.1 The cpow functions
''''''''''''''''''''''''''

.. _9899_G.6.4.1p1:

:ref:`1 <9899_G.6.4.1p1>` The cpow functions raise floating-point exceptions if appropriate for the calculation of the parts of the result, and may raise spurious exceptions.\ [#9899_note327]_





.. rubric:: Footnotes

.. [#9899_note327] This allows cpow( z , c ) to be implemented as cexp(c clog( z )) without precluding implementations that treat special cases more carefully.
