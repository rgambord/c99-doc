.. _9899_7.12.6.7:

7.12.6.7 The log functions
''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.6.7p1:

:ref:`1 <9899_7.12.6.7p1>`

::

    #include <math.h>
    double log(double x);
    float logf(float x);
    long double logl(long double x);

.. rubric:: Description

.. _9899_7.12.6.7p2:

:ref:`2 <9899_7.12.6.7p2>` The log functions compute the base-e (natural) logarithm of x. A domain error occurs if the argument is negative. A range error may occur if the argument is zero.

.. rubric:: Returns

.. _9899_7.12.6.7p3:

:ref:`3 <9899_7.12.6.7p3>` The log functions return loge x.

