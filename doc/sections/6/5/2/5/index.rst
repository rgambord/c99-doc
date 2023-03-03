.. _9899_6.5.2.5:

6.5.2.5 Compound literals
'''''''''''''''''''''''''

.. rubric:: Constraints

.. _9899_6.5.2.5p1:

:ref:`1 <9899_6.5.2.5p1>` The type name shall specify an object type or an array of unknown size, but not a variable length array type.

.. _9899_6.5.2.5p2:

:ref:`2 <9899_6.5.2.5p2>` No initializer shall attempt to provide a value for an object not contained within the entire unnamed object specified by the compound literal.

.. _9899_6.5.2.5p3:

:ref:`3 <9899_6.5.2.5p3>` If the compound literal occurs outside the body of a function, the initializer list shall consist of constant expressions.

.. rubric:: Semantics

.. _9899_6.5.2.5p4:

:ref:`4 <9899_6.5.2.5p4>` A postfix expression that consists of a parenthesized type name followed by a brace- enclosed list of initializers is a compound literal. It provides an unnamed object whose value is given by the initializer list.\ [#9899_note84]_

.. _9899_6.5.2.5p5:

:ref:`5 <9899_6.5.2.5p5>` If the type name specifies an array of unknown size, the size is determined by the initializer list as specified in :ref:`6.7.8 <9899_6.7.8>`, and the type of the compound literal is that of the completed array type. Otherwise (when the type name specifies an object type), the type of the compound literal is that specified by the type name. In either case, the result is an lvalue.

.. _9899_6.5.2.5p6:

:ref:`6 <9899_6.5.2.5p6>` The value of the compound literal is that of an unnamed object initialized by the initializer list. If the compound literal occurs outside the body of a function, the object has static storage duration; otherwise, it has automatic storage duration associated with the enclosing block.

.. _9899_6.5.2.5p7:

:ref:`7 <9899_6.5.2.5p7>` All the semantic rules and constraints for initializer lists in :ref:`6.7.8 <9899_6.7.8>` are applicable to compound literals.\ [#9899_note85]_

.. _9899_6.5.2.5p8:

:ref:`8 <9899_6.5.2.5p8>` String literals, and compound literals with const-qualified types, need not designate distinct objects.\ [#9899_note86]_

.. _9899_6.5.2.5p9:

:ref:`9 <9899_6.5.2.5p9>` EXAMPLE 1 The file scope definition

::

    int *p = (int []){2, 4};

initializes p to point to the first element of an array of two ints, the first having the value two and the second, four. The expressions in this compound literal are required to be constant. The unnamed object has static storage duration.

.. _9899_6.5.2.5p10:

:ref:`10 <9899_6.5.2.5p10>` EXAMPLE 2 In contrast, in

::

    void f(void)
    {
          int *p;
          /*...*/
          p = (int [2]){*p};
          /*...*/
    }

p is assigned the address of the first element of an array of two ints, the first having the value previously pointed to by p and the second, zero. The expressions in this compound literal need not be constant. The unnamed object has automatic storage duration.

.. _9899_6.5.2.5p11:

:ref:`11 <9899_6.5.2.5p11>` EXAMPLE 3 Initializers with designations can be combined with compound literals. Structure objects created using compound literals can be passed to functions without depending on member order:

::

    drawline((struct point){.x=1, .y=1},
          (struct point){.x=3, .y=4});

Or, if drawline instead expected pointers to struct point:

::

    drawline(&(struct point){.x=1, .y=1},
          &(struct point){.x=3, .y=4});

.. _9899_6.5.2.5p12:

:ref:`12 <9899_6.5.2.5p12>` EXAMPLE 4 A read-only compound literal can be specified through constructions like:

::

    (const float []){1e0, 1e1, 1e2, 1e3, 1e4, 1e5, 1e6}

.. _9899_6.5.2.5p13:

:ref:`13 <9899_6.5.2.5p13>` EXAMPLE 5 The following three expressions have different meanings:

::

    "/tmp/fileXXXXXX"
    (char []){"/tmp/fileXXXXXX"}
    (const char []){"/tmp/fileXXXXXX"}

The first always has static storage duration and has type array of char, but need not be modifiable; the last two have automatic storage duration when they occur within the body of a function, and the first of these two is modifiable.

.. _9899_6.5.2.5p14:

:ref:`14 <9899_6.5.2.5p14>` EXAMPLE 6 Like string literals, const-qualified compound literals can be placed into read-only memory and can even be shared. For example,

::

    (const char []){"abc"} == "abc"

might yield 1 if the literals' storage is shared.

.. _9899_6.5.2.5p15:

:ref:`15 <9899_6.5.2.5p15>` EXAMPLE 7 Since compound literals are unnamed, a single compound literal cannot specify a circularly linked object. For example, there is no way to write a self-referential compound literal that could be used as the function argument in place of the named object endless_zeros below:

::

    struct int_list { int car; struct int_list *cdr; };
    struct int_list endless_zeros = {0, &endless_zeros};
    eval(endless_zeros);

.. _9899_6.5.2.5p16:

:ref:`16 <9899_6.5.2.5p16>` EXAMPLE 8 Each compound literal creates only a single object in a given scope:

::

    struct s { int i; };
    int f (void)
    {
          struct s *p = 0, *q;
          int j = 0;
    again:
          q = p, p = &((struct s){ j++ });
          if (j < 2) goto again;
              return p == q && q->i == 1;
    }

The function f() always returns the value 1.

.. _9899_6.5.2.5p17:

:ref:`17 <9899_6.5.2.5p17>` Note that if an iteration statement were used instead of an explicit goto and a labeled statement, the lifetime of the unnamed object would be the body of the loop only, and on entry next time around p would have an indeterminate value, which would result in undefined behavior.

**Forward references**: type names (:ref:`6.7.6 <9899_6.7.6>`), initialization (:ref:`6.7.8 <9899_6.7.8>`).







.. rubric:: Footnotes

.. [#9899_note84] Note that this differs from a cast expression. For example, a cast specifies a conversion to scalar types or void only, and the result of a cast expression is not an lvalue.
.. [#9899_note85] For example, subobjects without explicit initializers are initialized to zero.
.. [#9899_note86] This allows implementations to share storage for string literals and constant compound literals with the same or overlapping representations.
