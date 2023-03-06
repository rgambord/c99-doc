.. _9899_H.2.3.2:

H.2.3.2 Floating-point operations
'''''''''''''''''''''''''''''''''

.. _9899_H.2.3.2p1:

.. container:: snum

   :ref:`1 <9899_H.2.3.2p1>`

The floating-point operations on floating-point types are the following:

.. code-block:: text

    addF          x + y
    subF          x - y
    mulF          x * y
    divF          x / y
    negF          -x
    absF          fabsf(x), fabs(x), fabsl(x)
    exponentF     1.f+logbf(x), 1.0+logb(x), 1.L+logbl(x)
    scaleF        scalbnf(x, n), scalbn(x, n), scalbnl(x, n),
                  scalblnf(x, li), scalbln(x, li), scalblnl(x, li)
    intpartF      modff(x, &y), modf(x, &y), modfl(x, &y)
    fractpartF    modff(x, &y), modf(x, &y), modfl(x, &y)
    eqF           x == y
    neqF          x != y
    lssF          x < y
    leqF          x <= y
    gtrF          x > y
    geqF          x >= y

where x and y are expressions of the same floating point type, n is of type int, and li is of type long int.

