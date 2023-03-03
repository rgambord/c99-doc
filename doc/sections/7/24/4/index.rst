.. _9899_7.24.4:

7.24.4 General wide string utilities
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index
   4/index
   5/index
   6/index


.. _9899_7.24.4p1:

:ref:`1 <9899_7.24.4p1>` The header :ref:`\<wchar.h> <9899_7.24>` declares a number of functions useful for wide string manipulation. Various methods are used for determining the lengths of the arrays, but in all cases a wchar_t \* argument points to the initial (lowest addressed) element of the array. If an array is accessed beyond the end of an object, the behavior is undefined.

.. _9899_7.24.4p2:

:ref:`2 <9899_7.24.4p2>` Where an argument declared as size_t n determines the length of the array for a function, n can have the value zero on a call to that function. Unless explicitly stated otherwise in the description of a particular function in this subclause, pointer arguments on such a call shall still have valid values, as described in :ref:`7.1.4 <9899_7.1.4>`. On such a call, a function that locates a wide character finds no occurrence, a function that compares two wide character sequences returns zero, and a function that copies wide characters copies zero wide characters.

