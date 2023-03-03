.. _9899_H.2.4:

H.2.4 Type conversions
^^^^^^^^^^^^^^^^^^^^^^

.. _9899_H.2.4p1:

:ref:`1 <9899_H.2.4p1>` The LIA-1 type conversions are the following type casts:

.. code-block:: text

    cvtI' -> I      (int)i, (long int)i, (long long int)i,
                   (unsigned int)i, (unsigned long int)i,
                   (unsigned long long int)i
    cvtF -> I       (int)x, (long int)x, (long long int)x,
                   (unsigned int)x, (unsigned long int)x,
                   (unsigned long long int)x
    cvtI -> F       (float)i, (double)i, (long double)i
    cvtF' -> F      (float)x, (double)x, (long double)x

.. _9899_H.2.4p2:

:ref:`2 <9899_H.2.4p2>` In the above conversions from floating to integer, the use of (cast)x can be replaced with (cast)round(x), (cast)rint(x), (cast)nearbyint(x), (cast)trunc(x), (cast)ceil(x), or (cast)floor(x). In addition, C's floating-point to integer conversion functions, lrint(), llrint(), lround(), and llround(), can be used. They all meet LIA-1's requirements on floating to integer rounding for in-range values. For out-of-range values, the conversions shall silently wrap for the modulo types.

.. _9899_H.2.4p3:

:ref:`3 <9899_H.2.4p3>` The fmod() function is useful for doing silent wrapping to unsigned integer types, e.g., fmod( fabs(rint(x)), 65536.0 ) or (0.0 <= (y = fmod( rint(x), 65536.0 )) ? y : 65536.0 + y) will compute an integer value in the range 0.0 to 65535.0 which can then be cast to unsigned short int. But, the remainder() function is not useful for doing silent wrapping to signed integer types, e.g., remainder( rint(x), 65536.0 ) will compute an integer value in the range -32767.0 to +32768.0 which is not, in general, in the range of signed short int.

.. _9899_H.2.4p4:

:ref:`4 <9899_H.2.4p4>` C's conversions (casts) from floating-point to floating-point can meet LIA-1 requirements if an implementation uses round-to-nearest (IEC 60559 default).

.. _9899_H.2.4p5:

:ref:`5 <9899_H.2.4p5>` C's conversions (casts) from integer to floating-point can meet LIA-1 requirements if an implementation uses round-to-nearest.

