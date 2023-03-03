.. _9899_F.7.5:

F.7.5 Initialization
^^^^^^^^^^^^^^^^^^^^

.. _9899_F.7.5p1:

:ref:`1 <9899_F.7.5p1>` All computation for automatic initialization is done (as if) at execution time; thus, it is affected by any operative modes and raises floating-point exceptions as required by IEC 60559 (provided the state for the FENV_ACCESS pragma is ''on''). All computation for initialization of objects that have static storage duration is done (as if) at translation time.

.. _9899_F.7.5p2:

:ref:`2 <9899_F.7.5p2>` EXAMPLE

::

    #include <fenv.h>
    #pragma STDC FENV_ACCESS ON
    void f(void)
    {
          float u[] = { 1.1e75 };                  //   raises exceptions
          static float v = 1.1e75;                 //   does not raise exceptions
          float w = 1.1e75;                        //   raises exceptions
          double x = 1.1e75;                       //   may raise exceptions
          float y = 1.1e75f;                       //   may raise exceptions
          long double z = 1.1e75;                  //   does not raise exceptions
          /* ... */
    }

.. _9899_F.7.5p3:

:ref:`3 <9899_F.7.5p3>` The static initialization of v raises no (execution-time) floating-point exceptions because its computation is done at translation time. The automatic initialization of u and w require an execution-time conversion to float of the wider value 1.1e75, which raises floating-point exceptions. The automatic initializations of x and y entail execution-time conversion; however, in some expression evaluation methods, the conversions is not to a narrower format, in which case no floating-point exception is raised.\ [#9899_note316]_ The automatic initialization of z entails execution-time conversion, but not to a narrower format, so no floating- point exception is raised. Note that the conversions of the floating constants 1.1e75 and 1.1e75f to their internal representations occur at translation time in all cases.



::

    double_t x = 1.1e75;

could be done at translation time, regardless of the expression evaluation method.



.. rubric:: Footnotes

.. [#9899_note316] Use of float_t and double_t variables increases the likelihood of translation-time computation. For example, the automatic initialization
