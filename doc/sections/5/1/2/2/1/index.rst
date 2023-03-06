.. _9899_5.1.2.2.1:

5.1.2.2.1 Program startup
"""""""""""""""""""""""""

.. _9899_5.1.2.2.1p1:

.. container:: snum

   :ref:`1 <9899_5.1.2.2.1p1>`

The function called at program startup is named main. The implementation declares no prototype for this function. It shall be defined with a return type of int and with no parameters:

::

    int main(void) { /* ... */ }

or with two parameters (referred to here as argc and argv, though any names may be used, as they are local to the function in which they are declared):

::

    int main(int argc, char *argv[]) { /* ... */ }

or equivalent;\ [#9899_note9]_ or in some other implementation-defined manner.

.. _9899_5.1.2.2.1p2:

.. container:: snum

   :ref:`2 <9899_5.1.2.2.1p2>`

If they are declared, the parameters to the main function shall obey the following constraints:

-  The value of argc shall be nonnegative.
-  argv[argc] shall be a null pointer.
-  If the value of argc is greater than zero, the array members argv[0] through argv[argc-1] inclusive shall contain pointers to strings, which are given implementation-defined values by the host environment prior to program startup. The intent is to supply to the program information determined prior to program startup from elsewhere in the hosted environment. If the host environment is not capable of supplying strings with letters in both uppercase and lowercase, the implementation shall ensure that the strings are received in lowercase.
-  If the value of argc is greater than zero, the string pointed to by argv[0] represents the program name; argv[0][0] shall be the null character if the program name is not available from the host environment. If the value of argc is greater than one, the strings pointed to by argv[1] through argv[argc-1] represent the program parameters.
-  The parameters argc and argv and the strings pointed to by the argv array shall be modifiable by the program, and retain their last-stored values between program startup and program termination.





.. rubric:: Footnotes

.. [#9899_note9] Thus, int can be replaced by a typedef name defined as int, or the type of argv can be written as char \*\* argv, and so on.
