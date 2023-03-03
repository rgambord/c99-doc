.. _9899_7.6.3.2:

7.6.3.2 The fesetround function
'''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.6.3.2p1:

:ref:`1 <9899_7.6.3.2p1>`

::

    #include <fenv.h>
    int fesetround(int round);

.. rubric:: Description

.. _9899_7.6.3.2p2:

:ref:`2 <9899_7.6.3.2p2>` The fesetround function establishes the rounding direction represented by its argument round. If the argument is not equal to the value of a rounding direction macro, the rounding direction is not changed.

.. rubric:: Returns

.. _9899_7.6.3.2p3:

:ref:`3 <9899_7.6.3.2p3>` The fesetround function returns zero if and only if the requested rounding direction was established.

.. _9899_7.6.3.2p4:

:ref:`4 <9899_7.6.3.2p4>` EXAMPLE Save, set, and restore the rounding direction. Report an error and abort if setting the rounding direction fails.

::

    #include <fenv.h>
    #include <assert.h>
    void f(int round_dir)
    {
          #pragma STDC FENV_ACCESS ON
          int save_round;
          int setround_ok;
          save_round = fegetround();
          setround_ok = fesetround(round_dir);
          assert(setround_ok == 0);
          /* ... */
          fesetround(save_round);
          /* ... */
    }

.. _9899_7.6.4:

