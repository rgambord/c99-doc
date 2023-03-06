.. _9899_6.2.3:

6.2.3 Name spaces of identifiers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_6.2.3p1:

.. container:: snum

   :ref:`1 <9899_6.2.3p1>`

If more than one declaration of a particular identifier is visible at any point in a translation unit, the syntactic context disambiguates uses that refer to different entities. Thus, there are separate name spaces for various categories of identifiers, as follows:

-  label names (disambiguated by the syntax of the label declaration and use);
-  the tags of structures, unions, and enumerations (disambiguated by following any\ [#9899_note24]_ of the keywords struct, union, or enum);
-  the members of structures or unions; each structure or union has a separate name space for its members (disambiguated by the type of the expression used to access the member via the . or -> operator);
-  all other identifiers, called ordinary identifiers (declared in ordinary declarators or as enumeration constants).

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.7.2.2`
   - :ref:`9899_6.8.1`
   - :ref:`9899_6.7.2.1`
   - :ref:`9899_6.5.2.3`
   - :ref:`9899_6.7.2.3`
   - :ref:`9899_6.8.6.1`





.. rubric:: Footnotes

.. [#9899_note24] There is only one name space for tags even though three are possible.
