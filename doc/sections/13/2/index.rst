.. _9899_F.2:

F.2 Types
~~~~~~~~~


.. toctree::
   :maxdepth: 2

   1/index


.. _9899_F.2p1:

.. container:: snum

   :ref:`1 <9899_F.2p1>`

The C floating types match the IEC 60559 formats as follows:

-  The float type matches the IEC 60559 single format.
-  The double type matches the IEC 60559 double format.
-  The long double type matches an IEC 60559 extended format,\ [#9899_note307]_ else a non-IEC 60559 extended format, else the IEC 60559 double format.

Any non-IEC 60559 extended format used for the long double type shall have more precision than IEC 60559 double and at least the range of IEC 60559 double.\ [#9899_note308]_

.. rubric:: Recommended practice

.. _9899_F.2p2:

.. container:: snum

   :ref:`2 <9899_F.2p2>`

The long double type should match an IEC 60559 extended format.






.. rubric:: Footnotes

.. [#9899_note307] "Extended" is IEC 60559's double-extended data format. Extended refers to both the common 80-bit and quadruple 128-bit IEC 60559 formats.
.. [#9899_note308] A non-IEC 60559 long double type is required to provide infinity and NaNs, as its values include all double values.
