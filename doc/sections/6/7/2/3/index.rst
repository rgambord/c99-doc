.. _9899_6.7.2.3:

6.7.2.3 Tags
''''''''''''

.. rubric:: Constraints

.. _9899_6.7.2.3p1:

.. container:: snum

   :ref:`1 <9899_6.7.2.3p1>`

A specific type shall have its content defined at most once.

.. _9899_6.7.2.3p2:

.. container:: snum

   :ref:`2 <9899_6.7.2.3p2>`

Where two declarations that use the same tag declare the same type, they shall both use the same choice of struct, union, or enum.

.. _9899_6.7.2.3p3:

.. container:: snum

   :ref:`3 <9899_6.7.2.3p3>`

A type specifier of the form

.. code-block:: text

    enum identifier

without an enumerator list shall only appear after the type it specifies is complete.

.. rubric:: Semantics

.. _9899_6.7.2.3p4:

.. container:: snum

   :ref:`4 <9899_6.7.2.3p4>`

All declarations of structure, union, or enumerated types that have the same scope and use the same tag declare the same type. The type is incomplete\ [#9899_note111]_ until the closing brace of the list defining the content, and complete thereafter.

.. _9899_6.7.2.3p5:

.. container:: snum

   :ref:`5 <9899_6.7.2.3p5>`

Two declarations of structure, union, or enumerated types which are in different scopes or use different tags declare distinct types. Each declaration of a structure, union, or enumerated type which does not include a tag declares a distinct type.

.. _9899_6.7.2.3p6:

.. container:: snum

   :ref:`6 <9899_6.7.2.3p6>`

A type specifier of the form

.. code-block:: text

    struct-or-union identifieropt { struct-declaration-list }

or

.. code-block:: text

    enum identifier { enumerator-list }

or

.. code-block:: text

    enum identifier { enumerator-list , }

declares a structure, union, or enumerated type. The list defines the structure content, union content, or enumeration content. If an identifier is provided,\ [#9899_note112]_ the type specifier also declares the identifier to be the tag of that type.

.. _9899_6.7.2.3p7:

.. container:: snum

   :ref:`7 <9899_6.7.2.3p7>`

A declaration of the form

.. code-block:: text

    struct-or-union identifier ;

specifies a structure or union type and declares the identifier as a tag of that type.\ [#9899_note113]_

.. _9899_6.7.2.3p8:

.. container:: snum

   :ref:`8 <9899_6.7.2.3p8>`

If a type specifier of the form

.. code-block:: text

    struct-or-union identifier

occurs other than as part of one of the above forms, and no other declaration of the identifier as a tag is visible, then it declares an incomplete structure or union type, and declares the identifier as the tag of that type.\ [#9899_note113]_

.. _9899_6.7.2.3p9:

.. container:: snum

   :ref:`9 <9899_6.7.2.3p9>`

If a type specifier of the form

.. code-block:: text

    struct-or-union identifier

or

.. code-block:: text

    enum identifier

occurs other than as part of one of the above forms, and a declaration of the identifier as a tag is visible, then it specifies the same type as that other declaration, and does not redeclare the tag.

.. _9899_6.7.2.3p10:

.. container:: snum

   :ref:`10 <9899_6.7.2.3p10>`

EXAMPLE 1 This mechanism allows declaration of a self-referential structure.

::

    struct tnode {
          int count;
          struct tnode *left, *right;
    };

specifies a structure that contains an integer and two pointers to objects of the same type. Once this declaration has been given, the declaration

::

    struct tnode s, *sp;

declares s to be an object of the given type and sp to be a pointer to an object of the given type. With these declarations, the expression sp->left refers to the left struct tnode pointer of the object to which sp points; the expression s.right->count designates the count member of the right struct tnode pointed to from s.

.. _9899_6.7.2.3p11:

.. container:: snum

   :ref:`11 <9899_6.7.2.3p11>`

The following alternative formulation uses the typedef mechanism:

::

    typedef struct tnode TNODE;
    struct tnode {
          int count;
          TNODE *left, *right;
    };
    TNODE s, *sp;

.. _9899_6.7.2.3p12:

.. container:: snum

   :ref:`12 <9899_6.7.2.3p12>`

EXAMPLE 2 To illustrate the use of prior declaration of a tag to specify a pair of mutually referential structures, the declarations

::

    struct s1 { struct s2 *s2p; /* ... */ }; // D1
    struct s2 { struct s1 *s1p; /* ... */ }; // D2

specify a pair of structures that contain pointers to each other. Note, however, that if s2 were already declared as a tag in an enclosing scope, the declaration D1 would refer to it, not to the tag s2 declared in D2. To eliminate this context sensitivity, the declaration

::

    struct s2;

may be inserted ahead of D1. This declares a new tag s2 in the inner scope; the declaration D2 then completes the specification of the new type.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.7.5`
   - :ref:`9899_6.7.5.2`
   - :ref:`9899_6.7.7`







.. rubric:: Footnotes

.. [#9899_note111] An incomplete type may only by used when the size of an object of that type is not needed. It is not needed, for example, when a typedef name is declared to be a specifier for a structure or union, or when a pointer to or a function returning a structure or union is being declared. (See incomplete types in :ref:`6.2.5 <9899_6.2.5>`.) The specification has to be complete before such a function is called or defined.
.. [#9899_note112] If there is no identifier, the type can, within the translation unit, only be referred to by the declaration of which it is a part. Of course, when the declaration is of a typedef name, subsequent declarations can make use of that typedef name to declare objects having the specified structure, union, or enumerated type.
.. [#9899_note113] A similar construction with enum does not exist.
