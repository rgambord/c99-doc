.. _9899_6.9.2:

6.9.2 External object definitions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Semantics

.. _9899_6.9.2p1:

:ref:`1 <9899_6.9.2p1>` If the declaration of an identifier for an object has file scope and an initializer, the declaration is an external definition for the identifier.

.. _9899_6.9.2p2:

:ref:`2 <9899_6.9.2p2>` A declaration of an identifier for an object that has file scope without an initializer, and without a storage-class specifier or with the storage-class specifier static, constitutes a tentative definition. If a translation unit contains one or more tentative definitions for an identifier, and the translation unit contains no external definition for that identifier, then the behavior is exactly as if the translation unit contains a file scope declaration of that identifier, with the composite type as of the end of the translation unit, with an initializer equal to 0.

.. _9899_6.9.2p3:

:ref:`3 <9899_6.9.2p3>` If the declaration of an identifier for an object is a tentative definition and has internal linkage, the declared type shall not be an incomplete type.

.. _9899_6.9.2p4:

:ref:`4 <9899_6.9.2p4>` EXAMPLE 1

::

    int i1 = 1;                    // definition, external linkage
    static int i2 = 2;             // definition, internal linkage
    extern int i3 = 3;             // definition, external linkage
    int i4;                        // tentative definition, external linkage
    static int i5;                 // tentative definition, internal linkage
    int   i1;                      // valid tentative definition, refers to previous
    int   i2;                      // 6.2.2 renders undefined, linkage disagreement
    int   i3;                      // valid tentative definition, refers to previous
    int   i4;                      // valid tentative definition, refers to previous
    int   i5;                      // 6.2.2 renders undefined, linkage disagreement
    extern    int   i1;            // refers to previous, whose linkage is external
    extern    int   i2;            // refers to previous, whose linkage is internal
    extern    int   i3;            // refers to previous, whose linkage is external
    extern    int   i4;            // refers to previous, whose linkage is external
    extern    int   i5;            // refers to previous, whose linkage is internal

.. _9899_6.9.2p5:

:ref:`5 <9899_6.9.2p5>` EXAMPLE 2 If at the end of the translation unit containing

::

    int i[];

the array i still has incomplete type, the implicit initializer causes it to have one element, which is set to zero on program startup.

