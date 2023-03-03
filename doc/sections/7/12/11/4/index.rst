.. _9899_7.12.11.4:

7.12.11.4 The nexttoward functions
''''''''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.11.4p1:

:ref:`1 <9899_7.12.11.4p1>`

::

    #include <math.h>
    double nexttoward(double x, long double y);
    float nexttowardf(float x, long double y);
    long double nexttowardl(long double x, long double y);

.. rubric:: Description

.. _9899_7.12.11.4p2:

:ref:`2 <9899_7.12.11.4p2>` The nexttoward functions are equivalent to the nextafter functions except that the second parameter has type long double and the functions return y converted to the type of the function if x equals y.\ [#9899_note212]_





.. rubric:: Footnotes

.. [#9899_note212] The result of the nexttoward functions is determined in the type of the function, without loss of range or precision in a floating second argument.
