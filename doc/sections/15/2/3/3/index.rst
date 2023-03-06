.. _9899_H.2.3.3:

H.2.3.3 Rounding styles
'''''''''''''''''''''''

.. _9899_H.2.3.3p1:

.. container:: snum

   :ref:`1 <9899_H.2.3.3p1>`

The C Standard requires all floating types to use the same radix and rounding style, so that only one identifier for each is provided to map to LIA-1.

.. _9899_H.2.3.3p2:

.. container:: snum

   :ref:`2 <9899_H.2.3.3p2>`

The FLT_ROUNDS parameter can be used to indicate the LIA-1 rounding styles:

.. code-block:: text

    truncate      FLT_ROUNDS == 0

    nearest        FLT_ROUNDS == 1
    other          FLT_ROUNDS != 0 && FLT_ROUNDS != 1

provided that an implementation extends FLT_ROUNDS to cover the rounding style used in all relevant LIA-1 operations, not just addition as in C.

