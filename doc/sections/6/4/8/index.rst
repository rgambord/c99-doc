.. _9899_6.4.8:

6.4.8 Preprocessing numbers
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.4.8p1:

:ref:`1 <9899_6.4.8p1>`

.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            pp-number
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            digit
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            .
     
   
         .. container:: syntax-nonterminal
   
            digit
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pp-number
     
   
         .. container:: syntax-nonterminal
   
            digit
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pp-number
     
   
         .. container:: syntax-nonterminal
   
            identifier-nondigit
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pp-number
     
   
         .. container:: syntax-terminal
   
            e
     
   
         .. container:: syntax-nonterminal
   
            sign
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pp-number
     
   
         .. container:: syntax-terminal
   
            E
     
   
         .. container:: syntax-nonterminal
   
            sign
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pp-number
     
   
         .. container:: syntax-terminal
   
            p
     
   
         .. container:: syntax-nonterminal
   
            sign
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pp-number
     
   
         .. container:: syntax-terminal
   
            P
     
   
         .. container:: syntax-nonterminal
   
            sign
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            pp-number
     
   
         .. container:: syntax-terminal
   
            .

.. rubric:: Description

.. _9899_6.4.8p2:

:ref:`2 <9899_6.4.8p2>` A preprocessing number begins with a digit optionally preceded by a period (.) and may be followed by valid identifier characters and the character sequences e+, e-, E+, E-, p+, p-, P+, or P-.

.. _9899_6.4.8p3:

:ref:`3 <9899_6.4.8p3>` Preprocessing number tokens lexically include all floating and integer constant tokens.

.. rubric:: Semantics

.. _9899_6.4.8p4:

:ref:`4 <9899_6.4.8p4>` A preprocessing number does not have type or a value; it acquires both after a successful conversion (as part of translation phase 7) to a floating constant token or an integer constant token.

