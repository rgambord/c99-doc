.. _9899_F.8.3:

F.8.3 Relational operators
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_F.8.3p1:

.. container:: snum

   :ref:`1 <9899_F.8.3p1>`



.. code-block:: text

    x != x -> false          

The statement x != x is true if x is a NaN.

.. code-block:: text

    x == x -> true           

The statement x == x is false if x is a NaN.

.. code-block:: text

    x < y -> isless(x,y)  

(and similarly for <=, >, >=) Though numerically equal, these expressions are not equivalent because of side effects when x or y is a NaN and the state of the FENV_ACCESS pragma is "on". This transformation, which would be desirable if extra code were required to cause the "invalid" floating-point exception for unordered cases, could be performed provided the state of the FENV_ACCESS pragma is "off".

The sense of relational operators shall be maintained. This includes handling unordered cases as expressed by the source code.

.. _9899_F.8.3p2:

.. container:: snum

   :ref:`2 <9899_F.8.3p2>`

EXAMPLE

::

    // calls g and raises "invalid" if a and b are unordered
    if (a < b)
            f();
    else
            g();

is not equivalent to

::

    // calls f and raises "invalid" if a and b are unordered
    if (a >= b)
            g();
    else
            f();

nor to

::

    // calls f without raising "invalid" if a and b are unordered
    if (isgreaterequal(a,b))
            g();
    else
            f();

nor, unless the state of the FENV_ACCESS pragma is "off", to

::

    // calls g without raising "invalid" if a and b are unordered
    if (isless(a,b))
            f();
    else
            g();

but is equivalent to

::

    if (!(a < b))
          g();
    else
          f();

