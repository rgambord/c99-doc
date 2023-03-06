.. _9899_A.1.6:

A.1.6 String literals
^^^^^^^^^^^^^^^^^^^^^

(:ref:`6.4.5 <9899_6.4.5>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            string-literal
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            "
     
   
         .. container:: syntax-nonterminal
   
            s-char-sequence
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            "
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            L"
     
   
         .. container:: syntax-nonterminal
   
            s-char-sequence
   
   
            .. container:: syntax-opt
   
               :sub:`opt`
     
   
         .. container:: syntax-terminal
   
            "
   
(:ref:`6.4.5 <9899_6.4.5>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            s-char-sequence
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            s-char
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            s-char-sequence
     
   
         .. container:: syntax-nonterminal
   
            s-char
   
(:ref:`6.4.5 <9899_6.4.5>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            s-char
   
         :
   
      .. container:: syntax-text-rule
       
         any member of the source character set except the double-quote |_|
   
         .. container:: syntax-terminal
   
            "

         , backslash |_|
   
         .. container:: syntax-terminal
   
            \\

         , or |_|
         
         .. container:: syntax-nonterminal

            new-line

         |_| character |_|
   
      .. container:: syntax-rule
   
         .. container:: syntax-nonterminal
   
            escape-sequence

