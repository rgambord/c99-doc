.. _9899_7.6.2:

7.6.2 Floating-point exceptions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index
   4/index
   5/index


.. _9899_7.6.2p1:

.. container:: snum

   :ref:`1 <9899_7.6.2p1>`

The following functions provide access to the floating-point status flags.\ [#9899_note186]_ The int input argument for the functions represents a subset of floating-point exceptions, and can be zero or the bitwise OR of one or more floating-point exception macros, for example FE_OVERFLOW \| FE_INEXACT. For other argument values the behavior of these functions is undefined.





.. rubric:: Footnotes

.. [#9899_note186] The functions fetestexcept, feraiseexcept, and feclearexcept support the basic abstraction of flags that are either set or clear. An implementation may endow floating-point status flags with more information -- for example, the address of the code which first raised the floating- point exception; the functions fegetexceptflag and fesetexceptflag deal with the full content of flags.
