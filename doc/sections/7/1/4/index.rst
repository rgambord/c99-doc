.. _9899_7.1.4:

7.1.4 Use of library functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_7.1.4p1:

.. container:: snum

   :ref:`1 <9899_7.1.4p1>`

Each of the following statements applies unless explicitly stated otherwise in the detailed descriptions that follow: If an argument to a function has an invalid value (such as a value outside the domain of the function, or a pointer outside the address space of the program, or a null pointer, or a pointer to non-modifiable storage when the corresponding parameter is not const-qualified) or a type (after promotion) not expected by a function with variable number of arguments, the behavior is undefined. If a function argument is described as being an array, the pointer actually passed to the function shall have a value such that all address computations and accesses to objects (that would be valid if the pointer did point to the first element of such an array) are in fact valid. Any function declared in a header may be additionally implemented as a function-like macro defined in the header, so if a library function is declared explicitly when its header is included, one of the techniques shown below can be used to ensure the declaration is not affected by such a macro. Any macro definition of a function can be suppressed locally by enclosing the name of the function in parentheses, because the name is then not followed by the left parenthesis that indicates expansion of a macro function name. For the same syntactic reason, it is permitted to take the address of a library function even if it is also defined as a macro.\ [#9899_note161]_ The use of `#undef` to remove any macro definition will also ensure that an actual function is referred to. Any invocation of a library function that is implemented as a macro shall expand to code that evaluates each of its arguments exactly once, fully protected by parentheses where necessary, so it is generally safe to use arbitrary expressions as arguments.\ [#9899_note162]_ Likewise, those function-like macros described in the following subclauses may be invoked in an expression anywhere a function with a compatible return type could be called.\ [#9899_note163]_ All object-like macros listed as expanding to integer constant expressions shall additionally be suitable for use in `#if` preprocessing directives.

.. _9899_7.1.4p2:

.. container:: snum

   :ref:`2 <9899_7.1.4p2>`

Provided that a library function can be declared without reference to any type defined in a header, it is also permissible to declare the function and use it without including its associated header.

.. _9899_7.1.4p3:

.. container:: snum

   :ref:`3 <9899_7.1.4p3>`

There is a sequence point immediately before a library function returns.

.. _9899_7.1.4p4:

.. container:: snum

   :ref:`4 <9899_7.1.4p4>`

The functions in the standard library are not guaranteed to be reentrant and may modify objects with static storage duration.\ [#9899_note164]_

.. _9899_7.1.4p5:

.. container:: snum

   :ref:`5 <9899_7.1.4p5>`

EXAMPLE The function atoi may be used in any of several ways:

-  by use of its associated header (possibly generating a macro expansion)

::

    #include <stdlib.h>
    const char *str;
    /* ... */
    i = atoi(str);

-  by use of its associated header (assuredly generating a true function reference)

::

    #include <stdlib.h>
    #undef atoi
    const char *str;
    /* ... */
    i = atoi(str);

   or

::

    #include <stdlib.h>
    const char *str;
    /* ... */
    i = (atoi)(str);

-  by explicit declaration

::

    extern int atoi(const char *);
    const char *str;
    /* ... */
    i = atoi(str);





::

    #define abs(x) _BUILTIN_abs(x)

for a compiler whose code generator will accept it. In this manner, a user desiring to guarantee that a given library function such as abs will be a genuine function may write

::

    #undef abs

whether the implementation's header provides a macro implementation of abs or a built-in implementation. The prototype for the function, which precedes and is hidden by any macro definition, is thereby revealed also.




.. rubric:: Footnotes

.. [#9899_note161] This means that an implementation shall provide an actual function for each library function, even if it also provides a macro for that function.
.. [#9899_note162] Such macros might not contain the sequence points that the corresponding function calls do.
.. [#9899_note163] Because external identifiers and some macro names beginning with an underscore are reserved, implementations may provide special semantics for such names. For example, the identifier \_BUILTIN_abs could be used to indicate generation of in-line code for the abs function. Thus, the appropriate header could specify
.. [#9899_note164] Thus, a signal handler cannot, in general, call standard library functions.
