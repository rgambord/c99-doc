.. _9899_7.20:

7.20 General utilities \<stdlib.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. toctree::
   :maxdepth: 2

   1/index
   2/index
   3/index
   4/index
   5/index
   6/index
   7/index
   8/index


.. _9899_7.20p1:

:ref:`1 <9899_7.20p1>` The header :ref:`\<stdlib.h> <9899_7.20>` declares five types and several functions of general utility, and defines several macros.\ [#9899_note257]_

.. _9899_7.20p2:

:ref:`2 <9899_7.20p2>` The types declared are size_t and wchar_t (both described in :ref:`7.17 <9899_7.17>`),

::

    div_t

which is a structure type that is the type of the value returned by the div function,

::

    ldiv_t

which is a structure type that is the type of the value returned by the ldiv function, and

::

    lldiv_t

which is a structure type that is the type of the value returned by the lldiv function.

.. _9899_7.20p3:

:ref:`3 <9899_7.20p3>` The macros defined are NULL (described in :ref:`7.17 <9899_7.17>`);

::

    EXIT_FAILURE

and

::

    EXIT_SUCCESS

which expand to integer constant expressions that can be used as the argument to the exit function to return unsuccessful or successful termination status, respectively, to the host environment;

::

    RAND_MAX

which expands to an integer constant expression that is the maximum value returned by the rand function; and

::

    MB_CUR_MAX

which expands to a positive integer expression with type size_t that is the maximum number of bytes in a multibyte character for the extended character set specified by the current locale (category LC_CTYPE), which is never greater than MB_LEN_MAX.





.. rubric:: Footnotes

.. [#9899_note257] See ''future library directions'' (:ref:`7.26.10 <9899_7.26.10>`).
