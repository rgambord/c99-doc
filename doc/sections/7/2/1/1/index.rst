.. _9899_7.2.1.1:

7.2.1.1 The assert macro
''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.2.1.1p1:

:ref:`1 <9899_7.2.1.1p1>`

::

    #include <assert.h>
    void assert(scalar expression);

.. rubric:: Description

.. _9899_7.2.1.1p2:

:ref:`2 <9899_7.2.1.1p2>` The assert macro puts diagnostic tests into programs; it expands to a void expression. When it is executed, if expression (which shall have a scalar type) is false (that is, compares equal to 0), the assert macro writes information about the particular call that failed (including the text of the argument, the name of the source file, the source line number, and the name of the enclosing function -- the latter are respectively the values of the preprocessing macros \__FILE\_\_ and \__LINE\_\_ and of the identifier \__func\_\_) on the standard error stream in an implementation-defined format.\ [#9899_note165]_ It then calls the abort function.

.. rubric:: Returns

.. _9899_7.2.1.1p3:

:ref:`3 <9899_7.2.1.1p3>` The assert macro returns no value.

**Forward references**: the abort function (:ref:`7.20.4.1 <9899_7.20.4.1>`).





.. rubric:: Footnotes

.. [#9899_note165] The message written might be of the form: Assertion failed: expression, function abc, file xyz, line nnn.
