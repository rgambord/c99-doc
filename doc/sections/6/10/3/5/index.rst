.. _9899_6.10.3.5:

6.10.3.5 Scope of macro definitions
'''''''''''''''''''''''''''''''''''

.. _9899_6.10.3.5p1:

:ref:`1 <9899_6.10.3.5p1>` A macro definition lasts (independent of block structure) until a corresponding #undef directive is encountered or (if none is encountered) until the end of the preprocessing translation unit. Macro definitions have no significance after translation phase 4.

.. _9899_6.10.3.5p2:

:ref:`2 <9899_6.10.3.5p2>` A preprocessing directive of the form

.. code-block:: text

    # undef identifier new-line

causes the specified identifier no longer to be defined as a macro name. It is ignored if the specified identifier is not currently defined as a macro name.

.. _9899_6.10.3.5p3:

:ref:`3 <9899_6.10.3.5p3>` EXAMPLE 1 The simplest use of this facility is to define a ''manifest constant'', as in

::

    #define TABSIZE 100
    int table[TABSIZE];

.. _9899_6.10.3.5p4:

:ref:`4 <9899_6.10.3.5p4>` EXAMPLE 2 The following defines a function-like macro whose value is the maximum of its arguments. It has the advantages of working for any compatible types of the arguments and of generating in-line code without the overhead of function calling. It has the disadvantages of evaluating one or the other of its arguments a second time (including side effects) and generating more code than a function if invoked several times. It also cannot have its address taken, as it has none.

::

    #define max(a, b) ((a) > (b) ? (a) : (b))

The parentheses ensure that the arguments and the resulting expression are bound properly.

.. _9899_6.10.3.5p5:

:ref:`5 <9899_6.10.3.5p5>` EXAMPLE 3 To illustrate the rules for redefinition and reexamination, the sequence

::

    #define   x         3
    #define   f(a)      f(x * (a))
    #undef    x
    #define   x         2
    #define   g         f
    #define   z         z[0]
    #define   h         g(~
    #define   m(a)      a(w)
    #define   w         0,1
    #define   t(a)      a
    #define   p()       int
    #define   q(x)      x
    #define   r(x,y)    x ## y
    #define   str(x)    # x
    f(y+1) + f(f(z)) % t(t(g)(0) + t)(1);
    g(x+(3,4)-w) | h 5) & m
          (f)^m(m);
    p() i[q()] = { q(1), r(2,3), r(4,), r(,5), r(,) };
    char c[2][6] = { str(hello), str() };

results in

::

    f(2 * (y+1)) + f(2 * (f(2 * (z[0])))) % f(2 * (0)) + t(1);
    f(2 * (2+(3,4)-0,1)) | f(2 * (~ 5)) & f(2 * (0,1))^m(0,1);
    int i[] = { 1, 23, 4, 5, };
    char c[2][6] = { "hello", "" };

.. _9899_6.10.3.5p6:

:ref:`6 <9899_6.10.3.5p6>` EXAMPLE 4 To illustrate the rules for creating character string literals and concatenating tokens, the sequence

.. code-block:: text

    #define str(s)      # s
    #define xstr(s)     str(s)
    #define debug(s, t) printf("x" # s "= %d, x" # t "= %s", \
                            x ## s, x ## t)
    #define INCFILE(n) vers ## n
    #define glue(a, b) a ## b
    #define xglue(a, b) glue(a, b)
    #define HIGHLOW     "hello"
    #define LOW         LOW ", world"
    debug(1, 2);
    fputs(str(strncmp("abc\0d", "abc", '\4') // this goes away
          == 0) str(: @\n), s);
    #include xstr(INCFILE(2).h)
    glue(HIGH, LOW);
    xglue(HIGH, LOW)

results in

::

    printf("x" "1" "= %d, x" "2" "= %s", x1, x2);
    fputs(
      "strncmp(\"abc\\0d\", \"abc\", '\\4') == 0" ": @\n",
      s);
    #include "vers2.h"    (after macro replacement, before file access)
    "hello";
    "hello" ", world"

or, after concatenation of the character string literals,

::

    printf("x1= %d, x2= %s", x1, x2);
    fputs(
      "strncmp(\"abc\\0d\", \"abc\", '\\4') == 0: @\n",
      s);
    #include "vers2.h"    (after macro replacement, before file access)
    "hello";
    "hello, world"

Space around the # and ## tokens in the macro definition is optional.

.. _9899_6.10.3.5p7:

:ref:`7 <9899_6.10.3.5p7>` EXAMPLE 5 To illustrate the rules for placemarker preprocessing tokens, the sequence

::

    #define t(x,y,z) x ## y ## z
    int j[] = { t(1,2,3), t(,4,5), t(6,,7), t(8,9,),
               t(10,,), t(,11,), t(,,12), t(,,) };

results in

::

    int j[] = { 123, 45, 67, 89,
                10, 11, 12, };

.. _9899_6.10.3.5p8:

:ref:`8 <9899_6.10.3.5p8>` EXAMPLE 6 To demonstrate the redefinition rules, the following sequence is valid.

::

    #define      OBJ_LIKE      (1-1)
    #define      OBJ_LIKE      /* white space */ (1-1) /* other */
    #define      FUNC_LIKE(a)   ( a )
    #define      FUNC_LIKE( a )( /* note the white space */ \
                                 a /* other stuff on this line
                                     */ )

But the following redefinitions are invalid:

::

    #define      OBJ_LIKE    (0)     // different token sequence
    #define      OBJ_LIKE    (1 - 1) // different white space
    #define      FUNC_LIKE(b) ( a ) // different parameter usage
    #define      FUNC_LIKE(b) ( b ) // different parameter spelling

.. _9899_6.10.3.5p9:

:ref:`9 <9899_6.10.3.5p9>` EXAMPLE 7 Finally, to show the variable argument list macro facilities:

::

    #define debug(...)       fprintf(stderr, __VA_ARGS__)
    #define showlist(...)    puts(#__VA_ARGS__)
    #define report(test, ...) ((test)?puts(#test):\
                printf(__VA_ARGS__))
    debug("Flag");
    debug("X = %d\n", x);
    showlist(The first, second, and third items.);
    report(x>y, "x is %d but y is %d", x, y);

results in

::

    fprintf(stderr, "Flag" );
    fprintf(stderr, "X = %d\n", x );
    puts( "The first, second, and third items." );
    ((x>y)?puts("x>y"):
                printf("x is %d but y is %d", x, y));

