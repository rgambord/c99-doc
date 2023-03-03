.. _9899_7.8.1:

7.8.1 Macros for format specifiers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_7.8.1p1:

:ref:`1 <9899_7.8.1p1>` Each of the following object-like macros\ [#9899_note191]_ expands to a character string literal containing a conversion specifier, possibly modified by a length modifier, suitable for use within the format argument of a formatted input/output function when converting the corresponding integer type. These macro names have the general form of PRI (character string literals for the fprintf and fwprintf family) or SCN (character string literals for the fscanf and fwscanf family),\ [#9899_note192]_ followed by the conversion specifier, followed by a name corresponding to a similar type name in :ref:`7.18.1 <9899_7.18.1>`. In these names, N represents the width of the type as described in :ref:`7.18.1 <9899_7.18.1>`. For example, PRIdFAST32 can be used in a format string to print the value of an integer of type int_fast32_t.

.. _9899_7.8.1p2:

:ref:`2 <9899_7.8.1p2>` The fprintf macros for signed integers are:

::

    PRIdN             PRIdLEASTN                PRIdFASTN          PRIdMAX             PRIdPTR
    PRIiN             PRIiLEASTN                PRIiFASTN          PRIiMAX             PRIiPTR

.. _9899_7.8.1p3:

:ref:`3 <9899_7.8.1p3>` The fprintf macros for unsigned integers are:

::

    PRIoN           PRIoLEASTN               PRIoFASTN              PRIoMAX             PRIoPTR
    PRIuN           PRIuLEASTN               PRIuFASTN              PRIuMAX             PRIuPTR
    PRIxN           PRIxLEASTN               PRIxFASTN              PRIxMAX             PRIxPTR
    PRIXN           PRIXLEASTN               PRIXFASTN              PRIXMAX             PRIXPTR

.. _9899_7.8.1p4:

:ref:`4 <9899_7.8.1p4>` The fscanf macros for signed integers are:

::

    SCNdN           SCNdLEASTN               SCNdFASTN              SCNdMAX             SCNdPTR
    SCNiN           SCNiLEASTN               SCNiFASTN              SCNiMAX             SCNiPTR

.. _9899_7.8.1p5:

:ref:`5 <9899_7.8.1p5>` The fscanf macros for unsigned integers are:

::

    SCNoN           SCNoLEASTN               SCNoFASTN              SCNoMAX             SCNoPTR
    SCNuN           SCNuLEASTN               SCNuFASTN              SCNuMAX             SCNuPTR
    SCNxN           SCNxLEASTN               SCNxFASTN              SCNxMAX             SCNxPTR

.. _9899_7.8.1p6:

:ref:`6 <9899_7.8.1p6>` For each type that the implementation provides in :ref:`\<stdint.h> <9899_7.18>`, the corresponding fprintf macros shall be defined and the corresponding fscanf macros shall be defined unless the implementation does not have a suitable fscanf length modifier for the type.

.. _9899_7.8.1p7:

:ref:`7 <9899_7.8.1p7>` EXAMPLE

::

    #include <inttypes.h>
    #include <wchar.h>
    int main(void)
    {
          uintmax_t i = UINTMAX_MAX;    // this type always exists
          wprintf(L"The largest integer value is %020"
                PRIxMAX "\n", i);
          return 0;
    }






.. rubric:: Footnotes

.. [#9899_note191] C++ implementations should define these macros only when \__STDC_FORMAT_MACROS is defined before :ref:`\<inttypes.h> <9899_7.8>` is included.
.. [#9899_note192] Separate macros are given for use with fprintf and fscanf functions because, in the general case, different format specifiers may be required for fprintf and fscanf, even when the type is the same.
