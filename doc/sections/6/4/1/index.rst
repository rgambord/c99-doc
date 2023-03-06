.. _9899_6.4.1:

6.4.1 Keywords
^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.4.1p1:

.. container:: snum

   :ref:`1 <9899_6.4.1p1>`



.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            keyword
   
         : one of
   
      .. container:: syntax-rule-tbl
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               auto
      
            .. container:: syntax-terminal
      
               enum
      
            .. container:: syntax-terminal
      
               restrict
      
            .. container:: syntax-terminal
      
               unsigned
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               break
      
            .. container:: syntax-terminal
      
               extern
      
            .. container:: syntax-terminal
      
               return
      
            .. container:: syntax-terminal
      
               void
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               case
      
            .. container:: syntax-terminal
      
               float
      
            .. container:: syntax-terminal
      
               short
      
            .. container:: syntax-terminal
      
               volatile
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               char
      
            .. container:: syntax-terminal
      
               for
      
            .. container:: syntax-terminal
      
               signed
      
            .. container:: syntax-terminal
      
               while
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               const
      
            .. container:: syntax-terminal
      
               goto
      
            .. container:: syntax-terminal
      
               sizeof
      
            .. container:: syntax-terminal
      
               _Bool
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               continue
      
            .. container:: syntax-terminal
      
               if
      
            .. container:: syntax-terminal
      
               static
      
            .. container:: syntax-terminal
      
               _Complex
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               default
      
            .. container:: syntax-terminal
      
               inline
      
            .. container:: syntax-terminal
      
               struct
      
            .. container:: syntax-terminal
      
               _Imaginary
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               do
      
            .. container:: syntax-terminal
      
               int
      
            .. container:: syntax-terminal
      
               switch
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               double
      
            .. container:: syntax-terminal
      
               long
      
            .. container:: syntax-terminal
      
               typedef
      
         .. container:: syntax-rule
      
            .. container:: syntax-terminal
      
               else
      
            .. container:: syntax-terminal
      
               register
      
            .. container:: syntax-terminal
      
               union

.. rubric:: Semantics

.. _9899_6.4.1p2:

.. container:: snum

   :ref:`2 <9899_6.4.1p2>`

The above tokens (case sensitive) are reserved (in translation phases 7 and 8) for use as keywords, and shall not be used otherwise. The keyword \_Imaginary is reserved for specifying imaginary types.\ [#9899_note59]_





.. rubric:: Footnotes

.. [#9899_note59] One possible specification for imaginary types appears in :ref:`annex G <9899_G>`.
