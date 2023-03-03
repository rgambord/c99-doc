.. _9899_7.6.4.4:

7.6.4.4 The feupdateenv function
''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.6.4.4p1:

:ref:`1 <9899_7.6.4.4p1>`

::

    #include <fenv.h>
    int feupdateenv(const fenv_t *envp);

.. rubric:: Description

.. _9899_7.6.4.4p2:

:ref:`2 <9899_7.6.4.4p2>` The feupdateenv function attempts to save the currently raised floating-point exceptions in its automatic storage, install the floating-point environment represented by the object pointed to by envp, and then raise the saved floating-point exceptions. The argument envp shall point to an object set by a call to feholdexcept or fegetenv, or equal a floating-point environment macro.

.. rubric:: Returns

.. _9899_7.6.4.4p3:

:ref:`3 <9899_7.6.4.4p3>` The feupdateenv function returns zero if all the actions were successfully carried out. Otherwise, it returns a nonzero value.

.. _9899_7.6.4.4p4:

:ref:`4 <9899_7.6.4.4p4>` EXAMPLE Hide spurious underflow floating-point exceptions:

::

    #include <fenv.h>
    double f(double x)
    {
          #pragma STDC FENV_ACCESS ON
          double result;
          fenv_t save_env;
          if (feholdexcept(&save_env))
                return /* indication of an environmental problem */;
          // compute result
          if (/* test spurious underflow */)
                if (feclearexcept(FE_UNDERFLOW))
                         return /* indication of an environmental problem */;
          if (feupdateenv(&save_env))
                return /* indication of an environmental problem */;
          return result;
    }

.. _9899_7.7:

