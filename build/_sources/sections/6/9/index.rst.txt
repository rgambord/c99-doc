.. _9899_6.9:

6.9 External definitions
~~~~~~~~~~~~~~~~~~~~~~~~


.. toctree::
   :maxdepth: 2

   1/index
   2/index


.. rubric:: Syntax

.. _9899_6.9p1:

.. container:: snum

   :ref:`1 <9899_6.9p1>`



.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            translation-unit
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            external-declaration
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            translation-unit
     
   
         .. container:: syntax-nonterminal
   
            external-declaration
   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            external-declaration
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            function-definition
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            declaration

.. rubric:: Constraints

.. _9899_6.9p2:

.. container:: snum

   :ref:`2 <9899_6.9p2>`

The storage-class specifiers auto and register shall not appear in the declaration specifiers in an external declaration.

.. _9899_6.9p3:

.. container:: snum

   :ref:`3 <9899_6.9p3>`

There shall be no more than one external definition for each identifier declared with internal linkage in a translation unit. Moreover, if an identifier declared with internal linkage is used in an expression (other than as a part of the operand of a sizeof operator whose result is an integer constant), there shall be exactly one external definition for the identifier in the translation unit.

.. rubric:: Semantics

.. _9899_6.9p4:

.. container:: snum

   :ref:`4 <9899_6.9p4>`

As discussed in :ref:`5.1.1.1 <9899_5.1.1.1>`, the unit of program text after preprocessing is a translation unit, which consists of a sequence of external declarations. These are described as "external" because they appear outside any function (and hence have file scope). As discussed in :ref:`6.7 <9899_6.7>`, a declaration that also causes storage to be reserved for an object or a function named by the identifier is a definition.

.. _9899_6.9p5:

.. container:: snum

   :ref:`5 <9899_6.9p5>`

An external definition is an external declaration that is also a definition of a function (other than an inline definition) or an object. If an identifier declared with external linkage is used in an expression (other than as part of the operand of a sizeof operator whose result is an integer constant), somewhere in the entire program there shall be exactly one external definition for the identifier; otherwise, there shall be no more than one.\ [#9899_note140]_





.. rubric:: Footnotes

.. [#9899_note140] Thus, if an identifier declared with external linkage is not used in an expression, there need be no external definition for it.
