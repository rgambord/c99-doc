.. _9899_4:

4. Conformance
--------------

.. _9899_4p1:

:ref:`1 <9899_4p1>` In this International Standard, ''shall'' is to be interpreted as a requirement on an implementation or on a program; conversely, ''shall not'' is to be interpreted as a prohibition.

.. _9899_4p2:

:ref:`2 <9899_4p2>` If a ''shall'' or ''shall not'' requirement that appears outside of a constraint is violated, the behavior is undefined. Undefined behavior is otherwise indicated in this International Standard by the words ''undefined behavior'' or by the omission of any explicit definition of behavior. There is no difference in emphasis among these three; they all describe ''behavior that is undefined''.

.. _9899_4p3:

:ref:`3 <9899_4p3>` A program that is correct in all other aspects, operating on correct data, containing unspecified behavior shall be a correct program and act in accordance with :ref:`5.1.2.3 <9899_5.1.2.3>`.

.. _9899_4p4:

:ref:`4 <9899_4p4>` The implementation shall not successfully translate a preprocessing translation unit containing a #error preprocessing directive unless it is part of a group skipped by conditional inclusion.

.. _9899_4p5:

:ref:`5 <9899_4p5>` A strictly conforming program shall use only those features of the language and library specified in this International Standard.\ [#9899_note2]_ It shall not produce output dependent on any unspecified, undefined, or implementation-defined behavior, and shall not exceed any minimum implementation limit.

.. _9899_4p6:

:ref:`6 <9899_4p6>` The two forms of conforming implementation are hosted and freestanding. A conforming hosted implementation shall accept any strictly conforming program. A conforming freestanding implementation shall accept any strictly conforming program that does not use complex types and in which the use of the features specified in the library clause (clause 7) is confined to the contents of the standard headers :ref:`\<float.h> <9899_7.7>`, :ref:`\<iso646.h> <9899_7.9>`, :ref:`\<limits.h> <9899_7.10>`, :ref:`\<stdarg.h> <9899_7.15>`, :ref:`\<stdbool.h> <9899_7.16>`, :ref:`\<stddef.h> <9899_7.17>`, and :ref:`\<stdint.h> <9899_7.18>`. A conforming implementation may have extensions (including additional library functions), provided they do not alter the behavior of any strictly conforming program.\ [#9899_note3]_

.. _9899_4p7:

:ref:`7 <9899_4p7>` A conforming program is one that is acceptable to a conforming implementation.\ [#9899_note4]_

.. _9899_4p8:

:ref:`8 <9899_4p8>` An implementation shall be accompanied by a document that defines all implementation- defined and locale-specific characteristics and all extensions.

**Forward references**: conditional inclusion (:ref:`6.10.1 <9899_6.10.1>`), error directive (:ref:`6.10.5 <9899_6.10.5>`), characteristics of floating types :ref:`\<float.h> <9899_7.7>` (:ref:`7.7 <9899_7.7>`), alternative spellings :ref:`\<iso646.h> <9899_7.9>` (:ref:`7.9 <9899_7.9>`), sizes of integer types :ref:`\<limits.h> <9899_7.10>` (:ref:`7.10 <9899_7.10>`), variable arguments :ref:`\<stdarg.h> <9899_7.15>` (:ref:`7.15 <9899_7.15>`), boolean type and values :ref:`\<stdbool.h> <9899_7.16>` (:ref:`7.16 <9899_7.16>`), common definitions :ref:`\<stddef.h> <9899_7.17>` (:ref:`7.17 <9899_7.17>`), integer types :ref:`\<stdint.h> <9899_7.18>` (:ref:`7.18 <9899_7.18>`).



::

    #ifdef __STDC_IEC_559__ /* FE_UPWARD defined */
       /* ... */
       fesetround(FE_UPWARD);
       /* ... */
    #endif





.. rubric:: Footnotes

.. [#9899_note2] A strictly conforming program can use conditional features (such as those in :ref:`annex F <9899_F>`) provided the use is guarded by a #ifdef directive with the appropriate macro. For example:
.. [#9899_note3] This implies that a conforming implementation reserves no identifiers other than those explicitly reserved in this International Standard.
.. [#9899_note4] Strictly conforming programs are intended to be maximally portable among conforming implementations. Conforming programs may depend upon nonportable features of a conforming implementation.
