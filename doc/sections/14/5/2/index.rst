.. _9899_G.5.2:

G.5.2 Additive operators
^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Semantics

.. _9899_G.5.2p1:

.. container:: snum

   :ref:`1 <9899_G.5.2p1>`

If both operands have imaginary type, then the result has imaginary type. (If one operand has real type and the other operand has imaginary type, or if either operand has complex type, then the result has complex type.)

.. _9899_G.5.2p2:

.. container:: snum

   :ref:`2 <9899_G.5.2p2>`

In all cases the result and floating-point exception behavior of a + or - operator is defined by the usual mathematical formula:

.. code-block:: text

    + or -              u                       iv                    u + iv

.. code-block:: text

    x                 x(+-)u                     x (+-) iv              (x (+-) u) (+-) iv

.. code-block:: text

    iy               (+-)u + iy                 i(y (+-) v)             (+-)u + i(y (+-) v)

.. code-block:: text

    x + iy         (x (+-) u) + iy            x + i(y (+-) v)        (x (+-) u) + i(y (+-) v)

