.. _9899_6.4.6:

6.4.6 Punctuators
^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.4.6p1:

:ref:`1 <9899_6.4.6p1>`

.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            punctuator
   
         : one of
   
      .. container:: syntax-rule-tbl
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               [
      
            .. container:: syntax-terminal
      
               ]
      
            .. container:: syntax-terminal
      
               (
      
            .. container:: syntax-terminal
      
               )
      
            .. container:: syntax-terminal
      
               {
      
            .. container:: syntax-terminal
      
               }
      
            .. container:: syntax-terminal
      
               .
      
            .. container:: syntax-terminal
      
               ->
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               ++
      
            .. container:: syntax-terminal
      
               --
      
            .. container:: syntax-terminal
      
               &
      
            .. container:: syntax-terminal
      
               \*
      
            .. container:: syntax-terminal
      
               \+
      
            .. container:: syntax-terminal
      
               \-
      
            .. container:: syntax-terminal
      
               ~
      
            .. container:: syntax-terminal
      
               !
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               /
      
            .. container:: syntax-terminal
      
               \%
      
            .. container:: syntax-terminal
      
               <<
      
            .. container:: syntax-terminal
      
               >>
      
            .. container:: syntax-terminal
      
               <
      
            .. container:: syntax-terminal
      
               >
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               <=
      
            .. container:: syntax-terminal
      
               >=
      
            .. container:: syntax-terminal
      
               ==
      
            .. container:: syntax-terminal
      
               !=
      
            .. container:: syntax-terminal
      
               ^
      
            .. container:: syntax-terminal
      
               \|
      
            .. container:: syntax-terminal
      
               &&
      
            .. container:: syntax-terminal
      
               \|\|
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               ?
      
            .. container:: syntax-terminal
      
               :
      
            .. container:: syntax-terminal
      
               ;
      
            .. container:: syntax-terminal
      
               \.\.\.
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               =
      
            .. container:: syntax-terminal
      
               \*=
      
            .. container:: syntax-terminal
      
               /=
      
            .. container:: syntax-terminal
      
               \%=
      
            .. container:: syntax-terminal
      
               +=
      
            .. container:: syntax-terminal
      
               -=
      
            .. container:: syntax-terminal
      
               <<=
      
            .. container:: syntax-terminal
      
               >>=
      
            .. container:: syntax-terminal
      
               &=
      
            .. container:: syntax-terminal
      
               ^=
      
            .. container:: syntax-terminal
      
               \|=
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               ,
      
            .. container:: syntax-terminal
      
               #
      
            .. container:: syntax-terminal
      
               ##
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               <:
      
            .. container:: syntax-terminal
      
               :>
      
            .. container:: syntax-terminal
      
               <\%
      
            .. container:: syntax-terminal
      
               \%>
      
            .. container:: syntax-terminal
      
               \%:
      
            .. container:: syntax-terminal
      
               \%:\%:

.. rubric:: Semantics

.. _9899_6.4.6p2:

:ref:`2 <9899_6.4.6p2>` A punctuator is a symbol that has independent syntactic and semantic significance. Depending on context, it may specify an operation to be performed (which in turn may yield a value or a function designator, produce a side effect, or some combination thereof) in which case it is known as an operator (other forms of operator also exist in some contexts). An operand is an entity on which an operator acts.

.. _9899_6.4.6p3:

:ref:`3 <9899_6.4.6p3>` In all aspects of the language, the six tokens\ [#9899_note67]_

.. code-block:: text

    <:    :>      <%    %>     %:     %:%:

behave, respectively, the same as the six tokens

.. code-block:: text

    [     ]       {     }      #      ##

except for their spelling.\ [#9899_note68]_

**Forward references**: expressions (:ref:`6.5 <9899_6.5>`), declarations (:ref:`6.7 <9899_6.7>`), preprocessing directives (:ref:`6.10 <9899_6.10>`), statements (:ref:`6.8 <9899_6.8>`).






.. rubric:: Footnotes

.. [#9899_note67] These tokens are sometimes called ''digraphs''.
.. [#9899_note68] Thus [ and <: behave differently when ''stringized'' (see :ref:`6.10.3.2 <9899_6.10.3.2>`), but can otherwise be freely interchanged.
