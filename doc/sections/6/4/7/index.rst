.. _9899_6.4.7:

6.4.7 Header names
^^^^^^^^^^^^^^^^^^

.. rubric:: Syntax

.. _9899_6.4.7p1:

.. container:: snum

   :ref:`1 <9899_6.4.7p1>`



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

.. rubric:: Semantics

.. _9899_6.4.7p2:

.. container:: snum

   :ref:`2 <9899_6.4.7p2>`

The sequences in both forms of header names are mapped in an implementation-defined manner to headers or external source file names as specified in :ref:`6.10.2 <9899_6.10.2>`.

.. _9899_6.4.7p3:

.. container:: snum

   :ref:`3 <9899_6.4.7p3>`

If the characters **'**\ , **\\**\ , **"**\ , **//**\ , or **/\*** occur in the sequence between the **<** and **>** delimiters, the behavior is undefined. Similarly, if the characters **'**\ , **\\**\ , **//**\ , or **/\*** occur in the sequence between the **"** delimiters, the behavior is undefined.\ [#9899_note69]_ Header name preprocessing tokens are recognized only within `#include` preprocessing directives and in implementation-defined locations within `#pragma` directives.\ [#9899_note70]_

.. _9899_6.4.7p4:

.. container:: snum

   :ref:`4 <9899_6.4.7p4>`

EXAMPLE The following sequence of characters:

::

    0x3<1/a.h>1e2
    #include <1/a.h>
    #define const.member@$

forms the following sequence of preprocessing tokens (with each individual preprocessing token delimited by a { on the left and a } on the right).

.. code-block:: text

    {0x3}{<}{1}{/}{a}{.}{h}{>}{1e2}
    {#}{include} {<1/a.h>}
    {#}{define} {const}{.}{member}{@}{$}

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.10.2`






.. rubric:: Footnotes

.. [#9899_note69] Thus, sequences of characters that resemble escape sequences cause undefined behavior.
.. [#9899_note70] For an example of a header name preprocessing token used in a `#pragma` directive, see :ref:`6.10.9 <9899_6.10.9>`.
