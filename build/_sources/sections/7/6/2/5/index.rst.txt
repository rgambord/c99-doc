.. _9899_7.6.2.5:

7.6.2.5 The fetestexcept function
'''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.6.2.5p1:

.. container:: snum

   :ref:`1 <9899_7.6.2.5p1>`



::

    #include <fenv.h>
    int fetestexcept(int excepts);

.. rubric:: Description

.. _9899_7.6.2.5p2:

.. container:: snum

   :ref:`2 <9899_7.6.2.5p2>`

The fetestexcept function determines which of a specified subset of the floating- point exception flags are currently set. The excepts argument specifies the floating- point status flags to be queried.\ [#9899_note188]_

.. rubric:: Returns

.. _9899_7.6.2.5p3:

.. container:: snum

   :ref:`3 <9899_7.6.2.5p3>`

The fetestexcept function returns the value of the bitwise OR of the floating-point exception macros corresponding to the currently set floating-point exceptions included in excepts.

.. _9899_7.6.2.5p4:

.. container:: snum

   :ref:`4 <9899_7.6.2.5p4>`

EXAMPLE Call f if "invalid" is set, then g if "overflow" is set:

::

    #include <fenv.h>
    /* ... */
    {
            #pragma STDC FENV_ACCESS ON
            int set_excepts;
            feclearexcept(FE_INVALID | FE_OVERFLOW);
            // maybe raise exceptions
            set_excepts = fetestexcept(FE_INVALID | FE_OVERFLOW);
            if (set_excepts & FE_INVALID) f();
            if (set_excepts & FE_OVERFLOW) g();
            /* ... */
    }





.. rubric:: Footnotes

.. [#9899_note188] This mechanism allows testing several floating-point exceptions with just one function call.
