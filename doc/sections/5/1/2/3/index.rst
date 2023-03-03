.. _9899_program-execution-1:

5.1.2.3 Program execution
'''''''''''''''''''''''''

.. _9899_5.1.2.3p1:

:ref:`1 <9899_5.1.2.3p1>` The semantic descriptions in this International Standard describe the behavior of an abstract machine in which issues of optimization are irrelevant.

.. _9899_5.1.2.3p2:

:ref:`2 <9899_5.1.2.3p2>` Accessing a volatile object, modifying an object, modifying a file, or calling a function that does any of those operations are all side effects,\ [#9899_note11]_ which are changes in the state of the execution environment. Evaluation of an expression may produce side effects. At certain specified points in the execution sequence called sequence points, all side effects of previous evaluations shall be complete and no side effects of subsequent evaluations shall have taken place. (A summary of the sequence points is given in :ref:`annex C <9899_C>`.)

.. _9899_5.1.2.3p3:

:ref:`3 <9899_5.1.2.3p3>` In the abstract machine, all expressions are evaluated as specified by the semantics. An actual implementation need not evaluate part of an expression if it can deduce that its value is not used and that no needed side effects are produced (including any caused by calling a function or accessing a volatile object).

.. _9899_5.1.2.3p4:

:ref:`4 <9899_5.1.2.3p4>` When the processing of the abstract machine is interrupted by receipt of a signal, only the values of objects as of the previous sequence point may be relied on. Objects that may be modified between the previous sequence point and the next sequence point need not have received their correct values yet.

.. _9899_5.1.2.3p5:

:ref:`5 <9899_5.1.2.3p5>` The least requirements on a conforming implementation are:

-  At sequence points, volatile objects are stable in the sense that previous accesses are complete and subsequent accesses have not yet occurred.
-  At program termination, all data written into files shall be identical to the result that execution of the program according to the abstract semantics would have produced.
-  The input and output dynamics of interactive devices shall take place as specified in :ref:`7.19.3 <9899_7.19.3>`. The intent of these requirements is that unbuffered or line-buffered output appear as soon as possible, to ensure that prompting messages actually appear prior to a program waiting for input.

.. _9899_5.1.2.3p6:

:ref:`6 <9899_5.1.2.3p6>` What constitutes an interactive device is implementation-defined.

.. _9899_5.1.2.3p7:

:ref:`7 <9899_5.1.2.3p7>` More stringent correspondences between abstract and actual semantics may be defined by each implementation.

.. _9899_5.1.2.3p8:

:ref:`8 <9899_5.1.2.3p8>` EXAMPLE 1 An implementation might define a one-to-one correspondence between abstract and actual semantics: at every sequence point, the values of the actual objects would agree with those specified by the abstract semantics. The keyword volatile would then be redundant.

.. _9899_5.1.2.3p9:

:ref:`9 <9899_5.1.2.3p9>` Alternatively, an implementation might perform various optimizations within each translation unit, such that the actual semantics would agree with the abstract semantics only when making function calls across translation unit boundaries. In such an implementation, at the time of each function entry and function return where the calling function and the called function are in different translation units, the values of all externally linked objects and of all objects accessible via pointers therein would agree with the abstract semantics. Furthermore, at the time of each such function entry the values of the parameters of the called function and of all objects accessible via pointers therein would agree with the abstract semantics. In this type of implementation, objects referred to by interrupt service routines activated by the signal function would require explicit specification of volatile storage, as well as other implementation-defined restrictions.

.. _9899_5.1.2.3p10:

:ref:`10 <9899_5.1.2.3p10>` EXAMPLE 2 In executing the fragment

::

    char c1, c2;
    /* ... */
    c1 = c1 + c2;

the ''integer promotions'' require that the abstract machine promote the value of each variable to int size and then add the two ints and truncate the sum. Provided the addition of two chars can be done without overflow, or with overflow wrapping silently to produce the correct result, the actual execution need only produce the same result, possibly omitting the promotions.

.. _9899_5.1.2.3p11:

:ref:`11 <9899_5.1.2.3p11>` EXAMPLE 3 Similarly, in the fragment

::

    float f1, f2;
    double d;
    /* ... */
    f1 = f2 * d;

the multiplication may be executed using single-precision arithmetic if the implementation can ascertain that the result would be the same as if it were executed using double-precision arithmetic (for example, if d were replaced by the constant 2.0, which has type double).

.. _9899_5.1.2.3p12:

:ref:`12 <9899_5.1.2.3p12>` EXAMPLE 4 Implementations employing wide registers have to take care to honor appropriate semantics. Values are independent of whether they are represented in a register or in memory. For example, an implicit spilling of a register is not permitted to alter the value. Also, an explicit store and load is required to round to the precision of the storage type. In particular, casts and assignments are required to perform their specified conversion. For the fragment

::

    double d1, d2;
    float f;
    d1 = f = expression;
    d2 = (float) expression;

the values assigned to d1 and d2 are required to have been converted to float.

.. _9899_5.1.2.3p13:

:ref:`13 <9899_5.1.2.3p13>` EXAMPLE 5 Rearrangement for floating-point expressions is often restricted because of limitations in precision as well as range. The implementation cannot generally apply the mathematical associative rules for addition or multiplication, nor the distributive rule, because of roundoff error, even in the absence of overflow and underflow. Likewise, implementations cannot generally replace decimal constants in order to rearrange expressions. In the following fragment, rearrangements suggested by mathematical rules for real numbers are often not valid (see :ref:`F.8 <9899_F.8>`).

::

    double x, y, z;
    /* ... */
    x = (x * y) * z;            //   not equivalent to x   *= y * z;
    z = (x - y) + y ;           //   not equivalent to z   = x;
    z = x + x * y;              //   not equivalent to z   = x * (1.0 + y);
    y = x / 5.0;                //   not equivalent to y   = x * 0.2;

.. _9899_5.1.2.3p14:

:ref:`14 <9899_5.1.2.3p14>` EXAMPLE 6 To illustrate the grouping behavior of expressions, in the following fragment

::

    int a, b;
    /* ... */
    a = a + 32760 + b + 5;

the expression statement behaves exactly the same as

::

    a = (((a + 32760) + b) + 5);

due to the associativity and precedence of these operators. Thus, the result of the sum (a + 32760) is next added to b, and that result is then added to 5 which results in the value assigned to a. On a machine in which overflows produce an explicit trap and in which the range of values representable by an int is [-32768, +32767], the implementation cannot rewrite this expression as

::

    a = ((a + b) + 32765);

since if the values for a and b were, respectively, -32754 and -15, the sum a + b would produce a trap while the original expression would not; nor can the expression be rewritten either as

::

    a = ((a + 32765) + b);

or

::

    a = (a + (b + 32765));

since the values for a and b might have been, respectively, 4 and -8 or -17 and 12. However, on a machine in which overflow silently generates some value and where positive and negative overflows cancel, the above expression statement can be rewritten by the implementation in any of the above ways because the same result will occur.

.. _9899_5.1.2.3p15:

:ref:`15 <9899_5.1.2.3p15>` EXAMPLE 7 The grouping of an expression does not completely determine its evaluation. In the following fragment

::

    #include <stdio.h>
    int sum;
    char *p;
    /* ... */
    sum = sum * 10 - '0' + (*p++ = getchar());

the expression statement is grouped as if it were written as

::

    sum = (((sum * 10) - '0') + ((*(p++)) = (getchar())));

but the actual increment of p can occur at any time between the previous sequence point and the next sequence point (the ;), and the call to getchar can occur at any point prior to the need of its returned value.

**Forward references**: expressions (:ref:`6.5 <9899_6.5>`), type qualifiers (:ref:`6.7.3 <9899_6.7.3>`), statements (:ref:`6.8 <9899_6.8>`), the signal function (:ref:`7.14 <9899_7.14>`), files (:ref:`7.19.3 <9899_7.19.3>`).





.. rubric:: Footnotes

.. [#9899_note11] The IEC 60559 standard for binary floating-point arithmetic requires certain user-accessible status flags and control modes. Floating-point operations implicitly set the status flags; modes affect result values of floating-point operations. Implementations that support such floating-point state are required to regard changes to it as side effects -- see :ref:`annex F <9899_F>` for details. The floating-point environment library :ref:`\<fenv.h> <9899_7.6>` provides a programming facility for indicating when these side effects matter, freeing the implementations in other cases.
