.. _9899_7.20.3.4:

7.20.3.4 The realloc function
'''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.20.3.4p1:

.. container:: snum

   :ref:`1 <9899_7.20.3.4p1>`



::

    #include <stdlib.h>
    void *realloc(void *ptr, size_t size);

.. rubric:: Description

.. _9899_7.20.3.4p2:

.. container:: snum

   :ref:`2 <9899_7.20.3.4p2>`

The realloc function deallocates the old object pointed to by ptr and returns a pointer to a new object that has the size specified by size. The contents of the new object shall be the same as that of the old object prior to deallocation, up to the lesser of the new and old sizes. Any bytes in the new object beyond the size of the old object have indeterminate values.

.. _9899_7.20.3.4p3:

.. container:: snum

   :ref:`3 <9899_7.20.3.4p3>`

If ptr is a null pointer, the realloc function behaves like the malloc function for the specified size. Otherwise, if ptr does not match a pointer earlier returned by the calloc, malloc, or realloc function, or if the space has been deallocated by a call to the free or realloc function, the behavior is undefined. If memory for the new object cannot be allocated, the old object is not deallocated and its value is unchanged.

.. rubric:: Returns

.. _9899_7.20.3.4p4:

.. container:: snum

   :ref:`4 <9899_7.20.3.4p4>`

The realloc function returns a pointer to the new object (which may have the same value as a pointer to the old object), or a null pointer if the new object could not be allocated.

