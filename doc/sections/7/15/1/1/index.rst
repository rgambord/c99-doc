.. _9899_7.15.1.1:

7.15.1.1 The va_arg macro
'''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.15.1.1p1:

:ref:`1 <9899_7.15.1.1p1>`

::

    #include <stdarg.h>
    type va_arg(va_list ap, type);

.. rubric:: Description

.. _9899_7.15.1.1p2:

:ref:`2 <9899_7.15.1.1p2>` The va_arg macro expands to an expression that has the specified type and the value of the next argument in the call. The parameter ap shall have been initialized by the va_start or va_copy macro (without an intervening invocation of the va_end macro for the same ap). Each invocation of the va_arg macro modifies ap so that the values of successive arguments are returned in turn. The parameter type shall be a type name specified such that the type of a pointer to an object that has the specified type can be obtained simply by postfixing a \* to type. If there is no actual next argument, or if type is not compatible with the type of the actual next argument (as promoted according to the default argument promotions), the behavior is undefined, except for the following cases:

-  one type is a signed integer type, the other type is the corresponding unsigned integer type, and the value is representable in both types;
-  one type is pointer to void and the other is a pointer to a character type.

.. rubric:: Returns

.. _9899_7.15.1.1p3:

:ref:`3 <9899_7.15.1.1p3>` The first invocation of the va_arg macro after that of the va_start macro returns the value of the argument after that specified by parmN . Successive invocations return the values of the remaining arguments in succession.

