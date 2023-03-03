.. _9899_7.16:

7.16 Boolean type and values \<stdbool.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _9899_7.16p1:

:ref:`1 <9899_7.16p1>` The header :ref:`\<stdbool.h> <9899_7.16>` defines four macros.

.. _9899_7.16p2:

:ref:`2 <9899_7.16p2>` The macro

::

    bool

expands to \_Bool.

.. _9899_7.16p3:

:ref:`3 <9899_7.16p3>` The remaining three macros are suitable for use in #if preprocessing directives. They are

::

    true

which expands to the integer constant 1,

::

    false

which expands to the integer constant 0, and

::

    __bool_true_false_are_defined

which expands to the integer constant 1.

.. _9899_7.16p4:

:ref:`4 <9899_7.16p4>` Notwithstanding the provisions of :ref:`7.1.3 <9899_7.1.3>`, a program may undefine and perhaps then redefine the macros bool, true, and false.\ [#9899_note222]_





.. rubric:: Footnotes

.. [#9899_note222] See ''future library directions'' (:ref:`7.26.7 <9899_7.26.7>`).
