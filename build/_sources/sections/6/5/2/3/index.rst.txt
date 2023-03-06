.. _9899_6.5.2.3:

6.5.2.3 Structure and union members
'''''''''''''''''''''''''''''''''''

.. rubric:: Constraints

.. _9899_6.5.2.3p1:

.. container:: snum

   :ref:`1 <9899_6.5.2.3p1>`

The first operand of the . operator shall have a qualified or unqualified structure or union type, and the second operand shall name a member of that type.

.. _9899_6.5.2.3p2:

.. container:: snum

   :ref:`2 <9899_6.5.2.3p2>`

The first operand of the -> operator shall have type "pointer to qualified or unqualified structure" or "pointer to qualified or unqualified union", and the second operand shall name a member of the type pointed to.

.. rubric:: Semantics

.. _9899_6.5.2.3p3:

.. container:: snum

   :ref:`3 <9899_6.5.2.3p3>`

A postfix expression followed by the . operator and an identifier designates a member of a structure or union object. The value is that of the named member,\ [#9899_note82]_ and is an lvalue if the first expression is an lvalue. If the first expression has qualified type, the result has the so-qualified version of the type of the designated member.

.. _9899_6.5.2.3p4:

.. container:: snum

   :ref:`4 <9899_6.5.2.3p4>`

A postfix expression followed by the -> operator and an identifier designates a member of a structure or union object. The value is that of the named member of the object to which the first expression points, and is an lvalue.\ [#9899_note83]_ If the first expression is a pointer to a qualified type, the result has the so-qualified version of the type of the designated member.

.. _9899_6.5.2.3p5:

.. container:: snum

   :ref:`5 <9899_6.5.2.3p5>`

One special guarantee is made in order to simplify the use of unions: if a union contains several structures that share a common initial sequence (see below), and if the union object currently contains one of these structures, it is permitted to inspect the common initial part of any of them anywhere that a declaration of the complete type of the union is visible. Two structures share a common initial sequence if corresponding members have compatible types (and, for bit-fields, the same widths) for a sequence of one or more initial members.

.. _9899_6.5.2.3p6:

.. container:: snum

   :ref:`6 <9899_6.5.2.3p6>`

EXAMPLE 1 If f is a function returning a structure or union, and x is a member of that structure or union, f().x is a valid postfix expression but is not an lvalue.

.. _9899_6.5.2.3p7:

.. container:: snum

   :ref:`7 <9899_6.5.2.3p7>`

EXAMPLE 2 In:

::

    struct s { int i; const int ci; };
    struct s s;
    const struct s cs;
    volatile struct s vs;

the various members have the types:

::

    s.i        int
    s.ci       const int
    cs.i       const int
    cs.ci      const int
    vs.i       volatile int
    vs.ci      volatile const int

.. _9899_6.5.2.3p8:

.. container:: snum

   :ref:`8 <9899_6.5.2.3p8>`

EXAMPLE 3 The following is a valid fragment:

::

    union {
            struct {
                  int      alltypes;
            } n;
            struct {
                  int      type;
                  int      intnode;
            } ni;
            struct {
                  int      type;
                  double doublenode;
            } nf;
    } u;
    u.nf.type = 1;
    u.nf.doublenode = 3.14;
    /* ... */
    if (u.n.alltypes == 1)
            if (sin(u.nf.doublenode) == 0.0)
                  /* ... */

The following is not a valid fragment (because the union type is not visible within function f):

::

    struct t1 { int m; };
    struct t2 { int m; };
    int f(struct t1 *p1, struct t2 *p2)
    {
          if (p1->m < 0)
                  p2->m = -p2->m;
          return p1->m;
    }
    int g()
    {
          union {
                  struct t1 s1;
                  struct t2 s2;
          } u;
          /* ... */
          return f(&u.s1, &u.s2);
    }

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.5.3.2`
   - :ref:`9899_6.7.2.1`






.. rubric:: Footnotes

.. [#9899_note82] If the member used to access the contents of a union object is not the same as the member last used to store a value in the object, the appropriate part of the object representation of the value is reinterpreted as an object representation in the new type as described in :ref:`6.2.6 <9899_6.2.6>` (a process sometimes called "type punning"). This might be a trap representation.
.. [#9899_note83] If &E is a valid pointer expression (where & is the "address-of '' operator, which generates a pointer to its operand), the expression (&E)->MOS is the same as E.MOS.
