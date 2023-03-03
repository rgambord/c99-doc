.. _9899_5.1.2:

5.1.2 Execution environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index


.. _9899_5.1.2p1:

:ref:`1 <9899_5.1.2p1>` Two execution environments are defined: freestanding and hosted. In both cases, program startup occurs when a designated C function is called by the execution environment. All objects with static storage duration shall be initialized (set to their initial values) before program startup. The manner and timing of such initialization are otherwise unspecified. Program termination returns control to the execution environment.

**Forward references**: storage durations of objects (:ref:`6.2.4 <9899_6.2.4>`), initialization (:ref:`6.7.8 <9899_6.7.8>`).

