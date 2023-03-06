.. _9899_introduction-2:

7.3.1 Introduction
^^^^^^^^^^^^^^^^^^

.. _9899_7.3.1p1:

.. container:: snum

   :ref:`1 <9899_7.3.1p1>`

The header :ref:`\<complex.h> <9899_7.3>` defines macros and declares functions that support complex arithmetic.\ [#9899_note166]_ Each synopsis specifies a family of functions consisting of a principal function with one or more double complex parameters and a double complex or double return value; and other functions with the same name but with f and l suffixes which are corresponding functions with float and long double parameters and return values.

.. _9899_7.3.1p2:

.. container:: snum

   :ref:`2 <9899_7.3.1p2>`

The macro

::

    complex

expands to \_Complex; the macro

::

    _Complex_I

expands to a constant expression of type const float \_Complex, with the value of the imaginary unit.\ [#9899_note167]_

.. _9899_7.3.1p3:

.. container:: snum

   :ref:`3 <9899_7.3.1p3>`

The macros

::

    imaginary

and

::

    _Imaginary_I

are defined if and only if the implementation supports imaginary types;\ [#9899_note168]_ if defined, they expand to \_Imaginary and a constant expression of type const float \_Imaginary with the value of the imaginary unit.

.. _9899_7.3.1p4:

.. container:: snum

   :ref:`4 <9899_7.3.1p4>`

The macro

::

    I

expands to either \_Imaginary_I or \_Complex_I. If \_Imaginary_I is not defined, I shall expand to \_Complex_I.

.. _9899_7.3.1p5:

.. container:: snum

   :ref:`5 <9899_7.3.1p5>`

Notwithstanding the provisions of :ref:`7.1.3 <9899_7.1.3>`, a program may undefine and perhaps then redefine the macros complex, imaginary, and I.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_G`







.. rubric:: Footnotes

.. [#9899_note166] See "future library directions" (:ref:`7.26.1 <9899_7.26.1>`).
.. [#9899_note167] The imaginary unit is a number i such that i\ :sup:`2` = -1.
.. [#9899_note168] A specification for imaginary types is in informative :ref:`annex G <9899_G>`.
