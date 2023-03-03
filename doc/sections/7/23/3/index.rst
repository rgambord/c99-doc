.. _9899_7.23.3:

7.23.3 Time conversion functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index
   4/index
   5/index


.. _9899_7.23.3p1:

:ref:`1 <9899_7.23.3p1>` Except for the strftime function, these functions each return a pointer to one of two types of static objects: a broken-down time structure or an array of char. Execution of any of the functions that return a pointer to one of these object types may overwrite the information in any object of the same type pointed to by the value returned from any previous call to any of them. The implementation shall behave as if no other library functions call these functions.

