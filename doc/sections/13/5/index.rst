.. _9899_F.5:

F.5 Binary-decimal conversion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _9899_F.5p1:

:ref:`1 <9899_F.5p1>` Conversion from the widest supported IEC 60559 format to decimal with DECIMAL_DIG digits and back is the identity function.\ [#9899_note311]_

.. _9899_F.5p2:

:ref:`2 <9899_F.5p2>` Conversions involving IEC 60559 formats follow all pertinent recommended practice. In particular, conversion between any supported IEC 60559 format and decimal with DECIMAL_DIG or fewer significant digits is correctly rounded (honoring the current rounding mode), which assures that conversion from the widest supported IEC 60559 format to decimal with DECIMAL_DIG digits and back is the identity function.

.. _9899_F.5p3:

:ref:`3 <9899_F.5p3>` Functions such as strtod that convert character sequences to floating types honor the rounding direction. Hence, if the rounding direction might be upward or downward, the implementation cannot convert a minus-signed sequence by negating the converted unsigned sequence.





.. rubric:: Footnotes

.. [#9899_note311] If the minimum-width IEC 60559 extended format (64 bits of precision) is supported, DECIMAL_DIG shall be at least 21. If IEC 60559 double (53 bits of precision) is the widest IEC 60559 format supported, then DECIMAL_DIG shall be at least 17. (By contrast, LDBL_DIG and DBL_DIG are 18 and 15, respectively, for these formats.)
