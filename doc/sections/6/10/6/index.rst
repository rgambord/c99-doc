.. _9899_6.10.6:

6.10.6 Pragma directive
^^^^^^^^^^^^^^^^^^^^^^^

.. rubric:: Semantics

.. _9899_6.10.6p1:

:ref:`1 <9899_6.10.6p1>` A preprocessing directive of the form

.. code-block:: text

    # pragma pp-tokensopt new-line

where the preprocessing token STDC does not immediately follow pragma in the directive (prior to any macro replacement)\ [#9899_note152]_ causes the implementation to behave in an implementation-defined manner. The behavior might cause translation to fail or cause the translator or the resulting program to behave in a non-conforming manner. Any such pragma that is not recognized by the implementation is ignored.

.. _9899_6.10.6p2:

:ref:`2 <9899_6.10.6p2>` If the preprocessing token STDC does immediately follow pragma in the directive (prior to any macro replacement), then no macro replacement is performed on the directive, and the directive shall have one of the following forms\ [#9899_note153]_ whose meanings are described elsewhere:

::

    #pragma STDC FP_CONTRACT on-off-switch
    #pragma STDC FENV_ACCESS on-off-switch
    #pragma STDC CX_LIMITED_RANGE on-off-switch
    on-off-switch: one of
                ON     OFF           DEFAULT

**Forward references**: the FP_CONTRACT pragma (:ref:`7.12.2 <9899_7.12.2>`), the FENV_ACCESS pragma (:ref:`7.6.1 <9899_7.6.1>`), the CX_LIMITED_RANGE pragma (:ref:`7.3.4 <9899_7.3.4>`).






.. rubric:: Footnotes

.. [#9899_note152] An implementation is not required to perform macro replacement in pragmas, but it is permitted except for in standard pragmas (where STDC immediately follows pragma). If the result of macro replacement in a non-standard pragma has the same form as a standard pragma, the behavior is still implementation-defined; an implementation is permitted to behave as if it were the standard pragma, but is not required to.
.. [#9899_note153] See ''future language directions'' (:ref:`6.11.8 <9899_6.11.8>`).
