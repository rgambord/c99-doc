.. _9899_F.9.3.4:

F.9.3.4 The frexp functions
'''''''''''''''''''''''''''

.. _9899_F.9.3.4p1:

:ref:`1 <9899_F.9.3.4p1>`

-  frexp((+-)0, exp) returns (+-)0, and stores 0 in the object pointed to by exp.
-  frexp((+-)(inf), exp) returns (+-)(inf), and stores an unspecified value in the object pointed to by exp.
-  frexp(NaN, exp) stores an unspecified value in the object pointed to by exp (and returns a NaN).

.. _9899_F.9.3.4p2:

:ref:`2 <9899_F.9.3.4p2>` frexp raises no floating-point exceptions.

.. _9899_F.9.3.4p3:

:ref:`3 <9899_F.9.3.4p3>` On a binary system, the body of the frexp function might be

::

    {
           *exp = (value == 0) ? 0 : (int)(1 + logb(value));
           return scalbn(value, -(*exp));
    }

