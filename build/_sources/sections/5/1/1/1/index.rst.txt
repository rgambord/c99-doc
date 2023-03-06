.. _9899_5.1.1.1:

5.1.1.1 Program structure
'''''''''''''''''''''''''

.. _9899_5.1.1.1p1:

.. container:: snum

   :ref:`1 <9899_5.1.1.1p1>`

A C program need not all be translated at the same time. The text of the program is kept in units called *source files*\ , (or *preprocessing files*\ ) in this International Standard. A source file together with all the headers and source files included via the preprocessing directive `#include` is known as a *preprocessing translation unit*\ . After preprocessing, a preprocessing translation unit is called a *translation unit*\ . Previously translated translation units may be preserved individually or in libraries. The separate translation units of a program communicate by (for example) calls to functions whose identifiers have external linkage, manipulation of objects whose identifiers have external linkage, or manipulation of data files. Translation units may be separately translated and then later linked to produce an executable program.

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.2.2`
   - :ref:`9899_6.9`
   - :ref:`9899_6.10`

