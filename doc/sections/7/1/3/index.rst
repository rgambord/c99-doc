.. _9899_7.1.3:

7.1.3 Reserved identifiers
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_7.1.3p1:

.. container:: snum

   :ref:`1 <9899_7.1.3p1>`

Each header declares or defines all identifiers listed in its associated subclause, and optionally declares or defines identifiers listed in its associated future library directions subclause and identifiers which are always reserved either for any use or for use as file scope identifiers.

-  All identifiers that begin with an underscore and either an uppercase letter or another underscore are always reserved for any use.
-  All identifiers that begin with an underscore are always reserved for use as identifiers with file scope in both the ordinary and tag name spaces.
-  Each macro name in any of the following subclauses (including the future library directions) is reserved for use as specified if any of its associated headers is included; unless explicitly stated otherwise (see :ref:`7.1.4 <9899_7.1.4>`).
-  All identifiers with external linkage in any of the following subclauses (including the future library directions) are always reserved for use as identifiers with external linkage.\ [#9899_note160]_
-  Each identifier with file scope listed in any of the following subclauses (including the future library directions) is reserved for use as a macro name and as an identifier with file scope in the same name space if any of its associated headers is included.

.. _9899_7.1.3p2:

.. container:: snum

   :ref:`2 <9899_7.1.3p2>`

No other identifiers are reserved. If the program declares or defines an identifier in a context in which it is reserved (other than as allowed by :ref:`7.1.4 <9899_7.1.4>`), or defines a reserved identifier as a macro name, the behavior is undefined.

.. _9899_7.1.3p3:

.. container:: snum

   :ref:`3 <9899_7.1.3p3>`

If the program removes (with `#undef`) any macro definition of an identifier in the first group listed above, the behavior is undefined.





.. rubric:: Footnotes

.. [#9899_note160] The list of reserved identifiers with external linkage includes errno, math_errhandling, setjmp, and va_end.
