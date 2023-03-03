.. _9899_G.5.1:

G.5.1 Multiplicative operators
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Semantics

.. _9899_G.5.1p1:

:ref:`1 <9899_G.5.1p1>` If one operand has real type and the other operand has imaginary type, then the result has imaginary type. If both operands have imaginary type, then the result has real type. (If either operand has complex type, then the result has complex type.)

.. _9899_G.5.1p2:

:ref:`2 <9899_G.5.1p2>` If the operands are not both complex, then the result and floating-point exception behavior of the \* operator is defined by the usual mathematical formula:

.. code-block:: text

    *                  u                   iv                 u + iv

.. code-block:: text

    x                  xu                i(xv)            (xu) + i(xv)

.. code-block:: text

    iy               i(yu)                -yv            (-yv) + i(yu)

.. code-block:: text

    x + iy       (xu) + i(yu)        (-yv) + i(xv)

.. _9899_G.5.1p3:

:ref:`3 <9899_G.5.1p3>` If the second operand is not complex, then the result and floating-point exception behavior of the / operator is defined by the usual mathematical formula:

.. code-block:: text

    /                   u                       iv

.. code-block:: text

    x                  x/u                 i(-x/v)

.. code-block:: text

    iy               i(y/u)                     y/v

.. code-block:: text

    x + iy       (x/u) + i(y/u)        (y/v) + i(-x/v)

.. _9899_G.5.1p4:

:ref:`4 <9899_G.5.1p4>` The \* and / operators satisfy the following infinity properties for all real, imaginary, and complex operands:[#9899_note325]_

-  if one operand is an infinity and the other operand is a nonzero finite number or an infinity, then the result of the \* operator is an infinity;
-  if the first operand is an infinity and the second operand is a finite number, then the result of the / operator is an infinity;
-  if the first operand is a finite number and the second operand is an infinity, then the result of the / operator is a zero;
-  if the first operand is a nonzero finite number or an infinity and the second operand is a zero, then the result of the / operator is an infinity.

.. _9899_G.5.1p5:

:ref:`5 <9899_G.5.1p5>` If both operands of the \* operator are complex or if the second operand of the / operator is complex, the operator raises floating-point exceptions if appropriate for the calculation of the parts of the result, and may raise spurious floating-point exceptions.

.. _9899_G.5.1p6:

:ref:`6 <9899_G.5.1p6>` EXAMPLE 1 Multiplication of double \_Complex operands could be implemented as follows. Note that the imaginary unit I has imaginary type (see :ref:`G.6 <9899_G.6>`).

::

    #include <math.h>
    #include <complex.h>
    /* Multiply z * w ... */
    double complex _Cmultd(double complex z, double complex w)
    {
           #pragma STDC FP_CONTRACT OFF
           double a, b, c, d, ac, bd, ad, bc, x, y;
           a = creal(z); b = cimag(z);
           c = creal(w); d = cimag(w);
           ac = a * c;       bd = b * d;
           ad = a * d;       bc = b * c;
           x = ac - bd; y = ad + bc;
           if (isnan(x) && isnan(y)) {
                   /* Recover infinities that computed as NaN+iNaN ... */
                   int recalc = 0;
                   if ( isinf(a) || isinf(b) ) { // z is infinite
                           /* "Box" the infinity and change NaNs in the other factor to 0 */
                           a = copysign(isinf(a) ? 1.0 : 0.0, a);
                           b = copysign(isinf(b) ? 1.0 : 0.0, b);
                           if (isnan(c)) c = copysign(0.0, c);
                           if (isnan(d)) d = copysign(0.0, d);
                           recalc = 1;
                   }
                   if ( isinf(c) || isinf(d) ) { // w is infinite
                           /* "Box" the infinity and change NaNs in the other factor to 0 */
                           c = copysign(isinf(c) ? 1.0 : 0.0, c);
                           d = copysign(isinf(d) ? 1.0 : 0.0, d);
                           if (isnan(a)) a = copysign(0.0, a);
                           if (isnan(b)) b = copysign(0.0, b);
                           recalc = 1;
                   }
                   if (!recalc && (isinf(ac) || isinf(bd) ||
                                          isinf(ad) || isinf(bc))) {
                           /* Recover infinities from overflow by changing NaNs to 0 ... */
                           if (isnan(a)) a = copysign(0.0, a);
                           if (isnan(b)) b = copysign(0.0, b);
                           if (isnan(c)) c = copysign(0.0, c);
                           if (isnan(d)) d = copysign(0.0, d);
                           recalc = 1;
                   }
                   if (recalc) {
                               x = INFINITY * ( a * c - b * d );
                               y = INFINITY * ( a * d + b * c );
                    }
              }
              return x + I * y;
      }

.. _9899_G.5.1p7:

:ref:`7 <9899_G.5.1p7>` This implementation achieves the required treatment of infinities at the cost of only one isnan test in ordinary (finite) cases. It is less than ideal in that undue overflow and underflow may occur.

.. _9899_G.5.1p8:

:ref:`8 <9899_G.5.1p8>` EXAMPLE 2 Division of two double \_Complex operands could be implemented as follows.

::

    #include <math.h>
    #include <complex.h>
    /* Divide z / w ... */
    double complex _Cdivd(double complex z, double complex w)
    {
           #pragma STDC FP_CONTRACT OFF
           double a, b, c, d, logbw, denom, x, y;
           int ilogbw = 0;
           a = creal(z); b = cimag(z);
           c = creal(w); d = cimag(w);
           logbw = logb(fmax(fabs(c), fabs(d)));
           if (isfinite(logbw)) {
                  ilogbw = (int)logbw;
                  c = scalbn(c, -ilogbw); d = scalbn(d, -ilogbw);
           }
           denom = c * c + d * d;
           x = scalbn((a * c + b * d) / denom, -ilogbw);
           y = scalbn((b * c - a * d) / denom, -ilogbw);
           /* Recover infinities and zeros that computed as NaN+iNaN;                 */
           /* the only cases are nonzero/zero, infinite/finite, and finite/infinite, ... */
           if (isnan(x) && isnan(y)) {
                 if ((denom == 0.0) &&
                       (!isnan(a) || !isnan(b))) {
                       x = copysign(INFINITY, c) * a;
                       y = copysign(INFINITY, c) * b;
                 }
                 else if ((isinf(a) || isinf(b)) &&
                       isfinite(c) && isfinite(d)) {
                       a = copysign(isinf(a) ? 1.0 : 0.0,                        a);
                       b = copysign(isinf(b) ? 1.0 : 0.0,                        b);
                       x = INFINITY * ( a * c + b * d );
                       y = INFINITY * ( b * c - a * d );
                 }
                 else if (isinf(logbw) &&
                       isfinite(a) && isfinite(b)) {
                       c = copysign(isinf(c) ? 1.0 : 0.0,                        c);
                       d = copysign(isinf(d) ? 1.0 : 0.0,                        d);
                       x = 0.0 * ( a * c + b * d );
                       y = 0.0 * ( b * c - a * d );
                 }
           }
           return x + I * y;
            }

.. _9899_G.5.1p9:

:ref:`9 <9899_G.5.1p9>` Scaling the denominator alleviates the main overflow and underflow problem, which is more serious than for multiplication. In the spirit of the multiplication example above, this code does not defend against overflow and underflow in the calculation of the numerator. Scaling with the scalbn function, instead of with division, provides better roundoff characteristics.





.. rubric:: Footnotes

.. [#9899_note325] These properties are already implied for those cases covered in the tables, but are required for all cases (at least where the state for CX_LIMITED_RANGE is ''off'').
