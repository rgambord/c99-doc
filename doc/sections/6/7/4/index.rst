.. _9899_6.7.4:

6.7.4 Function specifiers
^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.7.4p1:

:ref:`1 <9899_6.7.4p1>`

.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            function-specifier
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            inline

.. rubric:: Constraints

.. _9899_6.7.4p2:

:ref:`2 <9899_6.7.4p2>` Function specifiers shall be used only in the declaration of an identifier for a function.

.. _9899_6.7.4p3:

:ref:`3 <9899_6.7.4p3>` An inline definition of a function with external linkage shall not contain a definition of a modifiable object with static storage duration, and shall not contain a reference to an identifier with internal linkage.

.. _9899_6.7.4p4:

:ref:`4 <9899_6.7.4p4>` In a hosted environment, the inline function specifier shall not appear in a declaration of main.

.. rubric:: Semantics

.. _9899_6.7.4p5:

:ref:`5 <9899_6.7.4p5>` A function declared with an inline function specifier is an inline function. The function specifier may appear more than once; the behavior is the same as if it appeared only once. Making a function an inline function suggests that calls to the function be as fast as possible.\ [#9899_note120]_ The extent to which such suggestions are effective is implementation-defined.\ [#9899_note121]_

.. _9899_6.7.4p6:

:ref:`6 <9899_6.7.4p6>` Any function with internal linkage can be an inline function. For a function with external linkage, the following restrictions apply: If a function is declared with an inline function specifier, then it shall also be defined in the same translation unit. If all of the file scope declarations for a function in a translation unit include the inline function specifier without extern, then the definition in that translation unit is an inline definition. An inline definition does not provide an external definition for the function, and does not forbid an external definition in another translation unit. An inline definition provides an alternative to an external definition, which a translator may use to implement any call to the function in the same translation unit. It is unspecified whether a call to the function uses the inline definition or the external definition.\ [#9899_note122]_

.. _9899_6.7.4p7:

:ref:`7 <9899_6.7.4p7>` EXAMPLE The declaration of an inline function with external linkage can result in either an external definition, or a definition available for use only within the translation unit. A file scope declaration with extern creates an external definition. The following example shows an entire translation unit.

::

    inline double fahr(double t)
    {
          return (9.0 * t) / 5.0 + 32.0;
    }
    inline double cels(double t)
    {
          return (5.0 * (t - 32.0)) / 9.0;
    }
    extern double fahr(double);                  // creates an external definition
    double convert(int is_fahr, double temp)
    {
          /* A translator may perform inline substitutions */
          return is_fahr ? cels(temp) : fahr(temp);
    }

.. _9899_6.7.4p8:

:ref:`8 <9899_6.7.4p8>` Note that the definition of fahr is an external definition because fahr is also declared with extern, but the definition of cels is an inline definition. Because cels has external linkage and is referenced, an external definition has to appear in another translation unit (see :ref:`6.9 <9899_6.9>`); the inline definition and the external definition are distinct and either may be used for the call.

**Forward references**: function definitions (:ref:`6.9.1 <9899_6.9.1>`).







.. rubric:: Footnotes

.. [#9899_note120] By using, for example, an alternative to the usual function call mechanism, such as ''inline substitution''. Inline substitution is not textual substitution, nor does it create a new function. Therefore, for example, the expansion of a macro used within the body of the function uses the definition it had at the point the function body appears, and not where the function is called; and identifiers refer to the declarations in scope where the body occurs. Likewise, the function has a single address, regardless of the number of inline definitions that occur in addition to the external definition.
.. [#9899_note121] For example, an implementation might never perform inline substitution, or might only perform inline substitutions to calls in the scope of an inline declaration.
.. [#9899_note122] Since an inline definition is distinct from the corresponding external definition and from any other corresponding inline definitions in other translation units, all corresponding objects with static storage duration are also distinct in each of the definitions.
