.. _9899_I:

Annex I
-------

(informative)

Common warnings

.. _9899_Ip1:

:ref:`1 <9899_Ip1>` An implementation may generate warnings in many situations, none of which are specified as part of this International Standard. The following are a few of the more common situations.

.. _9899_Ip2:

:ref:`2 <9899_Ip2>`

-  A new struct or union type appears in a function prototype (:ref:`6.2.1 <9899_6.2.1>`, :ref:`6.7.2.3 <9899_6.7.2.3>`).
-  A block with initialization of an object that has automatic storage duration is jumped into (:ref:`6.2.4 <9899_6.2.4>`).
-  An implicit narrowing conversion is encountered, such as the assignment of a long int or a double to an int, or a pointer to void to a pointer to any type other than a character type (:ref:`6.3 <9899_6.3>`).
-  A hexadecimal floating constant cannot be represented exactly in its evaluation format (:ref:`6.4.4.2 <9899_6.4.4.2>`).
-  An integer character constant includes more than one character or a wide character constant includes more than one multibyte character (:ref:`6.4.4.4 <9899_6.4.4.4>`).
-  The characters /\* are found in a comment (:ref:`6.4.7 <9899_6.4.7>`).
-  An ''unordered'' binary operator (not comma, &&, or \|\|) contains a side effect to an lvalue in one operand, and a side effect to, or an access to the value of, the identical lvalue in the other operand (:ref:`6.5 <9899_6.5>`).
-  A function is called but no prototype has been supplied (:ref:`6.5.2.2 <9899_6.5.2.2>`).
-  The arguments in a function call do not agree in number and type with those of the parameters in a function definition that is not a prototype (:ref:`6.5.2.2 <9899_6.5.2.2>`).
-  An object is defined but not used (:ref:`6.7 <9899_6.7>`).
-  A value is given to an object of an enumerated type other than by assignment of an enumeration constant that is a member of that type, or an enumeration object that has the same type, or the value of a function that returns the same enumerated type (:ref:`6.7.2.2 <9899_6.7.2.2>`).
-  An aggregate has a partly bracketed initialization (:ref:`6.7.7 <9899_6.7.7>`).
-  A statement cannot be reached (:ref:`6.8 <9899_6.8>`).
-  A statement with no apparent effect is encountered (:ref:`6.8 <9899_6.8>`).
-  A constant expression is used as the controlling expression of a selection statement (:ref:`6.8.4 <9899_6.8.4>`).
-  An incorrectly formed preprocessing group is encountered while skipping a preprocessing group (:ref:`6.10.1 <9899_6.10.1>`).
-  An unrecognized #pragma directive is encountered (:ref:`6.10.6 <9899_6.10.6>`).

