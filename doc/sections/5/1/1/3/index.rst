.. _9899_5.1.1.3:

5.1.1.3 Diagnostics
'''''''''''''''''''

.. _9899_5.1.1.3p1:

.. container:: snum

   :ref:`1 <9899_5.1.1.3p1>`

A conforming implementation shall produce at least one diagnostic message (identified in an implementation-defined manner) if a preprocessing translation unit or translation unit contains a violation of any syntax rule or constraint, even if the behavior is also explicitly specified as undefined or implementation-defined. Diagnostic messages need not be produced in other circumstances.\ [#9899_note8]_

.. _9899_5.1.1.3p2:

.. container:: snum

   :ref:`2 <9899_5.1.1.3p2>`

EXAMPLE An implementation shall issue a diagnostic for the translation unit:

::

    char i;
    int i;

because in those cases where wording in this International Standard describes the behavior for a construct as being both a constraint error and resulting in undefined behavior, the constraint error shall be diagnosed.





.. rubric:: Footnotes

.. [#9899_note8] The intent is that an implementation should identify the nature of, and where possible localize, each violation. Of course, an implementation is free to produce any number of diagnostics as long as a valid program is still correctly translated. It may also successfully translate an invalid program.
