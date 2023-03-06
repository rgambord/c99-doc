.. _9899_7.2:

7.2 Diagnostics \<assert.h>
~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. toctree::
   :maxdepth: 2

   1/index


.. _9899_7.2p1:

.. container:: snum

   :ref:`1 <9899_7.2p1>`

The header :ref:`\<assert.h> <9899_7.2>` defines the assert macro and refers to another macro,

::

    NDEBUG

which is not defined by :ref:`\<assert.h> <9899_7.2>`. If NDEBUG is defined as a macro name at the point in the source file where :ref:`\<assert.h> <9899_7.2>` is included, the assert macro is defined simply as

::

    #define assert(ignore) ((void)0)

The assert macro is redefined according to the current state of NDEBUG each time that :ref:`\<assert.h> <9899_7.2>` is included.

.. _9899_7.2p2:

.. container:: snum

   :ref:`2 <9899_7.2p2>`

The assert macro shall be implemented as a macro, not as an actual function. If the macro definition is suppressed in order to access an actual function, the behavior is undefined.

