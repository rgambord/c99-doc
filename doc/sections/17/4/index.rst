.. _9899_J.4:

J.4 Locale-specific behavior
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _9899_J.4p1:

:ref:`1 <9899_J.4p1>` The following characteristics of a hosted environment are locale-specific and are required to be documented by the implementation:

-  Additional members of the source and execution character sets beyond the basic character set (:ref:`5.2.1 <9899_5.2.1>`).
-  The presence, meaning, and representation of additional multibyte characters in the execution character set beyond the basic character set (:ref:`5.2.1.2 <9899_5.2.1.2>`).
-  The shift states used for the encoding of multibyte characters (:ref:`5.2.1.2 <9899_5.2.1.2>`).
-  The direction of writing of successive printing characters (:ref:`5.2.2 <9899_5.2.2>`).
-  The decimal-point character (:ref:`7.1.1 <9899_7.1.1>`).
-  The set of printing characters (:ref:`7.4 <9899_7.4>`, :ref:`7.25.2 <9899_7.25.2>`).
-  The set of control characters (:ref:`7.4 <9899_7.4>`, :ref:`7.25.2 <9899_7.25.2>`).
-  The sets of characters tested for by the isalpha, isblank, islower, ispunct, isspace, isupper, iswalpha, iswblank, iswlower, iswpunct, iswspace, or iswupper functions (:ref:`7.4.1.2 <9899_7.4.1.2>`, :ref:`7.4.1.3 <9899_7.4.1.3>`, :ref:`7.4.1.7 <9899_7.4.1.7>`, :ref:`7.4.1.9 <9899_7.4.1.9>`, :ref:`7.4.1.10 <9899_7.4.1.10>`, :ref:`7.4.1.11 <9899_7.4.1.11>`, :ref:`7.25.2.1.2 <9899_7.25.2.1.2>`, :ref:`7.25.2.1.3 <9899_7.25.2.1.3>`, :ref:`7.25.2.1.7 <9899_7.25.2.1.7>`, :ref:`7.25.2.1.9 <9899_7.25.2.1.9>`, :ref:`7.25.2.1.10 <9899_7.25.2.1.10>`, :ref:`7.25.2.1.11 <9899_7.25.2.1.11>`).
-  The native environment (:ref:`7.11.1.1 <9899_7.11.1.1>`).
-  Additional subject sequences accepted by the numeric conversion functions (:ref:`7.20.1 <9899_7.20.1>`, :ref:`7.24.4.1 <9899_7.24.4.1>`).
-  The collation sequence of the execution character set (:ref:`7.21.4.3 <9899_7.21.4.3>`, :ref:`7.24.4.4.2 <9899_7.24.4.4.2>`).
-  The contents of the error message strings set up by the strerror function (:ref:`7.21.6.2 <9899_7.21.6.2>`).
-  The formats for time and date (:ref:`7.23.3.5 <9899_7.23.3.5>`, :ref:`7.24.5.1 <9899_7.24.5.1>`).
-  Character mappings that are supported by the towctrans function (:ref:`7.25.1 <9899_7.25.1>`).
-  Character classifications that are supported by the iswctype function (:ref:`7.25.1 <9899_7.25.1>`).

