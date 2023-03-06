.. _9899_7.18:

7.18 Integer types \<stdint.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index
   4/index


.. _9899_7.18p1:

.. container:: snum

   :ref:`1 <9899_7.18p1>`

The header :ref:`\<stdint.h> <9899_7.18>` declares sets of integer types having specified widths, and defines corresponding sets of macros.\ [#9899_note223]_ It also defines macros that specify limits of integer types corresponding to types defined in other standard headers.

.. _9899_7.18p2:

.. container:: snum

   :ref:`2 <9899_7.18p2>`

Types are defined in the following categories:

-  integer types having certain exact widths;
-  integer types having at least certain specified widths;
-  fastest integer types having at least certain specified widths;
-  integer types wide enough to hold pointers to objects;
-  integer types having greatest width.

(Some of these types may denote the same type.)

.. _9899_7.18p3:

.. container:: snum

   :ref:`3 <9899_7.18p3>`

Corresponding macros specify limits of the declared types and construct suitable constants.

.. _9899_7.18p4:

.. container:: snum

   :ref:`4 <9899_7.18p4>`

For each type described herein that the implementation provides,\ [#9899_note224]_ :ref:`\<stdint.h> <9899_7.18>` shall declare that typedef name and define the associated macros. Conversely, for each type described herein that the implementation does not provide, :ref:`\<stdint.h> <9899_7.18>` shall not declare that typedef name nor shall it define the associated macros. An implementation shall provide those types described as "required", but need not provide any of the others (described as "optional").




.. _9899_7.18.1:



.. rubric:: Footnotes

.. [#9899_note223] See "future library directions" (:ref:`7.26.8 <9899_7.26.8>`).
.. [#9899_note224] Some of these types may denote implementation-defined extended integer types.
