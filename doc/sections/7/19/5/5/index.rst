.. _9899_7.19.5.5:

7.19.5.5 The setbuf function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.19.5.5p1:

:ref:`1 <9899_7.19.5.5p1>`

::

    #include <stdio.h>
    void setbuf(FILE * restrict stream,
         char * restrict buf);

.. rubric:: Description

.. _9899_7.19.5.5p2:

:ref:`2 <9899_7.19.5.5p2>` Except that it returns no value, the setbuf function is equivalent to the setvbuf function invoked with the values \_IOFBF for mode and BUFSIZ for size, or (if buf is a null pointer), with the value \_IONBF for mode.

.. rubric:: Returns

.. _9899_7.19.5.5p3:

:ref:`3 <9899_7.19.5.5p3>` The setbuf function returns no value.

**Forward references**: the setvbuf function (:ref:`7.19.5.6 <9899_7.19.5.6>`).

