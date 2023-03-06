.. _9899_7.12.14.5:

7.12.14.5 The islessgreater macro
'''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.14.5p1:

.. container:: snum

   :ref:`1 <9899_7.12.14.5p1>`



::

    #include <math.h>
    int islessgreater(real-floating x, real-floating y);

.. rubric:: Description

.. _9899_7.12.14.5p2:

.. container:: snum

   :ref:`2 <9899_7.12.14.5p2>`

The islessgreater macro determines whether its first argument is less than or greater than its second argument. The islessgreater(x, y) macro is similar to (x) < (y) \|\| (x) > (y); however, islessgreater(x, y) does not raise the "invalid" floating-point exception when x and y are unordered (nor does it evaluate x and y twice).

.. rubric:: Returns

.. _9899_7.12.14.5p3:

.. container:: snum

   :ref:`3 <9899_7.12.14.5p3>`

The islessgreater macro returns the value of (x) < (y) \|\| (x) > (y).

