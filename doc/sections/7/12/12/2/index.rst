.. _9899_7.12.12.2:

7.12.12.2 The fmax functions
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.12.12.2p1:

:ref:`1 <9899_7.12.12.2p1>`

::

    #include <math.h>
    double fmax(double x, double y);
    float fmaxf(float x, float y);
    long double fmaxl(long double x, long double y);

.. rubric:: Description

.. _9899_7.12.12.2p2:

:ref:`2 <9899_7.12.12.2p2>` The fmax functions determine the maximum numeric value of their arguments.\ [#9899_note213]_

.. rubric:: Returns

.. _9899_7.12.12.2p3:

:ref:`3 <9899_7.12.12.2p3>` The fmax functions return the maximum numeric value of their arguments.





.. rubric:: Footnotes

.. [#9899_note213] NaN arguments are treated as missing data: if one argument is a NaN and the other numeric, then the fmax functions choose the numeric value. See :ref:`F.9.9.2 <9899_F.9.9.2>`.
