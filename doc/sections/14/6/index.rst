.. _9899_G.6:

G.6 Complex arithmetic \<complex.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index
   4/index


.. _9899_G.6p1:

:ref:`1 <9899_G.6p1>` The macros

::

    imaginary

and

::

    _Imaginary_I

are defined, respectively, as \_Imaginary and a constant expression of type const float \_Imaginary with the value of the imaginary unit. The macro

::

    I

is defined to be \_Imaginary_I (not \_Complex_I as stated in :ref:`7.3 <9899_7.3>`). Notwithstanding the provisions of :ref:`7.1.3 <9899_7.1.3>`, a program may undefine and then perhaps redefine the macro imaginary.

.. _9899_G.6p2:

:ref:`2 <9899_G.6p2>` This subclause contains specifications for the :ref:`\<complex.h> <9899_7.3>` functions that are particularly suited to IEC 60559 implementations. For families of functions, the specifications apply to all of the functions even though only the principal function is shown. Unless otherwise specified, where the symbol ''(+-)'' occurs in both an argument and the result, the result has the same sign as the argument.

.. _9899_G.6p3:

:ref:`3 <9899_G.6p3>` The functions are continuous onto both sides of their branch cuts, taking into account the sign of zero. For example, csqrt(-2 (+-) i0) = (+-)i(sqrt)(2).

.. _9899_G.6p4:

:ref:`4 <9899_G.6p4>` Since complex and imaginary values are composed of real values, each function may be regarded as computing real values from real values. Except as noted, the functions treat real infinities, NaNs, signed zeros, subnormals, and the floating-point exception flags in a manner consistent with the specifications for real functions in F.9.\ [#9899_note326]_

.. _9899_G.6p5:

:ref:`5 <9899_G.6p5>` The functions cimag, conj, cproj, and creal are fully specified for all implementations, including IEC 60559 ones, in :ref:`7.3.9 <9899_7.3.9>`. These functions raise no floating- point exceptions.

.. _9899_G.6p6:

:ref:`6 <9899_G.6p6>` Each of the functions cabs and carg is specified by a formula in terms of a real function (whose special cases are covered in :ref:`annex F <9899_F>`):

::

    cabs(x + iy) = hypot(x, y)
    carg(x + iy) = atan2(y, x)

.. _9899_G.6p7:

:ref:`7 <9899_G.6p7>` Each of the functions casin, catan, ccos, csin, and ctan is specified implicitly by a formula in terms of other complex functions (whose special cases are specified below):

::

    casin(z)        =   -i casinh(iz)
    catan(z)        =   -i catanh(iz)
    ccos(z)         =   ccosh(iz)
    csin(z)         =   -i csinh(iz)
    ctan(z)         =   -i ctanh(iz)

.. _9899_G.6p8:

:ref:`8 <9899_G.6p8>` For the other functions, the following subclauses specify behavior for special cases, including treatment of the ''invalid'' and ''divide-by-zero'' floating-point exceptions. For families of functions, the specifications apply to all of the functions even though only the principal function is shown. For a function f satisfying f (conj(z)) = conj( f (z)), the specifications for the upper half-plane imply the specifications for the lower half-plane; if the function f is also either even, f (-z) = f (z), or odd, f (-z) = - f (z), then the specifications for the first quadrant imply the specifications for the other three quadrants.

.. _9899_G.6p9:

:ref:`9 <9899_G.6p9>` In the following subclauses, cis(y) is defined as cos(y) + i sin(y).





.. rubric:: Footnotes

.. [#9899_note326] As noted in :ref:`G.3 <9899_G.3>`, a complex value with at least one infinite part is regarded as an infinity even if its other part is a NaN.
