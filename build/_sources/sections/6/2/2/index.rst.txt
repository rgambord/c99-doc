.. _9899_6.2.2:

6.2.2 Linkages of identifiers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_6.2.2p1:

.. container:: snum

   :ref:`1 <9899_6.2.2p1>`

An identifier declared in different scopes or in the same scope more than once can be made to refer to the same object or function by a process called linkage.\ [#9899_note21]_ There are three kinds of linkage: external, internal, and none.

.. _9899_6.2.2p2:

.. container:: snum

   :ref:`2 <9899_6.2.2p2>`

In the set of translation units and libraries that constitutes an entire program, each declaration of a particular identifier with external linkage denotes the same object or function. Within one translation unit, each declaration of an identifier with internal linkage denotes the same object or function. Each declaration of an identifier with no linkage denotes a unique entity.

.. _9899_6.2.2p3:

.. container:: snum

   :ref:`3 <9899_6.2.2p3>`

If the declaration of a file scope identifier for an object or a function contains the storage- class specifier static, the identifier has internal linkage.\ [#9899_note22]_

.. _9899_6.2.2p4:

.. container:: snum

   :ref:`4 <9899_6.2.2p4>`

For an identifier declared with the storage-class specifier extern in a scope in which a prior declaration of that identifier is visible,\ [#9899_note23]_ if the prior declaration specifies internal or external linkage, the linkage of the identifier at the later declaration is the same as the linkage specified at the prior declaration. If no prior declaration is visible, or if the prior declaration specifies no linkage, then the identifier has external linkage.

.. _9899_6.2.2p5:

.. container:: snum

   :ref:`5 <9899_6.2.2p5>`

If the declaration of an identifier for a function has no storage-class specifier, its linkage is determined exactly as if it were declared with the storage-class specifier extern. If the declaration of an identifier for an object has file scope and no storage-class specifier, its linkage is external.

.. _9899_6.2.2p6:

.. container:: snum

   :ref:`6 <9899_6.2.2p6>`

The following identifiers have no linkage: an identifier declared to be anything other than an object or a function; an identifier declared to be a function parameter; a block scope identifier for an object declared without the storage-class specifier extern.

.. _9899_6.2.2p7:

.. container:: snum

   :ref:`7 <9899_6.2.2p7>`

If, within a translation unit, the same identifier appears with both internal and external linkage, the behavior is undefined.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.7`
   - :ref:`9899_6.5`
   - :ref:`9899_6.9`
   - :ref:`9899_6.8`







.. rubric:: Footnotes

.. [#9899_note21] There is no linkage between different identifiers.
.. [#9899_note22] A function declaration can contain the storage-class specifier static only if it is at file scope; see :ref:`6.7.1 <9899_6.7.1>`.
.. [#9899_note23] As specified in :ref:`6.2.1 <9899_6.2.1>`, the later declaration might hide the prior declaration.
