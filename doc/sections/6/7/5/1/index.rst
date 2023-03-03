.. _9899_6.7.5.1:

6.7.5.1 Pointer declarators
'''''''''''''''''''''''''''

.. rubric:: Semantics

.. _9899_6.7.5.1p1:

:ref:`1 <9899_6.7.5.1p1>` If, in the declaration ''T D1'', D1 has the form

.. code-block:: text

    * type-qualifier-listopt D

and the type specified for ident in the declaration ''T D'' is ''derived-declarator-type-list T '', then the type specified for ident is ''derived-declarator-type-list type-qualifier-list pointer to T ''. For each type qualifier in the list, ident is a so-qualified pointer.

.. _9899_6.7.5.1p2:

:ref:`2 <9899_6.7.5.1p2>` For two pointer types to be compatible, both shall be identically qualified and both shall be pointers to compatible types.

.. _9899_6.7.5.1p3:

:ref:`3 <9899_6.7.5.1p3>` EXAMPLE The following pair of declarations demonstrates the difference between a ''variable pointer to a constant value'' and a ''constant pointer to a variable value''.

::

    const int *ptr_to_constant;
    int *const constant_ptr;

The contents of any object pointed to by ptr_to_constant shall not be modified through that pointer, but ptr_to_constant itself may be changed to point to another object. Similarly, the contents of the int pointed to by constant_ptr may be modified, but constant_ptr itself shall always point to the same location.

.. _9899_6.7.5.1p4:

:ref:`4 <9899_6.7.5.1p4>` The declaration of the constant pointer constant_ptr may be clarified by including a definition for the type ''pointer to int''.

::

    typedef int *int_ptr;
    const int_ptr constant_ptr;

declares constant_ptr as an object that has type ''const-qualified pointer to int''.

