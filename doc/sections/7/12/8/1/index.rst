.. _9899_7.12.8.1:

7.12.8.1 The erf functions
''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.8.1p1:

.. container:: snum

   :ref:`1 <9899_7.12.8.1p1>`



::

    #include <math.h>
    double erf(double x);
    float erff(float x);
    long double erfl(long double x);

.. rubric:: Description

.. _9899_7.12.8.1p2:

.. container:: snum

   :ref:`2 <9899_7.12.8.1p2>`

The erf functions compute the error function of x.

.. rubric:: Returns

.. _9899_7.12.8.1p3:

.. container:: snum

   :ref:`3 <9899_7.12.8.1p3>`

The erf functions return

::

    2        x
    erf x =     -----    (integral)  e-t2 dt .
             (sqrt)(pi)   0 

