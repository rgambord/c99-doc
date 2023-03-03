.. _9899_F.8.2:

F.8.2 Expression transformations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_F.8.2p1:

:ref:`1 <9899_F.8.2p1>`

.. code-block:: text

    x / 2 <-> x * 0.5    

Although similar transformations involving inexact constants generally do not yield numerically equivalent expressions, if the constants are exact then such transformations can be made on IEC 60559 machines and others that round perfectly.

.. code-block:: text

    1 * x and x / 1 -> x    

The expressions 1 \* x, x / 1, and x are equivalent (on IEC 60559 machines, among others).\ [#9899_note317]_

.. code-block:: text

    x / x -> 1.0            

The expressions x / x and 1.0 are not equivalent if x can be zero, infinite, or NaN.

.. code-block:: text

    x - y <-> x + (-y)   

The expressions x - y, x + (-y), and (-y) + x are equivalent (on IEC 60559 machines, among others).

.. code-block:: text

    x - y <-> -(y - x)   

The expressions x - y and -(y - x) are not equivalent because 1 - 1 is +0 but -(1 - 1) is -0 (in the default rounding direction).\ [#9899_note318]_

.. code-block:: text

    x - x -> 0.0            

The expressions x - x and 0.0 are not equivalent if x is a NaN or infinite.

.. code-block:: text

    0 * x -> 0.0            

The expressions 0 \* x and 0.0 are not equivalent if x is a NaN, infinite, or -0.

.. code-block:: text

    x + 0 -> x              

The expressions x + 0 and x are not equivalent if x is -0, because (-0) + (+0) yields +0 (in the default rounding direction), not -0.

.. code-block:: text

    x - 0 -> x              

(+0) - (+0) yields -0 when rounding is downward (toward -(inf)), but +0 otherwise, and (-0) - (+0) always yields -0; so, if the state of the FENV_ACCESS pragma is ''off'', promising default rounding, then the implementation can replace x - 0 by x, even if x might be zero.

.. code-block:: text

    -x <-> 0 - x         

The expressions -x and 0 - x are not equivalent if x is +0, because -(+0) yields -0, but 0 - (+0) yields +0 (unless rounding is downward).




.. code-block:: text

    1/(1/ (+-) (inf)) is (+-) (inf)

and

.. code-block:: text

    conj(csqrt(z)) is csqrt(conj(z)),

for complex z.



.. rubric:: Footnotes

.. [#9899_note317] Strict support for signaling NaNs -- not required by this specification -- would invalidate these and other transformations that remove arithmetic operators.
.. [#9899_note318] IEC 60559 prescribes a signed zero to preserve mathematical identities across certain discontinuities. Examples include:
