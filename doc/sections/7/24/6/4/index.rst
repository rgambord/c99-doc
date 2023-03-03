.. _9899_7.24.6.4:

7.24.6.4 Restartable multibyte/wide string conversion functions
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


.. toctree::
   :maxdepth: 2

   1/index
   2/index


.. _9899_7.24.6.4p1:

:ref:`1 <9899_7.24.6.4p1>` These functions differ from the corresponding multibyte string functions of :ref:`7.20.8 <9899_7.20.8>` (mbstowcs and wcstombs) in that they have an extra parameter, ps, of type pointer to mbstate_t that points to an object that can completely describe the current conversion state of the associated multibyte character sequence. If ps is a null pointer, each function uses its own internal mbstate_t object instead, which is initialized at program startup to the initial conversion state. The implementation behaves as if no library function calls these functions with a null pointer for ps.

.. _9899_7.24.6.4p2:

:ref:`2 <9899_7.24.6.4p2>` Also unlike their corresponding functions, the conversion source parameter, src, has a pointer-to-pointer type. When the function is storing the results of conversions (that is, when dst is not a null pointer), the pointer object pointed to by this parameter is updated to reflect the amount of the source processed by that invocation.

