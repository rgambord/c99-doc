.. _9899_7.5:

7.5 Errors \<errno.h>
~~~~~~~~~~~~~~~~~~~~~

.. _9899_7.5p1:

:ref:`1 <9899_7.5p1>` The header :ref:`\<errno.h> <9899_7.5>` defines several macros, all relating to the reporting of error conditions.

.. _9899_7.5p2:

:ref:`2 <9899_7.5p2>` The macros are

::

    EDOM
    EILSEQ
    ERANGE

which expand to integer constant expressions with type int, distinct positive values, and which are suitable for use in #if preprocessing directives; and

::

    errno

which expands to a modifiable lvalue\ [#9899_note175]_ that has type int, the value of which is set to a positive error number by several library functions. It is unspecified whether errno is a macro or an identifier declared with external linkage. If a macro definition is suppressed in order to access an actual object, or a program defines an identifier with the name errno, the behavior is undefined.

.. _9899_7.5p3:

:ref:`3 <9899_7.5p3>` The value of errno is zero at program startup, but is never set to zero by any library function.\ [#9899_note176]_ The value of errno may be set to nonzero by a library function call whether or not there is an error, provided the use of errno is not documented in the description of the function in this International Standard.

.. _9899_7.5p4:

:ref:`4 <9899_7.5p4>` Additional macro definitions, beginning with E and a digit or E and an uppercase letter,\ [#9899_note177]_ may also be specified by the implementation.







.. rubric:: Footnotes

.. [#9899_note175] The macro errno need not be the identifier of an object. It might expand to a modifiable lvalue resulting from a function call (for example, \*errno()).
.. [#9899_note176] Thus, a program that uses errno for error checking should set it to zero before a library function call, then inspect it before a subsequent library function call. Of course, a library function can save the value of errno on entry and then set it to zero, as long as the original value is restored if errno's value is still zero just before the return.
.. [#9899_note177] See ''future library directions'' (:ref:`7.26.3 <9899_7.26.3>`).
