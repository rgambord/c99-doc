.. _9899_7.13:

7.13 Nonlocal jumps \<setjmp.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. toctree::
   :maxdepth: 2

   1/index
   2/index


.. _9899_7.13p1:

:ref:`1 <9899_7.13p1>` The header :ref:`\<setjmp.h> <9899_7.13>` defines the macro setjmp, and declares one function and one type, for bypassing the normal function call and return discipline.\ [#9899_note216]_

.. _9899_7.13p2:

:ref:`2 <9899_7.13p2>` The type declared is

::

    jmp_buf

which is an array type suitable for holding the information needed to restore a calling environment. The environment of a call to the setjmp macro consists of information sufficient for a call to the longjmp function to return execution to the correct block and invocation of that block, were it called recursively. It does not include the state of the floating-point status flags, of open files, or of any other component of the abstract machine.

.. _9899_7.13p3:

:ref:`3 <9899_7.13p3>` It is unspecified whether setjmp is a macro or an identifier declared with external linkage. If a macro definition is suppressed in order to access an actual function, or a program defines an external identifier with the name setjmp, the behavior is undefined.





.. rubric:: Footnotes

.. [#9899_note216] These functions are useful for dealing with unusual conditions encountered in a low-level function of a program.
