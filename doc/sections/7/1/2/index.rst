.. _9899_7.1.2:

7.1.2 Standard headers
^^^^^^^^^^^^^^^^^^^^^^

.. _9899_7.1.2p1:

:ref:`1 <9899_7.1.2p1>` Each library function is declared, with a type that includes a prototype, in a header,\ [#9899_note159]_ whose contents are made available by the #include preprocessing directive. The header declares a set of related functions, plus any necessary types and additional macros needed to facilitate their use. Declarations of types described in this clause shall not include type qualifiers, unless explicitly stated otherwise.

.. _9899_7.1.2p2:

:ref:`2 <9899_7.1.2p2>` The standard headers are

.. code-block:: text

    <assert.h>             <inttypes.h>            <signal.h>              <stdlib.h>
    <complex.h>            <iso646.h>              <stdarg.h>              <string.h>
    <ctype.h>              <limits.h>              <stdbool.h>             <tgmath.h>
    <errno.h>              <locale.h>              <stddef.h>              <time.h>
    <fenv.h>               <math.h>                <stdint.h>              <wchar.h>
    <float.h>              <setjmp.h>              <stdio.h>               <wctype.h>

.. _9899_7.1.2p3:

:ref:`3 <9899_7.1.2p3>` If a file with the same name as one of the above < and > delimited sequences, not provided as part of the implementation, is placed in any of the standard places that are searched for included source files, the behavior is undefined.

.. _9899_7.1.2p4:

:ref:`4 <9899_7.1.2p4>` Standard headers may be included in any order; each may be included more than once in a given scope, with no effect different from being included only once, except that the effect of including :ref:`\<assert.h> <9899_7.2>` depends on the definition of NDEBUG (see :ref:`7.2 <9899_7.2>`). If used, a header shall be included outside of any external declaration or definition, and it shall first be included before the first reference to any of the functions or objects it declares, or to any of the types or macros it defines. However, if an identifier is declared or defined in more than one header, the second and subsequent associated headers may be included after the initial reference to the identifier. The program shall not have any macros with names lexically identical to keywords currently defined prior to the inclusion.

.. _9899_7.1.2p5:

:ref:`5 <9899_7.1.2p5>` Any definition of an object-like macro described in this clause shall expand to code that is fully protected by parentheses where necessary, so that it groups in an arbitrary expression as if it were a single identifier.

.. _9899_7.1.2p6:

:ref:`6 <9899_7.1.2p6>` Any declaration of a library function shall have external linkage.

.. _9899_7.1.2p7:

:ref:`7 <9899_7.1.2p7>` A summary of the contents of the standard headers is given in :ref:`annex B <9899_B>`.

**Forward references**: diagnostics (:ref:`7.2 <9899_7.2>`).





.. rubric:: Footnotes

.. [#9899_note159] A header is not necessarily a source file, nor are the < and > delimited sequences in header names necessarily valid source file names.
