.. _9899_6.7.3.1:

6.7.3.1 Formal definition of restrict
'''''''''''''''''''''''''''''''''''''

.. _9899_6.7.3.1p1:

:ref:`1 <9899_6.7.3.1p1>` Let D be a declaration of an ordinary identifier that provides a means of designating an object P as a restrict-qualified pointer to type T.

.. _9899_6.7.3.1p2:

:ref:`2 <9899_6.7.3.1p2>` If D appears inside a block and does not have storage class extern, let B denote the block. If D appears in the list of parameter declarations of a function definition, let B denote the associated block. Otherwise, let B denote the block of main (or the block of whatever function is called at program startup in a freestanding environment).

.. _9899_6.7.3.1p3:

:ref:`3 <9899_6.7.3.1p3>` In what follows, a pointer expression E is said to be based on object P if (at some sequence point in the execution of B prior to the evaluation of E) modifying P to point to a copy of the array object into which it formerly pointed would change the value of E.\ [#9899_note119]_ Note that ''based'' is defined only for expressions with pointer types.

.. _9899_6.7.3.1p4:

:ref:`4 <9899_6.7.3.1p4>` During each execution of B, let L be any lvalue that has &L based on P. If L is used to access the value of the object X that it designates, and X is also modified (by any means), then the following requirements apply: T shall not be const-qualified. Every other lvalue used to access the value of X shall also have its address based on P. Every access that modifies X shall be considered also to modify P, for the purposes of this subclause. If P is assigned the value of a pointer expression E that is based on another restricted pointer object P2, associated with block B2, then either the execution of B2 shall begin before the execution of B, or the execution of B2 shall end prior to the assignment. If these requirements are not met, then the behavior is undefined.

.. _9899_6.7.3.1p5:

:ref:`5 <9899_6.7.3.1p5>` Here an execution of B means that portion of the execution of the program that would correspond to the lifetime of an object with scalar type and automatic storage duration associated with B.

.. _9899_6.7.3.1p6:

:ref:`6 <9899_6.7.3.1p6>` A translator is free to ignore any or all aliasing implications of uses of restrict.

.. _9899_6.7.3.1p7:

:ref:`7 <9899_6.7.3.1p7>` EXAMPLE 1 The file scope declarations

::

    int * restrict a;
    int * restrict b;
    extern int c[];

assert that if an object is accessed using one of a, b, or c, and that object is modified anywhere in the program, then it is never accessed using either of the other two.

.. _9899_6.7.3.1p8:

:ref:`8 <9899_6.7.3.1p8>` EXAMPLE 2 The function parameter declarations in the following example

::

    void f(int n, int * restrict p, int * restrict q)
    {
          while (n-- > 0)
                *p++ = *q++;
    }

assert that, during each execution of the function, if an object is accessed through one of the pointer parameters, then it is not also accessed through the other.

.. _9899_6.7.3.1p9:

:ref:`9 <9899_6.7.3.1p9>` The benefit of the restrict qualifiers is that they enable a translator to make an effective dependence analysis of function f without examining any of the calls of f in the program. The cost is that the programmer has to examine all of those calls to ensure that none give undefined behavior. For example, the second call of f in g has undefined behavior because each of d[1] through d[49] is accessed through both p and q.

::

    void g(void)
    {
          extern int d[100];
          f(50, d + 50, d); // valid
          f(50, d + 1, d); // undefined behavior
    }

.. _9899_6.7.3.1p10:

:ref:`10 <9899_6.7.3.1p10>` EXAMPLE 3 The function parameter declarations

::

    void h(int n, int * restrict p, int * restrict q, int * restrict r)
    {
          int i;
          for (i = 0; i < n; i++)
                 p[i] = q[i] + r[i];
    }

illustrate how an unmodified object can be aliased through two restricted pointers. In particular, if a and b are disjoint arrays, a call of the form h(100, a, b, b) has defined behavior, because array b is not modified within function h.

.. _9899_6.7.3.1p11:

:ref:`11 <9899_6.7.3.1p11>` EXAMPLE 4 The rule limiting assignments between restricted pointers does not distinguish between a function call and an equivalent nested block. With one exception, only ''outer-to-inner'' assignments between restricted pointers declared in nested blocks have defined behavior.

::

    {
             int * restrict p1;
             int * restrict q1;
             p1 = q1; // undefined behavior
             {
                   int * restrict p2 = p1; // valid
                   int * restrict q2 = q1; // valid
                   p1 = q2;                // undefined behavior
                   p2 = q2;                // undefined behavior
             }
    }

.. _9899_6.7.3.1p12:

:ref:`12 <9899_6.7.3.1p12>` The one exception allows the value of a restricted pointer to be carried out of the block in which it (or, more precisely, the ordinary identifier used to designate it) is declared when that block finishes execution. For example, this permits new_vector to return a vector.

::

    typedef struct { int n; float * restrict v; } vector;
    vector new_vector(int n)
    {
          vector t;
          t.n = n;
          t.v = malloc(n * sizeof (float));
          return t;
    }





.. rubric:: Footnotes

.. [#9899_note119] In other words, E depends on the value of P itself rather than on the value of an object referenced indirectly through P. For example, if identifier p has type (int \**restrict), then the pointer expressions p and p+1 are based on the restricted pointer object designated by p, but the pointer expressions \*p and p[1] are not.
