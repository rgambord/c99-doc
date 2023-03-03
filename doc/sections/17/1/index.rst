.. _9899_J.1:

J.1 Unspecified behavior
~~~~~~~~~~~~~~~~~~~~~~~~

.. _9899_J.1p1:

:ref:`1 <9899_J.1p1>` The following are unspecified:

-  The manner and timing of static initialization (:ref:`5.1.2 <9899_5.1.2>`).
-  The termination status returned to the hosted environment if the return type of main is not compatible with int (:ref:`5.1.2.2.3 <9899_5.1.2.2.3>`).
-  The behavior of the display device if a printing character is written when the active position is at the final position of a line (:ref:`5.2.2 <9899_5.2.2>`).
-  The behavior of the display device if a backspace character is written when the active position is at the initial position of a line (:ref:`5.2.2 <9899_5.2.2>`).
-  The behavior of the display device if a horizontal tab character is written when the active position is at or past the last defined horizontal tabulation position (:ref:`5.2.2 <9899_5.2.2>`).
-  The behavior of the display device if a vertical tab character is written when the active position is at or past the last defined vertical tabulation position (:ref:`5.2.2 <9899_5.2.2>`).
-  How an extended source character that does not correspond to a universal character name counts toward the significant initial characters in an external identifier (:ref:`5.2.4.1 <9899_5.2.4.1>`).
-  Many aspects of the representations of types (:ref:`6.2.6 <9899_6.2.6>`).
-  The value of padding bytes when storing values in structures or unions (:ref:`6.2.6.1 <9899_6.2.6.1>`).
-  The value of a union member other than the last one stored into (:ref:`6.2.6.1 <9899_6.2.6.1>`).
-  The representation used when storing a value in an object that has more than one object representation for that value (:ref:`6.2.6.1 <9899_6.2.6.1>`).
-  The values of any padding bits in integer representations (:ref:`6.2.6.2 <9899_6.2.6.2>`).
-  Whether certain operators can generate negative zeros and whether a negative zero becomes a normal zero when stored in an object (:ref:`6.2.6.2 <9899_6.2.6.2>`).
-  Whether two string literals result in distinct arrays (:ref:`6.4.5 <9899_6.4.5>`).
-  The order in which subexpressions are evaluated and the order in which side effects take place, except as specified for the function-call (), &&, \|\|, ?:, and comma operators (:ref:`6.5 <9899_6.5>`).
-  The order in which the function designator, arguments, and subexpressions within the arguments are evaluated in a function call (:ref:`6.5.2.2 <9899_6.5.2.2>`).
-  The order of side effects among compound literal initialization list expressions (:ref:`6.5.2.5 <9899_6.5.2.5>`).
-  The order in which the operands of an assignment operator are evaluated (:ref:`6.5.16 <9899_6.5.16>`).
-  The alignment of the addressable storage unit allocated to hold a bit-field (:ref:`6.7.2.1 <9899_6.7.2.1>`).
-  Whether a call to an inline function uses the inline definition or the external definition of the function (:ref:`6.7.4 <9899_6.7.4>`).
-  Whether or not a size expression is evaluated when it is part of the operand of a sizeof operator and changing the value of the size expression would not affect the result of the operator (:ref:`6.7.5.2 <9899_6.7.5.2>`).
-  The order in which any side effects occur among the initialization list expressions in an initializer (:ref:`6.7.8 <9899_6.7.8>`).
-  The layout of storage for function parameters (:ref:`6.9.1 <9899_6.9.1>`).
-  When a fully expanded macro replacement list contains a function-like macro name as its last preprocessing token and the next preprocessing token from the source file is a (, and the fully expanded replacement of that macro ends with the name of the first macro and the next preprocessing token from the source file is again a (, whether that is considered a nested replacement (:ref:`6.10.3 <9899_6.10.3>`).
-  The order in which # and ## operations are evaluated during macro substitution (:ref:`6.10.3.2 <9899_6.10.3.2>`, :ref:`6.10.3.3 <9899_6.10.3.3>`).
-  Whether errno is a macro or an identifier with external linkage (:ref:`7.5 <9899_7.5>`).
-  The state of the floating-point status flags when execution passes from a part of the program translated with FENV_ACCESS ''off'' to a part translated with FENV_ACCESS ''on'' (:ref:`7.6.1 <9899_7.6.1>`).
-  The order in which feraiseexcept raises floating-point exceptions, except as stated in :ref:`F.7.6 <9899_F.7.6>` (:ref:`7.6.2.3 <9899_7.6.2.3>`).
-  Whether math_errhandling is a macro or an identifier with external linkage (:ref:`7.12 <9899_7.12>`).
-  The results of the frexp functions when the specified value is not a floating-point number (:ref:`7.12.6.4 <9899_7.12.6.4>`).
-  The numeric result of the ilogb functions when the correct value is outside the range of the return type (:ref:`7.12.6.5 <9899_7.12.6.5>`, :ref:`F.9.3.5 <9899_F.9.3.5>`).
-  The result of rounding when the value is out of range (:ref:`7.12.9.5 <9899_7.12.9.5>`, :ref:`7.12.9.7 <9899_7.12.9.7>`, :ref:`F.9.6.5 <9899_F.9.6.5>`).
-  The value stored by the remquo functions in the object pointed to by quo when y is zero (:ref:`7.12.10.3 <9899_7.12.10.3>`).
-  Whether setjmp is a macro or an identifier with external linkage (:ref:`7.13 <9899_7.13>`).
-  Whether va_copy and va_end are macros or identifiers with external linkage (:ref:`7.15.1 <9899_7.15.1>`).
-  The hexadecimal digit before the decimal point when a non-normalized floating-point number is printed with an a or A conversion specifier (:ref:`7.19.6.1 <9899_7.19.6.1>`, :ref:`7.24.2.1 <9899_7.24.2.1>`).
-  The value of the file position indicator after a successful call to the ungetc function for a text stream, or the ungetwc function for any stream, until all pushed-back characters are read or discarded (:ref:`7.19.7.11 <9899_7.19.7.11>`, :ref:`7.24.3.10 <9899_7.24.3.10>`).
-  The details of the value stored by the fgetpos function (:ref:`7.19.9.1 <9899_7.19.9.1>`).
-  The details of the value returned by the ftell function for a text stream (:ref:`7.19.9.4 <9899_7.19.9.4>`).
-  Whether the strtod, strtof, strtold, wcstod, wcstof, and wcstold functions convert a minus-signed sequence to a negative number directly or by negating the value resulting from converting the corresponding unsigned sequence (:ref:`7.20.1.3 <9899_7.20.1.3>`, :ref:`7.24.4.1.1 <9899_7.24.4.1.1>`).
-  The order and contiguity of storage allocated by successive calls to the calloc, malloc, and realloc functions (:ref:`7.20.3 <9899_7.20.3>`).
-  The amount of storage allocated by a successful call to the calloc, malloc, or realloc function when 0 bytes was requested (:ref:`7.20.3 <9899_7.20.3>`).
-  Which of two elements that compare as equal is matched by the bsearch function (:ref:`7.20.5.1 <9899_7.20.5.1>`).
-  The order of two elements that compare as equal in an array sorted by the qsort function (:ref:`7.20.5.2 <9899_7.20.5.2>`).
-  The encoding of the calendar time returned by the time function (:ref:`7.23.2.4 <9899_7.23.2.4>`).
-  The characters stored by the strftime or wcsftime function if any of the time values being converted is outside the normal range (:ref:`7.23.3.5 <9899_7.23.3.5>`, :ref:`7.24.5.1 <9899_7.24.5.1>`).
-  The conversion state after an encoding error occurs (:ref:`7.24.6.3.2 <9899_7.24.6.3.2>`, :ref:`7.24.6.3.3 <9899_7.24.6.3.3>`, :ref:`7.24.6.4.1 <9899_7.24.6.4.1>`, :ref:`7.24.6.4.2 <9899_7.24.6.4.2>`,
-  The resulting value when the ''invalid'' floating-point exception is raised during IEC 60559 floating to integer conversion (:ref:`F.4 <9899_F.4>`).
-  Whether conversion of non-integer IEC 60559 floating values to integer raises the ''inexact'' floating-point exception (:ref:`F.4 <9899_F.4>`).
-  Whether or when library functions in :ref:`\<math.h> <9899_7.12>` raise the ''inexact'' floating-point exception in an IEC 60559 conformant implementation (:ref:`F.9 <9899_F.9>`).
-  Whether or when library functions in :ref:`\<math.h> <9899_7.12>` raise an undeserved ''underflow'' floating-point exception in an IEC 60559 conformant implementation (:ref:`F.9 <9899_F.9>`).
-  The exponent value stored by frexp for a NaN or infinity (:ref:`F.9.3.4 <9899_F.9.3.4>`).
-  The numeric result returned by the lrint, llrint, lround, and llround functions if the rounded value is outside the range of the return type (:ref:`F.9.6.5 <9899_F.9.6.5>`, :ref:`F.9.6.7 <9899_F.9.6.7>`).
-  The sign of one part of the complex result of several math functions for certain exceptional values in IEC 60559 compatible implementations (:ref:`G.6.1.1 <9899_G.6.1.1>`, :ref:`G.6.2.2 <9899_G.6.2.2>`, :ref:`G.6.2.3 <9899_G.6.2.3>`, :ref:`G.6.2.4 <9899_G.6.2.4>`, :ref:`G.6.2.5 <9899_G.6.2.5>`, :ref:`G.6.2.6 <9899_G.6.2.6>`, :ref:`G.6.3.1 <9899_G.6.3.1>`, :ref:`G.6.4.2 <9899_G.6.4.2>`).

