.. _9899_6.2.4:

6.2.4 Storage durations of objects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_6.2.4p1:

:ref:`1 <9899_6.2.4p1>` An object has a storage duration that determines its lifetime. There are three storage durations: static, automatic, and allocated. Allocated storage is described in :ref:`7.20.3 <9899_7.20.3>`.

.. _9899_6.2.4p2:

:ref:`2 <9899_6.2.4p2>` The lifetime of an object is the portion of program execution during which storage is guaranteed to be reserved for it. An object exists, has a constant address,\ [#9899_note25]_ and retains its last-stored value throughout its lifetime.\ [#9899_note26]_ If an object is referred to outside of its lifetime, the behavior is undefined. The value of a pointer becomes indeterminate when the object it points to reaches the end of its lifetime.

.. _9899_6.2.4p3:

:ref:`3 <9899_6.2.4p3>` An object whose identifier is declared with external or internal linkage, or with the storage-class specifier static has static storage duration. Its lifetime is the entire execution of the program and its stored value is initialized only once, prior to program startup.

.. _9899_6.2.4p4:

:ref:`4 <9899_6.2.4p4>` An object whose identifier is declared with no linkage and without the storage-class specifier static has automatic storage duration.

.. _9899_6.2.4p5:

:ref:`5 <9899_6.2.4p5>` For such an object that does not have a variable length array type, its lifetime extends from entry into the block with which it is associated until execution of that block ends in any way. (Entering an enclosed block or calling a function suspends, but does not end, execution of the current block.) If the block is entered recursively, a new instance of the object is created each time. The initial value of the object is indeterminate. If an initialization is specified for the object, it is performed each time the declaration is reached in the execution of the block; otherwise, the value becomes indeterminate each time the declaration is reached.

.. _9899_6.2.4p6:

:ref:`6 <9899_6.2.4p6>` For such an object that does have a variable length array type, its lifetime extends from the declaration of the object until execution of the program leaves the scope of the declaration.\ [#9899_note27]_ If the scope is entered recursively, a new instance of the object is created each time. The initial value of the object is indeterminate.

**Forward references**: statements (:ref:`6.8 <9899_6.8>`), function calls (:ref:`6.5.2.2 <9899_6.5.2.2>`), declarators (:ref:`6.7.5 <9899_6.7.5>`), array declarators (:ref:`6.7.5.2 <9899_6.7.5.2>`), initialization (:ref:`6.7.8 <9899_6.7.8>`).







.. rubric:: Footnotes

.. [#9899_note25] The term ''constant address'' means that two pointers to the object constructed at possibly different times will compare equal. The address may be different during two different executions of the same program.
.. [#9899_note26] In the case of a volatile object, the last store need not be explicit in the program.
.. [#9899_note27] Leaving the innermost block containing the declaration, or jumping to a point in that block or an embedded block prior to the declaration, leaves the scope of the declaration.
