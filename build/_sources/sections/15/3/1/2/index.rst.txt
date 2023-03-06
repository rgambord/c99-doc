.. _9899_H.3.1.2:

H.3.1.2 Traps
'''''''''''''

.. _9899_H.3.1.2p1:

.. container:: snum

   :ref:`1 <9899_H.3.1.2p1>`

C is compatible with LIA-1's trap requirements for arithmetic operations, but not for math library functions (which are not permitted to generate any externally visible exceptional conditions). An implementation can provide an alternative of notification through termination with a "hard-to-ignore" message (see LIA-1 subclause 6.1.3).

.. _9899_H.3.1.2p2:

.. container:: snum

   :ref:`2 <9899_H.3.1.2p2>`

LIA-1 does not require that traps be precise.

.. _9899_H.3.1.2p3:

.. container:: snum

   :ref:`3 <9899_H.3.1.2p3>`

C does require that SIGFPE be the signal corresponding to arithmetic exceptions, if there is any signal raised for them.

.. _9899_H.3.1.2p4:

.. container:: snum

   :ref:`4 <9899_H.3.1.2p4>`

C supports signal handlers for SIGFPE and allows trapping of arithmetic exceptions. When arithmetic exceptions do trap, C's signal-handler mechanism allows trap-and- terminate (either default implementation behavior or user replacement for it) or trap-and- resume, at the programmer's option.

