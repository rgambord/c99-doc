.. _9899_6.3.2.3:

6.3.2.3 Pointers
''''''''''''''''

.. _9899_6.3.2.3p1:

.. container:: snum

   :ref:`1 <9899_6.3.2.3p1>`

A pointer to void may be converted to or from a pointer to any incomplete or object type. A pointer to any incomplete or object type may be converted to a pointer to void and back again; the result shall compare equal to the original pointer.

.. _9899_6.3.2.3p2:

.. container:: snum

   :ref:`2 <9899_6.3.2.3p2>`

For any qualifier q, a pointer to a non-q-qualified type may be converted to a pointer to the q-qualified version of the type; the values stored in the original and converted pointers shall compare equal.

.. _9899_6.3.2.3p3:

.. container:: snum

   :ref:`3 <9899_6.3.2.3p3>`

An integer constant expression with the value 0, or such an expression cast to type void \*, is called a null pointer constant.\ [#9899_note55]_ If a null pointer constant is converted to a pointer type, the resulting pointer, called a null pointer, is guaranteed to compare unequal to a pointer to any object or function.

.. _9899_6.3.2.3p4:

.. container:: snum

   :ref:`4 <9899_6.3.2.3p4>`

Conversion of a null pointer to another pointer type yields a null pointer of that type. Any two null pointers shall compare equal.

.. _9899_6.3.2.3p5:

.. container:: snum

   :ref:`5 <9899_6.3.2.3p5>`

An integer may be converted to any pointer type. Except as previously specified, the result is implementation-defined, might not be correctly aligned, might not point to an entity of the referenced type, and might be a trap representation.\ [#9899_note56]_

.. _9899_6.3.2.3p6:

.. container:: snum

   :ref:`6 <9899_6.3.2.3p6>`

Any pointer type may be converted to an integer type. Except as previously specified, the result is implementation-defined. If the result cannot be represented in the integer type, the behavior is undefined. The result need not be in the range of values of any integer type.

.. _9899_6.3.2.3p7:

.. container:: snum

   :ref:`7 <9899_6.3.2.3p7>`

A pointer to an object or incomplete type may be converted to a pointer to a different object or incomplete type. If the resulting pointer is not correctly aligned\ [#9899_note57]_ for the pointed-to type, the behavior is undefined. Otherwise, when converted back again, the result shall compare equal to the original pointer. When a pointer to an object is converted to a pointer to a character type, the result points to the lowest addressed byte of the object. Successive increments of the result, up to the size of the object, yield pointers to the remaining bytes of the object.

.. _9899_6.3.2.3p8:

.. container:: snum

   :ref:`8 <9899_6.3.2.3p8>`

A pointer to a function of one type may be converted to a pointer to a function of another type and back again; the result shall compare equal to the original pointer. If a converted pointer is used to call a function whose type is not compatible with the pointed-to type, the behavior is undefined.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.5.4`
   - :ref:`9899_6.5.9`
   - :ref:`9899_7.18.1.4`
   - :ref:`9899_6.5.16.1`







.. rubric:: Footnotes

.. [#9899_note55] The macro NULL is defined in :ref:`\<stddef.h> <9899_7.17>` (and other headers) as a null pointer constant; see :ref:`7.17 <9899_7.17>`.
.. [#9899_note56] The mapping functions for converting a pointer to an integer or an integer to a pointer are intended to be consistent with the addressing structure of the execution environment.
.. [#9899_note57] In general, the concept "correctly aligned" is transitive: if a pointer to type A is correctly aligned for a pointer to type B, which in turn is correctly aligned for a pointer to type C, then a pointer to type A is correctly aligned for a pointer to type C.
