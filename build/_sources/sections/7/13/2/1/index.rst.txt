.. _9899_7.13.2.1:

7.13.2.1 The longjmp function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.13.2.1p1:

.. container:: snum

   :ref:`1 <9899_7.13.2.1p1>`



::

    #include <setjmp.h>
    void longjmp(jmp_buf env, int val);

.. rubric:: Description

.. _9899_7.13.2.1p2:

.. container:: snum

   :ref:`2 <9899_7.13.2.1p2>`

The longjmp function restores the environment saved by the most recent invocation of the setjmp macro in the same invocation of the program with the corresponding jmp_buf argument. If there has been no such invocation, or if the function containing the invocation of the setjmp macro has terminated execution\ [#9899_note217]_ in the interim, or if the invocation of the setjmp macro was within the scope of an identifier with variably modified type and execution has left that scope in the interim, the behavior is undefined.

.. _9899_7.13.2.1p3:

.. container:: snum

   :ref:`3 <9899_7.13.2.1p3>`

All accessible objects have values, and all other components of the abstract machine\ [#9899_note218]_ have state, as of the time the longjmp function was called, except that the values of objects of automatic storage duration that are local to the function containing the invocation of the corresponding setjmp macro that do not have volatile-qualified type and have been changed between the setjmp invocation and longjmp call are indeterminate.

.. rubric:: Returns

.. _9899_7.13.2.1p4:

.. container:: snum

   :ref:`4 <9899_7.13.2.1p4>`

After longjmp is completed, program execution continues as if the corresponding invocation of the setjmp macro had just returned the value specified by val. The longjmp function cannot cause the setjmp macro to return the value 0; if val is 0, the setjmp macro returns the value 1.

.. _9899_7.13.2.1p5:

.. container:: snum

   :ref:`5 <9899_7.13.2.1p5>`

EXAMPLE The longjmp function that returns control back to the point of the setjmp invocation might cause memory associated with a variable length array object to be squandered.

::

    #include <setjmp.h>
    jmp_buf buf;
    void g(int n);
    void h(int n);
    int n = 6;
    void f(void)
    {
          int x[n];          // valid: f is not terminated
          setjmp(buf);
          g(n);
    }
    void g(int n)
    {
          int a[n];          // a may remain allocated
          h(n);
    }
    void h(int n)
    {
          int b[n];          // b may remain allocated
          longjmp(buf, 2);   // might cause memory loss
    }






.. rubric:: Footnotes

.. [#9899_note217] For example, by executing a return statement or because another longjmp call has caused a transfer to a setjmp invocation in a function earlier in the set of nested calls.
.. [#9899_note218] This includes, but is not limited to, the floating-point status flags and the state of open files.
