.. _9899_H.2.3.1:

H.2.3.1 Floating-point parameters
'''''''''''''''''''''''''''''''''

.. _9899_H.2.3.1p1:

.. container:: snum

   :ref:`1 <9899_H.2.3.1p1>`

The parameters for a floating point data type can be accessed by the following:

.. code-block:: text

    r              FLT_RADIX
    p              FLT_MANT_DIG, DBL_MANT_DIG, LDBL_MANT_DIG
    emax           FLT_MAX_EXP, DBL_MAX_EXP, LDBL_MAX_EXP
    emin           FLT_MIN_EXP, DBL_MIN_EXP, LDBL_MIN_EXP

.. _9899_H.2.3.1p2:

.. container:: snum

   :ref:`2 <9899_H.2.3.1p2>`

The derived constants for the floating point types are accessed by the following:

.. code-block:: text

    fmax          FLT_MAX, DBL_MAX, LDBL_MAX
    fminN         FLT_MIN, DBL_MIN, LDBL_MIN
    epsilon       FLT_EPSILON, DBL_EPSILON, LDBL_EPSILON
    rnd_style     FLT_ROUNDS

