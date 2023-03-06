.. _9899_B.5:

B.5 Floating-point environment \<fenv.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    fenv_t                 FE_OVERFLOW             FE_TOWARDZERO
    fexcept_t              FE_UNDERFLOW            FE_UPWARD
    FE_DIVBYZERO           FE_ALL_EXCEPT           FE_DFL_ENV
    FE_INEXACT             FE_DOWNWARD
    FE_INVALID             FE_TONEAREST

    #pragma STDC FENV_ACCESS on-off-switch

    int feclearexcept(int excepts);
    int fegetexceptflag(fexcept_t *flagp, int excepts);
    int feraiseexcept(int excepts);
    int fesetexceptflag(const fexcept_t *flagp, int excepts);
    int fetestexcept(int excepts);
    int fegetround(void);
    int fesetround(int round);
    int fegetenv(fenv_t *envp);
    int feholdexcept(fenv_t *envp);
    int fesetenv(const fenv_t *envp);
    int feupdateenv(const fenv_t *envp);

