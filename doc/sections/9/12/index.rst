.. _9899_B.12:

B.12 Nonlocal jumps \<setjmp.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    jmp_buf

    int setjmp(jmp_buf env);
    void longjmp(jmp_buf env, int val);

