.. _9899_7.24.6.3.1:

7.24.6.3.1 The mbrlen function
""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.6.3.1p1:

:ref:`1 <9899_7.24.6.3.1p1>`

::

    #include <wchar.h>
    size_t mbrlen(const char * restrict s,
         size_t n,
         mbstate_t * restrict ps);

.. rubric:: Description

.. _9899_7.24.6.3.1p2:

:ref:`2 <9899_7.24.6.3.1p2>` The mbrlen function is equivalent to the call:

::

    mbrtowc(NULL, s, n, ps != NULL ? ps : &internal)

where internal is the mbstate_t object for the mbrlen function, except that the expression designated by ps is evaluated only once.

.. rubric:: Returns

.. _9899_7.24.6.3.1p3:

:ref:`3 <9899_7.24.6.3.1p3>` The mbrlen function returns a value between zero and n, inclusive, (size_t)(-2), or (size_t)(-1).

**Forward references**: the mbrtowc function (:ref:`7.24.6.3.2 <9899_7.24.6.3.2>`).

