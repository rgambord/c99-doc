.. _9899_6.7.1:

6.7.1 Storage-class specifiers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.7.1p1:

:ref:`1 <9899_6.7.1p1>`

.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            storage-class-specifier
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            typedef
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            extern
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            static
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            auto
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            register

.. rubric:: Constraints

.. _9899_6.7.1p2:

:ref:`2 <9899_6.7.1p2>` At most, one storage-class specifier may be given in the declaration specifiers in a declaration.\ [#9899_note102]_

.. rubric:: Semantics

.. _9899_6.7.1p3:

:ref:`3 <9899_6.7.1p3>` The typedef specifier is called a ''storage-class specifier'' for syntactic convenience only; it is discussed in :ref:`6.7.7 <9899_6.7.7>`. The meanings of the various linkages and storage durations were discussed in :ref:`6.2.2 <9899_6.2.2>` and :ref:`6.2.4 <9899_6.2.4>`.

.. _9899_6.7.1p4:

:ref:`4 <9899_6.7.1p4>` A declaration of an identifier for an object with storage-class specifier register suggests that access to the object be as fast as possible. The extent to which such suggestions are effective is implementation-defined.\ [#9899_note103]_

.. _9899_6.7.1p5:

:ref:`5 <9899_6.7.1p5>` The declaration of an identifier for a function that has block scope shall have no explicit storage-class specifier other than extern.

.. _9899_6.7.1p6:

:ref:`6 <9899_6.7.1p6>` If an aggregate or union object is declared with a storage-class specifier other than typedef, the properties resulting from the storage-class specifier, except with respect to linkage, also apply to the members of the object, and so on recursively for any aggregate or union member objects.

**Forward references**: type definitions (:ref:`6.7.7 <9899_6.7.7>`).






.. rubric:: Footnotes

.. [#9899_note102] See ''future language directions'' (:ref:`6.11.5 <9899_6.11.5>`).
.. [#9899_note103] The implementation may treat any register declaration simply as an auto declaration. However, whether or not addressable storage is actually used, the address of any part of an object declared with storage-class specifier register cannot be computed, either explicitly (by use of the unary & operator as discussed in :ref:`6.5.3.2 <9899_6.5.3.2>`) or implicitly (by converting an array name to a pointer as discussed in :ref:`6.3.2.1 <9899_6.3.2.1>`). Thus, the only operator that can be applied to an array declared with storage-class specifier register is sizeof.
