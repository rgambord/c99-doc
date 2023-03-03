.. _9899_7.21.1:

7.21.1 String function conventions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_7.21.1p1:

:ref:`1 <9899_7.21.1p1>` The header :ref:`\<string.h> <9899_7.21>` declares one type and several functions, and defines one macro useful for manipulating arrays of character type and other objects treated as arrays of character type.\ [#9899_note268]_ The type is size_t and the macro is NULL (both described in :ref:`7.17 <9899_7.17>`). Various methods are used for determining the lengths of the arrays, but in all cases a char \* or void \* argument points to the initial (lowest addressed) character of the array. If an array is accessed beyond the end of an object, the behavior is undefined.

.. _9899_7.21.1p2:

:ref:`2 <9899_7.21.1p2>` Where an argument declared as size_t n specifies the length of the array for a function, n can have the value zero on a call to that function. Unless explicitly stated otherwise in the description of a particular function in this subclause, pointer arguments on such a call shall still have valid values, as described in :ref:`7.1.4 <9899_7.1.4>`. On such a call, a function that locates a character finds no occurrence, a function that compares two character sequences returns zero, and a function that copies characters copies zero characters.

.. _9899_7.21.1p3:

:ref:`3 <9899_7.21.1p3>` For all functions in this subclause, each character shall be interpreted as if it had the type unsigned char (and therefore every possible object representation is valid and has a different value).





.. rubric:: Footnotes

.. [#9899_note268] See ''future library directions'' (:ref:`7.26.11 <9899_7.26.11>`).
