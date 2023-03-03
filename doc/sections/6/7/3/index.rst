.. _9899_6.7.3:

6.7.3 Type qualifiers
^^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index


.. rubric:: Syntax

.. _9899_6.7.3p1:

:ref:`1 <9899_6.7.3p1>`

.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            type-qualifier
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            const
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            restrict
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            volatile

.. rubric:: Constraints

.. _9899_6.7.3p2:

:ref:`2 <9899_6.7.3p2>` Types other than pointer types derived from object or incomplete types shall not be restrict-qualified.

.. rubric:: Semantics

.. _9899_6.7.3p3:

:ref:`3 <9899_6.7.3p3>` The properties associated with qualified types are meaningful only for expressions that are lvalues.\ [#9899_note114]_

.. _9899_6.7.3p4:

:ref:`4 <9899_6.7.3p4>` If the same qualifier appears more than once in the same specifier-qualifier-list, either directly or via one or more typedefs, the behavior is the same as if it appeared only once.

.. _9899_6.7.3p5:

:ref:`5 <9899_6.7.3p5>` If an attempt is made to modify an object defined with a const-qualified type through use of an lvalue with non-const-qualified type, the behavior is undefined. If an attempt is made to refer to an object defined with a volatile-qualified type through use of an lvalue with non-volatile-qualified type, the behavior is undefined.\ [#9899_note115]_

.. _9899_6.7.3p6:

:ref:`6 <9899_6.7.3p6>` An object that has volatile-qualified type may be modified in ways unknown to the implementation or have other unknown side effects. Therefore any expression referring to such an object shall be evaluated strictly according to the rules of the abstract machine, as described in :ref:`5.1.2.3 <9899_5.1.2.3>`. Furthermore, at every sequence point the value last stored in the object shall agree with that prescribed by the abstract machine, except as modified by the unknown factors mentioned previously.\ [#9899_note116]_ What constitutes an access to an object that has volatile-qualified type is implementation-defined.

.. _9899_6.7.3p7:

:ref:`7 <9899_6.7.3p7>` An object that is accessed through a restrict-qualified pointer has a special association with that pointer. This association, defined in :ref:`6.7.3.1 <9899_6.7.3.1>` below, requires that all accesses to that object use, directly or indirectly, the value of that particular pointer.\ [#9899_note117]_ The intended use of the restrict qualifier (like the register storage class) is to promote optimization, and deleting all instances of the qualifier from all preprocessing translation units composing a conforming program does not change its meaning (i.e., observable behavior).

.. _9899_6.7.3p8:

:ref:`8 <9899_6.7.3p8>` If the specification of an array type includes any type qualifiers, the element type is so- qualified, not the array type. If the specification of a function type includes any type qualifiers, the behavior is undefined.\ [#9899_note118]_

.. _9899_6.7.3p9:

:ref:`9 <9899_6.7.3p9>` For two qualified types to be compatible, both shall have the identically qualified version of a compatible type; the order of type qualifiers within a list of specifiers or qualifiers does not affect the specified type.

.. _9899_6.7.3p10:

:ref:`10 <9899_6.7.3p10>` EXAMPLE 1 An object declared

::

    extern const volatile int real_time_clock;

may be modifiable by hardware, but cannot be assigned to, incremented, or decremented.

.. _9899_6.7.3p11:

:ref:`11 <9899_6.7.3p11>` EXAMPLE 2 The following declarations and expressions illustrate the behavior when type qualifiers modify an aggregate type:

::

    const struct s { int mem; } cs = { 1 };
    struct s ncs; // the object ncs is modifiable
    typedef int A[2][3];
    const A a = {{4, 5, 6}, {7, 8, 9}}; // array of array of const int
    int *pi;
    const int *pci;
    ncs = cs;             //   valid
    cs = ncs;             //   violates modifiable lvalue constraint for =
    pi = &ncs.mem;        //   valid
    pi = &cs.mem;         //   violates type constraints for =
    pci = &cs.mem;        //   valid
    pi = a[0];            //   invalid: a[0] has type ''const int *''









.. rubric:: Footnotes

.. [#9899_note114] The implementation may place a const object that is not volatile in a read-only region of storage. Moreover, the implementation need not allocate storage for such an object if its address is never used.
.. [#9899_note115] This applies to those objects that behave as if they were defined with qualified types, even if they are never actually defined as objects in the program (such as an object at a memory-mapped input/output address).
.. [#9899_note116] A volatile declaration may be used to describe an object corresponding to a memory-mapped input/output port or an object accessed by an asynchronously interrupting function. Actions on objects so declared shall not be ''optimized out'' by an implementation or reordered except as permitted by the rules for evaluating expressions.
.. [#9899_note117] For example, a statement that assigns a value returned by malloc to a single pointer establishes this association between the allocated object and the pointer.
.. [#9899_note118] Both of these can occur through the use of typedefs.
