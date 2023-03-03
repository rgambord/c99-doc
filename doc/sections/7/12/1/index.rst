.. _9899_7.12.1:

7.12.1 Treatment of error conditions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_7.12.1p1:

:ref:`1 <9899_7.12.1p1>` The behavior of each of the functions in :ref:`\<math.h> <9899_7.12>` is specified for all representable values of its input arguments, except where stated otherwise. Each function shall execute as if it were a single operation without generating any externally visible exceptional conditions.

.. _9899_7.12.1p2:

:ref:`2 <9899_7.12.1p2>` For all functions, a domain error occurs if an input argument is outside the domain over which the mathematical function is defined. The description of each function lists any required domain errors; an implementation may define additional domain errors, provided that such errors are consistent with the mathematical definition of the function.\ [#9899_note203]_ On a domain error, the function returns an implementation-defined value; if the integer expression math_errhandling & MATH_ERRNO is nonzero, the integer expression errno acquires the value EDOM; if the integer expression math_errhandling & MATH_ERREXCEPT is nonzero, the ''invalid'' floating-point exception is raised.

.. _9899_7.12.1p3:

:ref:`3 <9899_7.12.1p3>` Similarly, a range error occurs if the mathematical result of the function cannot be represented in an object of the specified type, due to extreme magnitude.

.. _9899_7.12.1p4:

:ref:`4 <9899_7.12.1p4>` A floating result overflows if the magnitude of the mathematical result is finite but so large that the mathematical result cannot be represented without extraordinary roundoff error in an object of the specified type. If a floating result overflows and default rounding is in effect, or if the mathematical result is an exact infinity from finite arguments (for example log(0.0)), then the function returns the value of the macro HUGE_VAL, HUGE_VALF, or HUGE_VALL according to the return type, with the same sign as the correct value of the function; if the integer expression math_errhandling & MATH_ERRNO is nonzero, the integer expression errno acquires the value ERANGE; if the integer expression math_errhandling & MATH_ERREXCEPT is nonzero, the ''divide-by-zero'' floating-point exception is raised if the mathematical result is an exact infinity and the ''overflow'' floating-point exception is raised otherwise.

.. _9899_7.12.1p5:

:ref:`5 <9899_7.12.1p5>` The result underflows if the magnitude of the mathematical result is so small that the mathematical result cannot be represented, without extraordinary roundoff error, in an object of the specified type.\ [#9899_note204]_ If the result underflows, the function returns an implementation-defined value whose magnitude is no greater than the smallest normalized positive number in the specified type; if the integer expression math_errhandling & MATH_ERRNO is nonzero, whether errno acquires the value ERANGE is implementation-defined; if the integer expression math_errhandling & MATH_ERREXCEPT is nonzero, whether the ''underflow'' floating-point exception is raised is implementation-defined.






.. rubric:: Footnotes

.. [#9899_note203] In an implementation that supports infinities, this allows an infinity as an argument to be a domain error if the mathematical domain of the function does not include the infinity.
.. [#9899_note204] The term underflow here is intended to encompass both ''gradual underflow'' as in IEC 60559 and also ''flush-to-zero'' underflow.
