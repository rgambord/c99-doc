.. _9899_7.3.4:

7.3.4 The CX_LIMITED_RANGE pragma
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Synopsis

.. _9899_7.3.4p1:

:ref:`1 <9899_7.3.4p1>`

::

    #include <complex.h>
    #pragma STDC CX_LIMITED_RANGE on-off-switch

.. rubric:: Description

.. _9899_7.3.4p2:

:ref:`2 <9899_7.3.4p2>` The usual mathematical formulas for complex multiply, divide, and absolute value are problematic because of their treatment of infinities and because of undue overflow and underflow. The CX_LIMITED_RANGE pragma can be used to inform the implementation that (where the state is ''on'') the usual mathematical formulas are acceptable.\ [#9899_note169]_ The pragma can occur either outside external declarations or preceding all explicit declarations and statements inside a compound statement. When outside external declarations, the pragma takes effect from its occurrence until another CX_LIMITED_RANGE pragma is encountered, or until the end of the translation unit. When inside a compound statement, the pragma takes effect from its occurrence until another CX_LIMITED_RANGE pragma is encountered (including within a nested compound statement), or until the end of the compound statement; at the end of a compound statement the state for the pragma is restored to its condition just before the compound statement. If this pragma is used in any other context, the behavior is undefined. The default state for the pragma is ''off''.



::

    (x + iy) x (u + iv) = (xu - yv) + i(yu + xv)
    (x + iy) / (u + iv) = [(xu + yv) + i(yu - xv)]/(u2 + v2)
    | x + iy | = (sqrt)(x2 + y2)

where the programmer can determine they are safe.



.. rubric:: Footnotes

.. [#9899_note169] The purpose of the pragma is to allow the implementation to use the formulas:
