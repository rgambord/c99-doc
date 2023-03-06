.. _9899_6.5.3.4:

6.5.3.4 The sizeof operator
'''''''''''''''''''''''''''

.. rubric:: Constraints

.. _9899_6.5.3.4p1:

.. container:: snum

   :ref:`1 <9899_6.5.3.4p1>`

The sizeof operator shall not be applied to an expression that has function type or an incomplete type, to the parenthesized name of such a type, or to an expression that designates a bit-field member.

.. rubric:: Semantics

.. _9899_6.5.3.4p2:

.. container:: snum

   :ref:`2 <9899_6.5.3.4p2>`

The sizeof operator yields the size (in bytes) of its operand, which may be an expression or the parenthesized name of a type. The size is determined from the type of the operand. The result is an integer. If the type of the operand is a variable length array type, the operand is evaluated; otherwise, the operand is not evaluated and the result is an integer constant.

.. _9899_6.5.3.4p3:

.. container:: snum

   :ref:`3 <9899_6.5.3.4p3>`

When applied to an operand that has type char, unsigned char, or signed char, (or a qualified version thereof) the result is 1. When applied to an operand that has array type, the result is the total number of bytes in the array.\ [#9899_note88]_ When applied to an operand that has structure or union type, the result is the total number of bytes in such an object, including internal and trailing padding.

.. _9899_6.5.3.4p4:

.. container:: snum

   :ref:`4 <9899_6.5.3.4p4>`

The value of the result is implementation-defined, and its type (an unsigned integer type) is size_t, defined in :ref:`\<stddef.h> <9899_7.17>` (and other headers).

.. _9899_6.5.3.4p5:

.. container:: snum

   :ref:`5 <9899_6.5.3.4p5>`

EXAMPLE 1 A principal use of the sizeof operator is in communication with routines such as storage allocators and I/O systems. A storage-allocation function might accept a size (in bytes) of an object to allocate and return a pointer to void. For example:

::

    extern void *alloc(size_t);
    double *dp = alloc(sizeof *dp);

The implementation of the alloc function should ensure that its return value is aligned suitably for conversion to a pointer to double.

.. _9899_6.5.3.4p6:

.. container:: snum

   :ref:`6 <9899_6.5.3.4p6>`

EXAMPLE 2 Another use of the sizeof operator is to compute the number of elements in an array:

::

    sizeof array / sizeof array[0]

.. _9899_6.5.3.4p7:

.. container:: snum

   :ref:`7 <9899_6.5.3.4p7>`

EXAMPLE 3 In this example, the size of a variable length array is computed and returned from a function:

::

    #include <stddef.h>
    size_t fsize3(int n)
    {
          char b[n+3];                  // variable length array
          return sizeof b;              // execution time sizeof
    }

::

    int main()
    {
          size_t size;
          size = fsize3(10); // fsize3 returns 13
          return 0;
    }

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_7.17`
   - :ref:`9899_7.17`
   - :ref:`9899_6.7`
   - :ref:`9899_6.7.2.1`
   - :ref:`9899_6.7.6`
   - :ref:`9899_6.7.5.2`





.. rubric:: Footnotes

.. [#9899_note88] When applied to a parameter declared to have array or function type, the sizeof operator yields the size of the adjusted (pointer) type (see :ref:`6.9.1 <9899_6.9.1>`).
