.. _9899_the-operator-1:

6.10.3.3 The ## operator
''''''''''''''''''''''''

.. rubric:: Constraints

.. _9899_6.10.3.3p1:

:ref:`1 <9899_6.10.3.3p1>` A ## preprocessing token shall not occur at the beginning or at the end of a replacement list for either form of macro definition.

.. rubric:: Semantics

.. _9899_6.10.3.3p2:

:ref:`2 <9899_6.10.3.3p2>` If, in the replacement list of a function-like macro, a parameter is immediately preceded or followed by a ## preprocessing token, the parameter is replaced by the corresponding argument's preprocessing token sequence; however, if an argument consists of no preprocessing tokens, the parameter is replaced by a placemarker preprocessing token instead.\ [#9899_note151]_

.. _9899_6.10.3.3p3:

:ref:`3 <9899_6.10.3.3p3>` For both object-like and function-like macro invocations, before the replacement list is reexamined for more macro names to replace, each instance of a ## preprocessing token in the replacement list (not from an argument) is deleted and the preceding preprocessing token is concatenated with the following preprocessing token. Placemarker preprocessing tokens are handled specially: concatenation of two placemarkers results in a single placemarker preprocessing token, and concatenation of a placemarker with a non-placemarker preprocessing token results in the non-placemarker preprocessing token. If the result is not a valid preprocessing token, the behavior is undefined. The resulting token is available for further macro replacement. The order of evaluation of ## operators is unspecified.

.. _9899_6.10.3.3p4:

:ref:`4 <9899_6.10.3.3p4>` EXAMPLE In the following fragment:

::

    #define     hash_hash # ## #
    #define     mkstr(a) # a
    #define     in_between(a) mkstr(a)
    #define     join(c, d) in_between(c hash_hash d)
    char p[] = join(x, y); // equivalent to
                           // char p[] = "x ## y";

The expansion produces, at various stages:

.. code-block:: text

    join(x, y)
    in_between(x hash_hash y)
    in_between(x ## y)
    mkstr(x ## y)
    "x ## y"

In other words, expanding hash_hash produces a new token, consisting of two adjacent sharp signs, but this new token is not the ## operator.





.. rubric:: Footnotes

.. [#9899_note151] Placemarker preprocessing tokens do not appear in the syntax because they are temporary entities that exist only within translation phase 4.
