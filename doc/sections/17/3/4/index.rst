.. _9899_J.3.4:

J.3.4 Characters
^^^^^^^^^^^^^^^^

.. _9899_J.3.4p1:

:ref:`1 <9899_J.3.4p1>`

-  The number of bits in a byte (:ref:`3.6 <9899_3.6>`).
-  The values of the members of the execution character set (:ref:`5.2.1 <9899_5.2.1>`).
-  The unique value of the member of the execution character set produced for each of the standard alphabetic escape sequences (:ref:`5.2.2 <9899_5.2.2>`).
-  The value of a char object into which has been stored any character other than a member of the basic execution character set (:ref:`6.2.5 <9899_6.2.5>`).
-  Which of signed char or unsigned char has the same range, representation, and behavior as ''plain'' char (:ref:`6.2.5 <9899_6.2.5>`, :ref:`6.3.1.1 <9899_6.3.1.1>`).
-  The mapping of members of the source character set (in character constants and string literals) to members of the execution character set (:ref:`6.4.4.4 <9899_6.4.4.4>`, :ref:`5.1.1.2 <9899_5.1.1.2>`).
-  The value of an integer character constant containing more than one character or containing a character or escape sequence that does not map to a single-byte execution character (:ref:`6.4.4.4 <9899_6.4.4.4>`).
-  The value of a wide character constant containing more than one multibyte character, or containing a multibyte character or escape sequence not represented in the extended execution character set (:ref:`6.4.4.4 <9899_6.4.4.4>`).
-  The current locale used to convert a wide character constant consisting of a single multibyte character that maps to a member of the extended execution character set into a corresponding wide character code (:ref:`6.4.4.4 <9899_6.4.4.4>`).
-  The current locale used to convert a wide string literal into corresponding wide character codes (:ref:`6.4.5 <9899_6.4.5>`).
-  The value of a string literal containing a multibyte character or escape sequence not represented in the execution character set (:ref:`6.4.5 <9899_6.4.5>`).

