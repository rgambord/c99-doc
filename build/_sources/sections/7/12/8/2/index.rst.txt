.. _9899_7.12.8.2:

7.12.8.2 The erfc functions
'''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.8.2p1:

.. container:: snum

   :ref:`1 <9899_7.12.8.2p1>`



::

    #include <math.h>
    double erfc(double x);
    float erfcf(float x);
    long double erfcl(long double x);

.. rubric:: Description

.. _9899_7.12.8.2p2:

.. container:: snum

   :ref:`2 <9899_7.12.8.2p2>`

The erfc functions compute the complementary error function of x. A range error occurs if x is too large.

.. rubric:: Returns

.. _9899_7.12.8.2p3:

.. container:: snum

   :ref:`3 <9899_7.12.8.2p3>`

The erfc functions return

::

    2       (inf)
    erfc x = 1 - erf x =     -----    (integral)  e-t2 dt .
                          (sqrt)(pi)    x 

