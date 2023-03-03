.. _9899_F.9.9.2:

F.9.9.2 The fmax functions
''''''''''''''''''''''''''

.. _9899_F.9.9.2p1:

:ref:`1 <9899_F.9.9.2p1>` If just one argument is a NaN, the fmax functions return the other argument (if both arguments are NaNs, the functions return a NaN).

.. _9899_F.9.9.2p2:

:ref:`2 <9899_F.9.9.2p2>` The body of the fmax function might be\ [#9899_note323]_

::

    { return (isgreaterequal(x, y) ||
         isnan(y)) ? x : y; }





.. rubric:: Footnotes

.. [#9899_note323] Ideally, fmax would be sensitive to the sign of zero, for example fmax(-0.0, +0.0) would return +0; however, implementation in software might be impractical.
