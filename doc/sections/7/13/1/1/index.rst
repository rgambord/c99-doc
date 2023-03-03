.. _9899_7.13.1.1:

7.13.1.1 The setjmp macro
'''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.13.1.1p1:

:ref:`1 <9899_7.13.1.1p1>`

::

    #include <setjmp.h>
    int setjmp(jmp_buf env);

.. rubric:: Description

.. _9899_7.13.1.1p2:

:ref:`2 <9899_7.13.1.1p2>` The setjmp macro saves its calling environment in its jmp_buf argument for later use by the longjmp function.

.. rubric:: Returns

.. _9899_7.13.1.1p3:

:ref:`3 <9899_7.13.1.1p3>` If the return is from a direct invocation, the setjmp macro returns the value zero. If the return is from a call to the longjmp function, the setjmp macro returns a nonzero value.

.. rubric:: Environmental limits

.. _9899_7.13.1.1p4:

:ref:`4 <9899_7.13.1.1p4>` An invocation of the setjmp macro shall appear only in one of the following contexts:

-  the entire controlling expression of a selection or iteration statement;
-  one operand of a relational or equality operator with the other operand an integer constant expression, with the resulting expression being the entire controlling expression of a selection or iteration statement;
-  the operand of a unary ! operator with the resulting expression being the entire controlling expression of a selection or iteration statement; or
-  the entire expression of an expression statement (possibly cast to void).

.. _9899_7.13.1.1p5:

:ref:`5 <9899_7.13.1.1p5>` If the invocation appears in any other context, the behavior is undefined.

