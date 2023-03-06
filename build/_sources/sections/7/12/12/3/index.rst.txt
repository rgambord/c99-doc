.. _9899_7.12.12.3:

7.12.12.3 The fmin functions
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.12.3p1:

.. container:: snum

   :ref:`1 <9899_7.12.12.3p1>`



::

    #include <math.h>
    double fmin(double x, double y);
    float fminf(float x, float y);
    long double fminl(long double x, long double y);

.. rubric:: Description

.. _9899_7.12.12.3p2:

.. container:: snum

   :ref:`2 <9899_7.12.12.3p2>`

The fmin functions determine the minimum numeric value of their arguments.\ [#9899_note214]_

.. rubric:: Returns

.. _9899_7.12.12.3p3:

.. container:: snum

   :ref:`3 <9899_7.12.12.3p3>`

The fmin functions return the minimum numeric value of their arguments.





.. rubric:: Footnotes

.. [#9899_note214] The fmin functions are analogous to the fmax functions in their treatment of NaNs.
