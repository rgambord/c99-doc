.. _9899_5.2.2:

5.2.2 Character display semantics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_5.2.2p1:

:ref:`1 <9899_5.2.2p1>` The active position is that location on a display device where the next character output by the fputc function would appear. The intent of writing a printing character (as defined by the isprint function) to a display device is to display a graphic representation of that character at the active position and then advance the active position to the next position on the current line. The direction of writing is locale-specific. If the active position is at the final position of a line (if there is one), the behavior of the display device is unspecified.

.. _9899_5.2.2p2:

:ref:`2 <9899_5.2.2p2>` Alphabetic escape sequences representing nongraphic characters in the execution character set are intended to produce actions on display devices as follows:

\\a
   (alert) Produces an audible or visible alert without changing the active position.
\\b
   (backspace) Moves the active position to the previous position on the current line. If the active position is at the initial position of a line, the behavior of the display device is unspecified.
\\f
   ( form feed) Moves the active position to the initial position at the start of the next logical page.
\\n
   (new line) Moves the active position to the initial position of the next line.
\\r
   (carriage return) Moves the active position to the initial position of the current line.
\\t
   (horizontal tab) Moves the active position to the next horizontal tabulation position on the current line. If the active position is at or past the last defined horizontal tabulation position, the behavior of the display device is unspecified.
\\v
   (vertical tab) Moves the active position to the initial position of the next vertical tabulation position. If the active position is at or past the last defined vertical tabulation position, the behavior of the display device is unspecified.

.. _9899_5.2.2p3:

:ref:`3 <9899_5.2.2p3>` Each of these escape sequences shall produce a unique implementation-defined value which can be stored in a single char object. The external representations in a text file need not be identical to the internal representations, and are outside the scope of this International Standard.

**Forward references**: the isprint function (:ref:`7.4.1.8 <9899_7.4.1.8>`), the fputc function (:ref:`7.19.7.3 <9899_7.19.7.3>`).

