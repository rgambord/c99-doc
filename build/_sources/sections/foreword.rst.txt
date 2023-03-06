.. _9899_Foreword:

Foreword
---------

.. _9899_Forewordp1:

:ref:`1 <9899_Forewordp1>` ISO (the International Organization for Standardization) and IEC (the International Electrotechnical Commission) form the specialized system for worldwide standardization. National bodies that are member of ISO or IEC participate in the development of International Standards through technical committees established by the respective organization to deal with particular fields of technical activity. ISO and IEC technical committees collaborate in fields of mutual interest. Other international organizations, governmental and non-governmental, in liaison with ISO and IEC, also take part in the work.

.. _9899_Forewordp2:

:ref:`2 <9899_Forewordp2>` International Standards are drafted in accordance with the rules given in the ISO/IEC Directives, Part 3.

.. _9899_Forewordp3:

:ref:`3 <9899_Forewordp3>` In the field of information technology, ISO and IEC have established a joint technical committee, ISO/IEC JTC 1. Draft International Standards adopted by the joint technical committee are circulated to national bodies for voting. Publication as an International Standard requires approval by at least 75% of the national bodies casting a vote.

.. _9899_Forewordp4:

:ref:`4 <9899_Forewordp4>` International Standard ISO/IEC 9899 was prepared by Joint Technical Committee ISO/IEC JTC 1, Information technology, Subcommittee SC 22, Programming languages, their environments and system software interfaces. The Working Group responsible for this standard (WG 14) maintains a site on the World Wide Web at http://www.open-std.org/JTC1/SC22/WG14/ containing additional information relevant to this standard such as a Rationale for many of the decisions made during its preparation and a log of Defect Reports and Responses.

.. _9899_Forewordp5:

:ref:`5 <9899_Forewordp5>` This second edition cancels and replaces the first edition, ISO/IEC 9899:1990, as amended and corrected by ISO/IEC 9899/COR1:1994, ISO/IEC 9899/AMD1:1995, and ISO/IEC 9899/COR2:1996. Major changes from the previous edition include:

-  restricted character set support via digraphs and :ref:`\<iso646.h> <9899_7.9>` (originally specified in AMD1)
-  wide character library support in :ref:`\<wchar.h> <9899_7.24>` and :ref:`\<wctype.h> <9899_7.25>` (originally specified in AMD1)
-  more precise aliasing rules via effective type
-  restricted pointers
-  variable length arrays
-  flexible array members
-  static and type qualifiers in parameter array declarators
-  complex (and imaginary) support in :ref:`\<complex.h> <9899_7.3>`
-  type-generic math macros in :ref:`\<tgmath.h> <9899_7.22>`
-  the long long int type and library functions
-  increased minimum translation limits
-  additional floating-point characteristics in :ref:`\<float.h> <9899_7.7>`
-  remove implicit int
-  reliable integer division
-  universal character names (\\u and \\U)
-  extended identifiers
-  hexadecimal floating-point constants and %a and %A printf/scanf conversion specifiers
-  compound literals
-  designated initializers
-  // comments
-  extended integer types and library functions in :ref:`\<inttypes.h> <9899_7.8>` and :ref:`\<stdint.h> <9899_7.18>`
-  remove implicit function declaration
-  preprocessor arithmetic done in intmax_t/uintmax_t
-  mixed declarations and code
-  new block scopes for selection and iteration statements
-  integer constant type rules
-  integer promotion rules
-  macros with a variable number of arguments
-  the vscanf family of functions in :ref:`\<stdio.h> <9899_7.19>` and :ref:`\<wchar.h> <9899_7.24>`
-  additional math library functions in :ref:`\<math.h> <9899_7.12>`
-  treatment of error conditions by math library functions (math_errhandling)
-  floating-point environment access in :ref:`\<fenv.h> <9899_7.6>`
-  IEC 60559 (also known as IEC 559 or IEEE arithmetic) support
-  trailing comma allowed in enum declaration
-  %lf conversion specifier allowed in printf
-  inline functions
-  the snprintf family of functions in :ref:`\<stdio.h> <9899_7.19>`
-  boolean type in :ref:`\<stdbool.h> <9899_7.16>`
-  idempotent type qualifiers
-  empty macro arguments
-  new structure type compatibility rules (tag compatibility)
-  additional predefined macro names
-  \_Pragma preprocessing operator
-  standard pragmas
-  \__func\_\_ predefined identifier
-  va_copy macro
-  additional strftime conversion specifiers
-  LIA compatibility annex
-  deprecate ungetc at the beginning of a binary file
-  remove deprecation of aliased array parameters
-  conversion of array to pointer not limited to lvalues
-  relaxed constraints on aggregate and union initialization
-  relaxed restrictions on portable header names
-  return without expression not permitted in function that returns a value (and vice versa)

.. _9899_Forewordp6:

:ref:`6 <9899_Forewordp6>` Annexes D and F form a normative part of this standard; annexes A, B, C, E, G, H, I, J, the bibliography, and the index are for information only. In accordance with Part 3 of the ISO/IEC Directives, this foreword, the introduction, notes, footnotes, and examples are also for information only.
