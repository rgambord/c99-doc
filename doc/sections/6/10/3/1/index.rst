.. _9899_6.10.3.1:

6.10.3.1 Argument substitution
''''''''''''''''''''''''''''''

.. _9899_6.10.3.1p1:

.. container:: snum

   :ref:`1 <9899_6.10.3.1p1>`

After the arguments for the invocation of a function-like macro have been identified, argument substitution takes place. A parameter in the replacement list, unless preceded by a # or ## preprocessing token or followed by a ## preprocessing token (see below), is replaced by the corresponding argument after all macros contained therein have been expanded. Before being substituted, each argument's preprocessing tokens are completely macro replaced as if they formed the rest of the preprocessing file; no other preprocessing tokens are available.

.. _9899_6.10.3.1p2:

.. container:: snum

   :ref:`2 <9899_6.10.3.1p2>`

An identifier \__VA_ARGS\_\_ that occurs in the replacement list shall be treated as if it were a parameter, and the variable arguments shall form the preprocessing tokens used to replace it.

