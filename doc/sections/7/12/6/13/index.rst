.. _9899_7.12.6.13:

7.12.6.13 The scalbn and scalbln functions
''''''''''''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.6.13p1:

:ref:`1 <9899_7.12.6.13p1>`

::

    #include <math.h>
    double scalbn(double x, int n);
    float scalbnf(float x, int n);
    long double scalbnl(long double x, int n);
    double scalbln(double x, long int n);
    float scalblnf(float x, long int n);
    long double scalblnl(long double x, long int n);

.. rubric:: Description

.. _9899_7.12.6.13p2:

:ref:`2 <9899_7.12.6.13p2>` The scalbn and scalbln functions compute x FLT_RADIX\ :sup:`n` efficiently, not normally by computing FLT_RADIX\ :sup:`n` explicitly. A range error may occur.

.. rubric:: Returns

.. _9899_7.12.6.13p3:

:ref:`3 <9899_7.12.6.13p3>` The scalbn and scalbln functions return x FLT_RADIX\ :sup:`n` .

.. _9899_7.12.7:

