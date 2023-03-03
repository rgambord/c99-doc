.. _9899_F.7.4:

F.7.4 Constant expressions
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_F.7.4p1:

:ref:`1 <9899_F.7.4p1>` An arithmetic constant expression of floating type, other than one in an initializer for an object that has static storage duration, is evaluated (as if) during execution; thus, it is affected by any operative floating-point control modes and raises floating-point exceptions as required by IEC 60559 (provided the state for the FENV_ACCESS pragma is ''on'').\ [#9899_note315]_

.. _9899_F.7.4p2:

:ref:`2 <9899_F.7.4p2>` EXAMPLE

::

    #include <fenv.h>
    #pragma STDC FENV_ACCESS ON
    void f(void)
    {
          float w[] = { 0.0/0.0 };                  //   raises an exception
          static float x = 0.0/0.0;                 //   does not raise an exception
          float y = 0.0/0.0;                        //   raises an exception
          double z = 0.0/0.0;                       //   raises an exception
          /* ... */
    }

.. _9899_F.7.4p3:

:ref:`3 <9899_F.7.4p3>` For the static initialization, the division is done at translation time, raising no (execution-time) floating- point exceptions. On the other hand, for the three automatic initializations the invalid division occurs at execution time.



::

    const static double one_third = 1.0/3.0;



.. rubric:: Footnotes

.. [#9899_note315] Where the state for the FENV_ACCESS pragma is ''on'', results of inexact expressions like 1.0/3.0 are affected by rounding modes set at execution time, and expressions such as 0.0/0.0 and 1.0/0.0 generate execution-time floating-point exceptions. The programmer can achieve the efficiency of translation-time evaluation through static initialization, such as
