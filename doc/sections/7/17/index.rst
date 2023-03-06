.. _9899_7.17:

7.17 Common definitions \<stddef.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _9899_7.17p1:

.. container:: snum

   :ref:`1 <9899_7.17p1>`

The following types and macros are defined in the standard header :ref:`\<stddef.h> <9899_7.17>`. Some are also defined in other headers, as noted in their respective subclauses.

.. _9899_7.17p2:

.. container:: snum

   :ref:`2 <9899_7.17p2>`

The types are

::

    ptrdiff_t

which is the signed integer type of the result of subtracting two pointers;

::

    size_t

which is the unsigned integer type of the result of the sizeof operator; and

::

    wchar_t

which is an integer type whose range of values can represent distinct codes for all members of the largest extended character set specified among the supported locales; the null character shall have the code value zero. Each member of the basic character set shall have a code value equal to its value when used as the lone character in an integer character constant if an implementation does not define \__STDC_MB_MIGHT_NEQ_WC\_\_.

.. _9899_7.17p3:

.. container:: snum

   :ref:`3 <9899_7.17p3>`

The macros are

::

    NULL

which expands to an implementation-defined null pointer constant; and

::

    offsetof(type, member-designator)

which expands to an integer constant expression that has type size_t, the value of which is the offset in bytes, to the structure member (designated by member-designator), from the beginning of its structure (designated by type). The type and member designator shall be such that given

::

    static type t;

then the expression &(t.member-designator) evaluates to an address constant. (If the specified member is a bit-field, the behavior is undefined.)

.. rubric:: Recommended practice

.. _9899_7.17p4:

.. container:: snum

   :ref:`4 <9899_7.17p4>`

The types used for size_t and ptrdiff_t should not have an integer conversion rank greater than that of signed long int unless the implementation supports objects large enough to make this necessary.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_7.11`

