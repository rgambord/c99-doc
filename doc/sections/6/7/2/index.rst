.. _9899_6.7.2:

6.7.2 Type specifiers
^^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index


.. rubric:: Syntax

.. _9899_6.7.2p1:

.. container:: snum

   :ref:`1 <9899_6.7.2p1>`



.. container:: syntax-block

   
   .. container:: syntax-production
   
      .. container:: syntax-definition
   
         .. container:: syntax-nonterminal
   
            type-specifier
   
         :
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            void
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            char
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            short
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            int
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            long
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            float
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            double
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            signed
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            unsigned
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            _Bool
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-terminal
   
            _Complex
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            struct-or-union-specifier
     
   
         .. container:: syntax-terminal
   
            \*
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            enum-specifier
   
   
      .. container:: syntax-rule
       
   
         .. container:: syntax-nonterminal
   
            typedef-name

.. rubric:: Constraints

.. _9899_6.7.2p2:

.. container:: snum

   :ref:`2 <9899_6.7.2p2>`

At least one type specifier shall be given in the declaration specifiers in each declaration, and in the specifier-qualifier list in each struct declaration and type name. Each list of type specifiers shall be one of the following sets (delimited by commas, when there is more than one set on a line); the type specifiers may occur in any order, possibly intermixed with the other declaration specifiers.

-  void
-  char
-  signed char
-  unsigned char
-  short, signed short, short int, or signed short int
-  unsigned short, or unsigned short int
-  int, signed, or signed int
-  unsigned, or unsigned int
-  long, signed long, long int, or signed long int
-  unsigned long, or unsigned long int
-  long long, signed long long, long long int, or signed long long int
-  unsigned long long, or unsigned long long int
-  float
-  double
-  long double
-  \_Bool
-  float \_Complex
-  double \_Complex
-  long double \_Complex
-  struct or union specifier \*
-  enum specifier
-  typedef name

.. _9899_6.7.2p3:

.. container:: snum

   :ref:`3 <9899_6.7.2p3>`

The type specifier \_Complex shall not be used if the implementation does not provide complex types.\ [#9899_note104]_

.. rubric:: Semantics

.. _9899_6.7.2p4:

.. container:: snum

   :ref:`4 <9899_6.7.2p4>`

Specifiers for structures, unions, and enumerations are discussed in :ref:`6.7.2.1 <9899_6.7.2.1>` through :ref:`6.7.2.3 <9899_6.7.2.3>`. Declarations of typedef names are discussed in :ref:`6.7.7 <9899_6.7.7>`. The characteristics of the other types are discussed in :ref:`6.2.5 <9899_6.2.5>`.

.. _9899_6.7.2p5:

.. container:: snum

   :ref:`5 <9899_6.7.2p5>`

Each of the comma-separated sets designates the same type, except that for bit-fields, it is implementation-defined whether the specifier int designates the same type as signed int or the same type as unsigned int.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.7.2.2`
   - :ref:`9899_6.7.2.1`
   - :ref:`9899_6.7.2.3`
   - :ref:`9899_6.7.7`





.. rubric:: Footnotes

.. [#9899_note104] Freestanding implementations are not required to provide complex types. \*
