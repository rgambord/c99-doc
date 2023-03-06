.. _9899_B.13:

B.13 Signal handling \<signal.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    sig_atomic_t   SIG_IGN            SIGILL            SIGTERM
    SIG_DFL        SIGABRT            SIGINT
    SIG_ERR        SIGFPE             SIGSEGV
    void (*signal(int sig, void (*func)(int)))(int);
    int raise(int sig);

