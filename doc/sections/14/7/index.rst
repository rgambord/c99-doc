.. _9899_G.7:

G.7 Type-generic math \<tgmath.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _9899_G.7p1:

.. container:: snum

   :ref:`1 <9899_G.7p1>`

Type-generic macros that accept complex arguments also accept imaginary arguments. If an argument is imaginary, the macro expands to an expression whose type is real, imaginary, or complex, as appropriate for the particular function: if the argument is imaginary, then the types of cos, cosh, fabs, carg, cimag, and creal are real; the types of sin, tan, sinh, tanh, asin, atan, asinh, and atanh are imaginary; and the types of the others are complex.

.. _9899_G.7p2:

.. container:: snum

   :ref:`2 <9899_G.7p2>`

Given an imaginary argument, each of the type-generic macros cos, sin, tan, cosh, sinh, tanh, asin, atan, asinh, atanh is specified by a formula in terms of real functions:

::

    cos(iy)      =   cosh(y)
    sin(iy)      =   i sinh(y)
    tan(iy)      =   i tanh(y)
    cosh(iy)     =   cos(y)
    sinh(iy)     =   i sin(y)
    tanh(iy)     =   i tan(y)
    asin(iy)     =   i asinh(y)
    atan(iy)     =   i atanh(y)
    asinh(iy)    =   i asin(y)
    atanh(iy)    =   i atan(y)

