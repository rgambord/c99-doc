.. _9899_J.3.12:

J.3.12 Library functions
^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_J.3.12p1:

:ref:`1 <9899_J.3.12p1>`

-  Any library facilities available to a freestanding program, other than the minimal set required by clause 4 (:ref:`5.1.2.1 <9899_5.1.2.1>`).
-  The format of the diagnostic printed by the assert macro (:ref:`7.2.1.1 <9899_7.2.1.1>`).
-  The representation of the floating-point status flags stored by the fegetexceptflag function (:ref:`7.6.2.2 <9899_7.6.2.2>`).
-  Whether the feraiseexcept function raises the ''inexact'' floating-point exception in addition to the ''overflow'' or ''underflow'' floating-point exception (:ref:`7.6.2.3 <9899_7.6.2.3>`).
-  Strings other than "C" and "" that may be passed as the second argument to the setlocale function (:ref:`7.11.1.1 <9899_7.11.1.1>`).
-  The types defined for float_t and double_t when the value of the FLT_EVAL_METHOD macro is less than 0 (:ref:`7.12 <9899_7.12>`).
-  Domain errors for the mathematics functions, other than those required by this International Standard (:ref:`7.12.1 <9899_7.12.1>`).
-  The values returned by the mathematics functions on domain errors (:ref:`7.12.1 <9899_7.12.1>`).
-  The values returned by the mathematics functions on underflow range errors, whether errno is set to the value of the macro ERANGE when the integer expression math_errhandling & MATH_ERRNO is nonzero, and whether the ''underflow'' floating-point exception is raised when the integer expression math_errhandling & MATH_ERREXCEPT is nonzero. (:ref:`7.12.1 <9899_7.12.1>`).
-  Whether a domain error occurs or zero is returned when an fmod function has a second argument of zero (:ref:`7.12.10.1 <9899_7.12.10.1>`).
-  Whether a domain error occurs or zero is returned when a remainder function has a second argument of zero (:ref:`7.12.10.2 <9899_7.12.10.2>`).
-  The base-2 logarithm of the modulus used by the remquo functions in reducing the quotient (:ref:`7.12.10.3 <9899_7.12.10.3>`).
-  Whether a domain error occurs or zero is returned when a remquo function has a second argument of zero (:ref:`7.12.10.3 <9899_7.12.10.3>`).
-  Whether the equivalent of signal(sig, SIG_DFL); is executed prior to the call of a signal handler, and, if not, the blocking of signals that is performed (:ref:`7.14.1.1 <9899_7.14.1.1>`).
-  The null pointer constant to which the macro NULL expands (:ref:`7.17 <9899_7.17>`).
-  Whether the last line of a text stream requires a terminating new-line character (:ref:`7.19.2 <9899_7.19.2>`).
-  Whether space characters that are written out to a text stream immediately before a new-line character appear when read in (:ref:`7.19.2 <9899_7.19.2>`).
-  The number of null characters that may be appended to data written to a binary stream (:ref:`7.19.2 <9899_7.19.2>`).
-  Whether the file position indicator of an append-mode stream is initially positioned at the beginning or end of the file (:ref:`7.19.3 <9899_7.19.3>`).
-  Whether a write on a text stream causes the associated file to be truncated beyond that point (:ref:`7.19.3 <9899_7.19.3>`).
-  The characteristics of file buffering (:ref:`7.19.3 <9899_7.19.3>`).
-  Whether a zero-length file actually exists (:ref:`7.19.3 <9899_7.19.3>`).
-  The rules for composing valid file names (:ref:`7.19.3 <9899_7.19.3>`).
-  Whether the same file can be simultaneously open multiple times (:ref:`7.19.3 <9899_7.19.3>`).
-  The nature and choice of encodings used for multibyte characters in files (:ref:`7.19.3 <9899_7.19.3>`).
-  The effect of the remove function on an open file (:ref:`7.19.4.1 <9899_7.19.4.1>`).
-  The effect if a file with the new name exists prior to a call to the rename function (:ref:`7.19.4.2 <9899_7.19.4.2>`).
-  Whether an open temporary file is removed upon abnormal program termination (:ref:`7.19.4.3 <9899_7.19.4.3>`).
-  Which changes of mode are permitted (if any), and under what circumstances (:ref:`7.19.5.4 <9899_7.19.5.4>`).
-  The style used to print an infinity or NaN, and the meaning of any n-char or n-wchar sequence printed for a NaN (:ref:`7.19.6.1 <9899_7.19.6.1>`, :ref:`7.24.2.1 <9899_7.24.2.1>`).
-  The output for %p conversion in the fprintf or fwprintf function (:ref:`7.19.6.1 <9899_7.19.6.1>`, :ref:`7.24.2.1 <9899_7.24.2.1>`).
-  The interpretation of a - character that is neither the first nor the last character, nor the second where a ^ character is the first, in the scanlist for %[ conversion in the fscanf or fwscanf function (:ref:`7.19.6.2 <9899_7.19.6.2>`, :ref:`7.24.2.1 <9899_7.24.2.1>`).
-  The set of sequences matched by a %p conversion and the interpretation of the corresponding input item in the fscanf or fwscanf function (:ref:`7.19.6.2 <9899_7.19.6.2>`, :ref:`7.24.2.2 <9899_7.24.2.2>`).
-  The value to which the macro errno is set by the fgetpos, fsetpos, or ftell functions on failure (:ref:`7.19.9.1 <9899_7.19.9.1>`, :ref:`7.19.9.3 <9899_7.19.9.3>`, :ref:`7.19.9.4 <9899_7.19.9.4>`).
-  The meaning of any n-char or n-wchar sequence in a string representing a NaN that is converted by the strtod, strtof, strtold, wcstod, wcstof, or wcstold function (:ref:`7.20.1.3 <9899_7.20.1.3>`, :ref:`7.24.4.1.1 <9899_7.24.4.1.1>`).
-  Whether or not the strtod, strtof, strtold, wcstod, wcstof, or wcstold function sets errno to ERANGE when underflow occurs (:ref:`7.20.1.3 <9899_7.20.1.3>`, :ref:`7.24.4.1.1 <9899_7.24.4.1.1>`).
-  Whether the calloc, malloc, and realloc functions return a null pointer or a pointer to an allocated object when the size requested is zero (:ref:`7.20.3 <9899_7.20.3>`).
-  Whether open streams with unwritten buffered data are flushed, open streams are closed, or temporary files are removed when the abort or \_Exit function is called (:ref:`7.20.4.1 <9899_7.20.4.1>`, :ref:`7.20.4.4 <9899_7.20.4.4>`).
-  The termination status returned to the host environment by the abort, exit, or \_Exit function (:ref:`7.20.4.1 <9899_7.20.4.1>`, :ref:`7.20.4.3 <9899_7.20.4.3>`, :ref:`7.20.4.4 <9899_7.20.4.4>`).
-  The value returned by the system function when its argument is not a null pointer (:ref:`7.20.4.6 <9899_7.20.4.6>`).
-  The local time zone and Daylight Saving Time (:ref:`7.23.1 <9899_7.23.1>`).
-  The range and precision of times representable in clock_t and time_t (:ref:`7.23 <9899_7.23>`).
-  The era for the clock function (:ref:`7.23.2.1 <9899_7.23.2.1>`).
-  The replacement string for the %Z specifier to the strftime, and wcsftime functions in the "C" locale (:ref:`7.23.3.5 <9899_7.23.3.5>`, :ref:`7.24.5.1 <9899_7.24.5.1>`).
-  Whether the functions in :ref:`\<math.h> <9899_7.12>` honor the rounding direction mode in an IEC 60559 conformant implementation, unless explicitly specified otherwise (:ref:`F.9 <9899_F.9>`).

