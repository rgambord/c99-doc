.. _9899_7.15.1.4:

7.15.1.4 The va_start macro
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.15.1.4p1:

:ref:`1 <9899_7.15.1.4p1>`

::

    #include <stdarg.h>
    void va_start(va_list ap, parmN);

.. rubric:: Description

.. _9899_7.15.1.4p2:

:ref:`2 <9899_7.15.1.4p2>` The va_start macro shall be invoked before any access to the unnamed arguments.

.. _9899_7.15.1.4p3:

:ref:`3 <9899_7.15.1.4p3>` The va_start macro initializes ap for subsequent use by the va_arg and va_end macros. Neither the va_start nor va_copy macro shall be invoked to reinitialize ap without an intervening invocation of the va_end macro for the same ap.

.. _9899_7.15.1.4p4:

:ref:`4 <9899_7.15.1.4p4>` The parameter parmN is the identifier of the rightmost parameter in the variable parameter list in the function definition (the one just before the , \.\.\.). If the parameter parmN is declared with the register storage class, with a function or array type, or with a type that is not compatible with the type that results after application of the default argument promotions, the behavior is undefined.

.. rubric:: Returns

.. _9899_7.15.1.4p5:

:ref:`5 <9899_7.15.1.4p5>` The va_start macro returns no value.

.. _9899_7.15.1.4p6:

:ref:`6 <9899_7.15.1.4p6>` EXAMPLE 1 The function f1 gathers into an array a list of arguments that are pointers to strings (but not more than MAXARGS arguments), then passes the array as a single argument to function f2. The number of pointers is specified by the first argument to f1.

::

    #include <stdarg.h>
    #define MAXARGS   31
    void f1(int n_ptrs, ...)
    {
          va_list ap;
          char *array[MAXARGS];
          int ptr_no = 0;
          if (n_ptrs > MAXARGS)
                n_ptrs = MAXARGS;
          va_start(ap, n_ptrs);
          while (ptr_no < n_ptrs)
                array[ptr_no++] = va_arg(ap, char *);
          va_end(ap);
          f2(n_ptrs, array);
    }

Each call to f1 is required to have visible the definition of the function or a declaration such as

::

    void f1(int, ...);

.. _9899_7.15.1.4p7:

:ref:`7 <9899_7.15.1.4p7>` EXAMPLE 2 The function f3 is similar, but saves the status of the variable argument list after the indicated number of arguments; after f2 has been called once with the whole list, the trailing part of the list is gathered again and passed to function f4.

::

    #include <stdarg.h>
    #define MAXARGS 31
    void f3(int n_ptrs, int f4_after, ...)
    {
          va_list ap, ap_save;
          char *array[MAXARGS];
          int ptr_no = 0;
          if (n_ptrs > MAXARGS)
                n_ptrs = MAXARGS;
          va_start(ap, f4_after);
          while (ptr_no < n_ptrs) {
                array[ptr_no++] = va_arg(ap, char *);
                if (ptr_no == f4_after)
                      va_copy(ap_save, ap);
          }
          va_end(ap);
          f2(n_ptrs, array);
             // Now process the saved copy.
             n_ptrs -= f4_after;
             ptr_no = 0;
             while (ptr_no < n_ptrs)
                   array[ptr_no++] = va_arg(ap_save, char *);
             va_end(ap_save);
             f4(n_ptrs, array);
    }

