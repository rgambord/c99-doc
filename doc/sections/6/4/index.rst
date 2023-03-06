.. _9899_6.4:

6.4 Lexical elements
~~~~~~~~~~~~~~~~~~~~


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

.. _9899_6.4p1:

.. container:: snum

   :ref:`1 <9899_6.4p1>`



.. container:: syntax-block
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            token
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            keyword
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            identifier
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            constant
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            string-literal
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            punctuator
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            preprocessing-token
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            header-name
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            identifier
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pp-number
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            character-constant
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            string-literal
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            punctuator
   
   
      .. container:: syntax-text-rule
       
         each non-white-space character that cannot be one of the above

.. rubric:: Constraints

.. _9899_6.4p2:

.. container:: snum

   :ref:`2 <9899_6.4p2>`

Each preprocessing token that is converted to a token shall have the lexical form of a keyword, an identifier, a constant, a string literal, or a punctuator.

.. rubric:: Semantics

.. _9899_6.4p3:

.. container:: snum

   :ref:`3 <9899_6.4p3>`

A token is the minimal lexical element of the language in translation phases 7 and 8. The categories of tokens are: keywords, identifiers, constants, string literals, and punctuators. A preprocessing token is the minimal lexical element of the language in translation phases 3 through 6. The categories of preprocessing tokens are: header names, identifiers, preprocessing numbers, character constants, string literals, punctuators, and single non-white-space characters that do not lexically match the other preprocessing token categories.\ [#9899_note58]_ If a ' or a " character matches the last category, the behavior is undefined. Preprocessing tokens can be separated by white space; this consists of comments (described later), or white-space characters (space, horizontal tab, new-line, vertical tab, and form-feed), or both. As described in :ref:`6.10 <9899_6.10>`, in certain circumstances during translation phase 4, white space (or the absence thereof) serves as more than preprocessing token separation. White space may appear within a preprocessing token only as part of a header name or between the quotation characters in a character constant or string literal.

.. _9899_6.4p4:

.. container:: snum

   :ref:`4 <9899_6.4p4>`

If the input stream has been parsed into preprocessing tokens up to a given character, the next preprocessing token is the longest sequence of characters that could constitute a preprocessing token. There is one exception to this rule: header name preprocessing tokens are recognized only within `#include` preprocessing directives and in implementation-defined locations within `#pragma` directives. In such contexts, a sequence of characters that could be either a header name or a string literal is recognized as the former.

.. _9899_6.4p5:

.. container:: snum

   :ref:`5 <9899_6.4p5>`

EXAMPLE 1 The program fragment 1Ex is parsed as a preprocessing number token (one that is not a valid floating or integer constant token), even though a parse as the pair of preprocessing tokens 1 and Ex might produce a valid expression (for example, if Ex were a macro defined as +1). Similarly, the program fragment 1E1 is parsed as a preprocessing number (one that is a valid floating constant token), whether or not E is a macro name.

.. _9899_6.4p6:

.. container:: snum

   :ref:`6 <9899_6.4p6>`

EXAMPLE 2 The program fragment x+++++y is parsed as x ++ ++ + y, which violates a constraint on increment operators, even though the parse x ++ + ++ y might yield a correct expression.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.4.4.4`
   - :ref:`9899_6.4.9`
   - :ref:`9899_6.5`
   - :ref:`9899_6.4.4.2`
   - :ref:`9899_6.4.7`
   - :ref:`9899_6.10.3`
   - :ref:`9899_6.5.2.4`
   - :ref:`9899_6.5.3.1`
   - :ref:`9899_6.10`
   - :ref:`9899_6.4.8`
   - :ref:`9899_6.4.5`





.. rubric:: Footnotes

.. [#9899_note58] An additional category, placemarkers, is used internally in translation phase 4 (see :ref:`6.10.3.3 <9899_6.10.3.3>`); it cannot occur in source files.
