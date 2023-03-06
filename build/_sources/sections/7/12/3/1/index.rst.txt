.. _9899_7.12.3.1:

7.12.3.1 The fpclassify macro
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.3.1p1:

.. container:: snum

   :ref:`1 <9899_7.12.3.1p1>`



::

    #include <math.h>
    int fpclassify(real-floating x);

.. rubric:: Description

.. _9899_7.12.3.1p2:

.. container:: snum

   :ref:`2 <9899_7.12.3.1p2>`

The fpclassify macro classifies its argument value as NaN, infinite, normal, subnormal, zero, or into another implementation-defined category. First, an argument represented in a format wider than its semantic type is converted to its semantic type. Then classification is based on the type of the argument.\ [#9899_note205]_

.. rubric:: Returns

.. _9899_7.12.3.1p3:

.. container:: snum

   :ref:`3 <9899_7.12.3.1p3>`

The fpclassify macro returns the value of the number classification macro appropriate to the value of its argument.

.. _9899_7.12.3.1p4:

.. container:: snum

   :ref:`4 <9899_7.12.3.1p4>`

EXAMPLE The fpclassify macro might be implemented in terms of ordinary functions as

::

    #define fpclassify(x) \
          ((sizeof (x) == sizeof (float)) ? __fpclassifyf(x) : \
           (sizeof (x) == sizeof (double)) ? __fpclassifyd(x) : \
                                             __fpclassifyl(x))





.. rubric:: Footnotes

.. [#9899_note205] Since an expression can be evaluated with more range and precision than its type has, it is important to know the type that classification is based on. For example, a normal long double value might become subnormal when converted to double, and zero when converted to float.
