.. _9899_G.2:

G.2 Types
~~~~~~~~~

.. _9899_G.2p1:

.. container:: snum

   :ref:`1 <9899_G.2p1>`

There is a new keyword \_Imaginary, which is used to specify imaginary types. It is used as a type specifier within declaration specifiers in the same way as \_Complex is (thus, \_Imaginary float is a valid type name).

.. _9899_G.2p2:

.. container:: snum

   :ref:`2 <9899_G.2p2>`

There are three imaginary types, designated as float \_Imaginary, double \_Imaginary, and long double \_Imaginary. The imaginary types (along with the real floating and complex types) are floating types.

.. _9899_G.2p3:

.. container:: snum

   :ref:`3 <9899_G.2p3>`

For imaginary types, the corresponding real type is given by deleting the keyword \_Imaginary from the type name.

.. _9899_G.2p4:

.. container:: snum

   :ref:`4 <9899_G.2p4>`

Each imaginary type has the same representation and alignment requirements as the corresponding real type. The value of an object of imaginary type is the value of the real representation times the imaginary unit.

.. _9899_G.2p5:

.. container:: snum

   :ref:`5 <9899_G.2p5>`

The imaginary type domain comprises the imaginary types.

