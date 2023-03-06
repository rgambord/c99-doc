.. _9899_J.3.9:

J.3.9 Structures, unions, enumerations, and bit-fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_J.3.9p1:

.. container:: snum

   :ref:`1 <9899_J.3.9p1>`



-  Whether a "plain" int bit-field is treated as a signed int bit-field or as an unsigned int bit-field (:ref:`6.7.2 <9899_6.7.2>`, :ref:`6.7.2.1 <9899_6.7.2.1>`).
-  Allowable bit-field types other than \_Bool, signed int, and unsigned int (:ref:`6.7.2.1 <9899_6.7.2.1>`).
-  Whether a bit-field can straddle a storage-unit boundary (:ref:`6.7.2.1 <9899_6.7.2.1>`).
-  The order of allocation of bit-fields within a unit (:ref:`6.7.2.1 <9899_6.7.2.1>`).
-  The alignment of non-bit-field members of structures (:ref:`6.7.2.1 <9899_6.7.2.1>`). This should present no problem unless binary data written by one implementation is read by another.
-  The integer type compatible with each enumerated type (:ref:`6.7.2.2 <9899_6.7.2.2>`).

