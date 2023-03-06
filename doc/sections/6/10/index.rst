.. _9899_6.10:

6.10 Preprocessing directives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index
   4/index
   5/index
   6/index
   7/index
   8/index
   9/index


.. rubric:: Syntax

.. _9899_6.10p1:

.. container:: snum

   :ref:`1 <9899_6.10p1>`



.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            preprocessing-file
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            group
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            group
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            group-part
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            group
     
   
         .. container:: syntax-nonterminal
   
            group-part
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            group-part
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            if-section
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            control-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            text-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-nonterminal
   
            non-directive
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            if-section
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            if-group
     
   
         .. container:: syntax-nonterminal
   
            elif-groups
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            else-group
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            endif-line
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            if-group
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            if
     
   
         .. container:: syntax-nonterminal
   
            constant-expression
     
   
         .. container:: syntax-nonterminal
   
            new-line
     
   
         .. container:: syntax-nonterminal
   
            group
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            ifdef
     
   
         .. container:: syntax-nonterminal
   
            identifier
     
   
         .. container:: syntax-nonterminal
   
            new-line
     
   
         .. container:: syntax-nonterminal
   
            group
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            ifndef
     
   
         .. container:: syntax-nonterminal
   
            identifier
     
   
         .. container:: syntax-nonterminal
   
            new-line
     
   
         .. container:: syntax-nonterminal
   
            group
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            elif-groups
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            elif-group
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            elif-groups
     
   
         .. container:: syntax-nonterminal
   
            elif-group
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            elif-group
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            elif
     
   
         .. container:: syntax-nonterminal
   
            constant-expression
     
   
         .. container:: syntax-nonterminal
   
            new-line
     
   
         .. container:: syntax-nonterminal
   
            group
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            else-group
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            else
     
   
         .. container:: syntax-nonterminal
   
            new-line
     
   
         .. container:: syntax-nonterminal
   
            group
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            endif-line
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            endif
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            control-line
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            include
     
   
         .. container:: syntax-nonterminal
   
            pp-tokens
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            define
     
   
         .. container:: syntax-nonterminal
   
            identifier
     
   
         .. container:: syntax-nonterminal
   
            replacement-list
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            define
     
   
         .. container:: syntax-nonterminal
   
            identifier
     
   
         .. container:: syntax-nonterminal
   
            lparen
     
   
         .. container:: syntax-nonterminal
   
            identifier-list
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            )
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            replacement-list
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            define
     
   
         .. container:: syntax-nonterminal
   
            identifier
     
   
         .. container:: syntax-nonterminal
   
            lparen
     
   
         .. container:: syntax-terminal
   
            \.\.\.
     
   
         .. container:: syntax-terminal
   
            )
     
   
         .. container:: syntax-nonterminal
   
            replacement-list
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            define
     
   
         .. container:: syntax-nonterminal
   
            identifier
     
   
         .. container:: syntax-nonterminal
   
            lparen
     
   
         .. container:: syntax-nonterminal
   
            identifier-list
     
   
         .. container:: syntax-terminal
   
            ,
     
   
         .. container:: syntax-terminal
   
            \.\.\.
     
   
         .. container:: syntax-terminal
   
            )
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            replacement-list
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            undef
     
   
         .. container:: syntax-nonterminal
   
            identifier
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            line
     
   
         .. container:: syntax-nonterminal
   
            pp-tokens
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            error
     
   
         .. container:: syntax-nonterminal
   
            pp-tokens
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-terminal
   
            pragma
     
   
         .. container:: syntax-nonterminal
   
            pp-tokens
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            #
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            text-line
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pp-tokens
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            non-directive
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pp-tokens
     
   
         .. container:: syntax-nonterminal
   
            new-line
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            lparen
   
         :
   
      .. container:: syntax-rule
       
   
         a
     
   
         .. container:: syntax-terminal
   
            (
     
   
         character not immediately preceded by white-space
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            replacement-list
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pp-tokens
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            pp-tokens
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            preprocessing-token
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pp-tokens
     
   
         .. container:: syntax-nonterminal
   
            preprocessing-token
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            new-line
   
         :
   
      .. container:: syntax-rule
   
         the
   
         .. container:: syntax-nonterminal
   
            new-line
   
         character

.. rubric:: Description

.. _9899_6.10p2:

.. container:: snum

   :ref:`2 <9899_6.10p2>`

A preprocessing directive consists of a sequence of preprocessing tokens that satisfies the following constraints: The first token in the sequence is a # preprocessing token that (at the start of translation phase 4) is either the first character in the source file (optionally after white space containing no new-line characters) or that follows white space containing at least one new-line character. The last token in the sequence is the first new- line character that follows the first token in the sequence.\ [#9899_note143]_ A new-line character ends the preprocessing directive even if it occurs within what would otherwise be an invocation of a function-like macro.

.. _9899_6.10p3:

.. container:: snum

   :ref:`3 <9899_6.10p3>`

A text line shall not begin with a # preprocessing token. A non-directive shall not begin with any of the directive names appearing in the syntax.

.. _9899_6.10p4:

.. container:: snum

   :ref:`4 <9899_6.10p4>`

When in a group that is skipped (:ref:`6.10.1 <9899_6.10.1>`), the directive syntax is relaxed to allow any sequence of preprocessing tokens to occur between the directive name and the following new-line character.

.. rubric:: Constraints

.. _9899_6.10p5:

.. container:: snum

   :ref:`5 <9899_6.10p5>`

The only white-space characters that shall appear between preprocessing tokens within a preprocessing directive (from just after the introducing # preprocessing token through just before the terminating new-line character) are space and horizontal-tab (including spaces that have replaced comments or possibly other white-space characters in translation phase 3).

.. rubric:: Semantics

.. _9899_6.10p6:

.. container:: snum

   :ref:`6 <9899_6.10p6>`

The implementation can process and skip sections of source files conditionally, include other source files, and replace macros. These capabilities are called preprocessing, because conceptually they occur before translation of the resulting translation unit.

.. _9899_6.10p7:

.. container:: snum

   :ref:`7 <9899_6.10p7>`

The preprocessing tokens within a preprocessing directive are not subject to macro expansion unless otherwise stated.

.. _9899_6.10p8:

.. container:: snum

   :ref:`8 <9899_6.10p8>`

EXAMPLE In:


.. code-block:: text

    #define EMPTY
    EMPTY # include <file.h>

the sequence of preprocessing tokens on the second line is not a preprocessing directive, because it does not begin with a # at the start of translation phase 4, even though it will do so after the macro EMPTY has been replaced.





.. rubric:: Footnotes

.. [#9899_note143] Thus, preprocessing directives are commonly called "lines". These "lines" have no other syntactic significance, as all white space is equivalent except in certain situations during preprocessing (see the # character string literal creation operator in :ref:`6.10.3.2 <9899_6.10.3.2>`, for example).
