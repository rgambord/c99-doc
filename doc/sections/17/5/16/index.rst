.. _9899_J.5.16:

J.5.16 Defined file position indicator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _9899_J.5.16p1:

.. container:: snum

   :ref:`1 <9899_J.5.16p1>`

The file position indicator is decremented by each successful call to the ungetc or ungetwc function for a text stream, except if its value was zero before a call (:ref:`7.19.7.11 <9899_7.19.7.11>`, :ref:`7.24.3.10 <9899_7.24.3.10>`).

