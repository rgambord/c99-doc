.. _9899_5.2.3:

5.2.3 Signals and interrupts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_5.2.3p1:

:ref:`1 <9899_5.2.3p1>` Functions shall be implemented such that they may be interrupted at any time by a signal, or may be called by a signal handler, or both, with no alteration to earlier, but still active, invocations' control flow (after the interruption), function return values, or objects with automatic storage duration. All such objects shall be maintained outside the function image (the instructions that compose the executable representation of a function) on a per-invocation basis.

