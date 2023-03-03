.. _9899_J.3.11:

J.3.11 Preprocessing directives
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_J.3.11p1:

:ref:`1 <9899_J.3.11p1>`

-  The locations within #pragma directives where header name preprocessing tokens are recognized (:ref:`6.4 <9899_6.4>`, :ref:`6.4.7 <9899_6.4.7>`).
-  How sequences in both forms of header names are mapped to headers or external source file names (:ref:`6.4.7 <9899_6.4.7>`).
-  Whether the value of a character constant in a constant expression that controls conditional inclusion matches the value of the same character constant in the execution character set (:ref:`6.10.1 <9899_6.10.1>`).
-  Whether the value of a single-character character constant in a constant expression that controls conditional inclusion may have a negative value (:ref:`6.10.1 <9899_6.10.1>`).
-  The places that are searched for an included < > delimited header, and how the places are specified or the header is identified (:ref:`6.10.2 <9899_6.10.2>`).
-  How the named source file is searched for in an included " " delimited header (:ref:`6.10.2 <9899_6.10.2>`).
-  The method by which preprocessing tokens (possibly resulting from macro expansion) in a #include directive are combined into a header name (:ref:`6.10.2 <9899_6.10.2>`).
-  The nesting limit for #include processing (:ref:`6.10.2 <9899_6.10.2>`).
-  Whether the # operator inserts a \\ character before the \\ character that begins a universal character name in a character constant or string literal (:ref:`6.10.3.2 <9899_6.10.3.2>`).
-  The behavior on each recognized non-STDC #pragma directive (:ref:`6.10.6 <9899_6.10.6>`).
-  The definitions for \__DATE\_\_ and \__TIME\_\_ when respectively, the date and time of translation are not available (:ref:`6.10.8 <9899_6.10.8>`).

