.. _9899_A.1.8:

A.1.8 Header names
^^^^^^^^^^^^^^^^^^

(:ref:`6.4.7 <9899_6.4.7>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            header-name
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            <
     
   
         .. container:: syntax-nonterminal
   
            h-char-sequence
     
   
         .. container:: syntax-terminal
   
            >
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            "
     
   
         .. container:: syntax-nonterminal
   
            q-char-sequence
     
   
         .. container:: syntax-terminal
   
            "
   
(:ref:`6.4.7 <9899_6.4.7>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            h-char-sequence
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            h-char
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            h-char-sequence
     
   
         .. container:: syntax-nonterminal
   
            h-char
   
(:ref:`6.4.7 <9899_6.4.7>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            h-char
   
         :
   
      .. container:: syntax-text-rule
       
         any member of the source character set except the |_|
   
         .. container:: syntax-nonterminal
   
            new-line
     
         |_| character and |_|
   
         .. container:: syntax-terminal
   
            >
   
(:ref:`6.4.7 <9899_6.4.7>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            q-char-sequence
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            q-char
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            q-char-sequence
     
   
         .. container:: syntax-nonterminal
   
            q-char
   
(:ref:`6.4.7 <9899_6.4.7>`)

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            q-char
   
         :
   
      .. container:: syntax-text-rule
       
         any member of the source character set except the |_|

         .. container:: syntax-nonterminal
   
            new-line
   
         |_| character and |_|
   
         .. container:: syntax-terminal
   
            "

