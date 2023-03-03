.. _9899_7.8:

7.8 Format conversion of integer types \<inttypes.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. toctree::
   :maxdepth: 2

   1/index
   2/index


.. _9899_7.8p1:

:ref:`1 <9899_7.8p1>` The header :ref:`\<inttypes.h> <9899_7.8>` includes the header :ref:`\<stdint.h> <9899_7.18>` and extends it with additional facilities provided by hosted implementations.

.. _9899_7.8p2:

:ref:`2 <9899_7.8p2>` It declares functions for manipulating greatest-width integers and converting numeric character strings to greatest-width integers, and it declares the type

::

    imaxdiv_t

which is a structure type that is the type of the value returned by the imaxdiv function. For each type declared in :ref:`\<stdint.h> <9899_7.18>`, it defines corresponding macros for conversion specifiers for use with the formatted input/output functions.\ [#9899_note190]_

**Forward references**: integer types :ref:`\<stdint.h> <9899_7.18>` (:ref:`7.18 <9899_7.18>`), formatted input/output functions (:ref:`7.19.6 <9899_7.19.6>`), formatted wide character input/output functions (:ref:`7.24.2 <9899_7.24.2>`).





.. rubric:: Footnotes

.. [#9899_note190] See ''future library directions'' (:ref:`7.26.4 <9899_7.26.4>`).
