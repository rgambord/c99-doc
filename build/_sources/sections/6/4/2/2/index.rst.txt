.. _9899_6.4.2.2:

6.4.2.2 Predefined identifiers
''''''''''''''''''''''''''''''

.. rubric:: Semantics

.. _9899_6.4.2.2p1:

.. container:: snum

   :ref:`1 <9899_6.4.2.2p1>`

The identifier \__func\_\_ shall be implicitly declared by the translator as if, immediately following the opening brace of each function definition, the declaration

::

    static const char __func__[] = "function-name";

appeared, where function-name is the name of the lexically-enclosing function.\ [#9899_note61]_

.. _9899_6.4.2.2p2:

.. container:: snum

   :ref:`2 <9899_6.4.2.2p2>`

This name is encoded as if the implicit declaration had been written in the source character set and then translated into the execution character set as indicated in translation phase 5.

.. _9899_6.4.2.2p3:

.. container:: snum

   :ref:`3 <9899_6.4.2.2p3>`

EXAMPLE Consider the code fragment:

::

    #include <stdio.h>
    void myfunc(void)
    {
          printf("%s\n", __func__);
          /* ... */
    }

Each time the function is called, it will print to the standard output stream:

.. code-block:: text

    myfunc

.. rubric:: Forward References

.. hlist::
   - :ref:`9899_6.9.1`





.. rubric:: Footnotes

.. [#9899_note61] Since the name \__func\_\_ is reserved for any use by the implementation (:ref:`7.1.3 <9899_7.1.3>`), if any other identifier is explicitly declared using the name \__func\_\_, the behavior is undefined.
