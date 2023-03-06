.. _9899_7.3.3:

7.3.3 Branch cuts
^^^^^^^^^^^^^^^^^

.. _9899_7.3.3p1:

.. container:: snum

   :ref:`1 <9899_7.3.3p1>`

Some of the functions below have branch cuts, across which the function is discontinuous. For implementations with a signed zero (including all IEC 60559 implementations) that follow the specifications of :ref:`annex G <9899_G>`, the sign of zero distinguishes one side of a cut from another so the function is continuous (except for format limitations) as the cut is approached from either side. For example, for the square root function, which has a branch cut along the negative real axis, the top of the cut, with imaginary part +0, maps to the positive imaginary axis, and the bottom of the cut, with imaginary part -0, maps to the negative imaginary axis.

.. _9899_7.3.3p2:

.. container:: snum

   :ref:`2 <9899_7.3.3p2>`

Implementations that do not support a signed zero (see :ref:`annex F <9899_F>`) cannot distinguish the sides of branch cuts. These implementations shall map a cut so the function is continuous as the cut is approached coming around the finite endpoint of the cut in a counter clockwise direction. (Branch cuts for the functions specified here have just one finite endpoint.) For example, for the square root function, coming counter clockwise around the finite endpoint of the cut along the negative real axis approaches the cut from above, so the cut maps to the positive imaginary axis.

