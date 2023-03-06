.. _9899_7.21.5.8:

7.21.5.8 The strtok function
''''''''''''''''''''''''''''

.. rubric:: Synopsis

.. _9899_7.21.5.8p1:

.. container:: snum

   :ref:`1 <9899_7.21.5.8p1>`



::

    #include <string.h>
    char *strtok(char * restrict s1,
         const char * restrict s2);

.. rubric:: Description

.. _9899_7.21.5.8p2:

.. container:: snum

   :ref:`2 <9899_7.21.5.8p2>`

A sequence of calls to the strtok function breaks the string pointed to by s1 into a sequence of tokens, each of which is delimited by a character from the string pointed to by s2. The first call in the sequence has a non-null first argument; subsequent calls in the sequence have a null first argument. The separator string pointed to by s2 may be different from call to call.

.. _9899_7.21.5.8p3:

.. container:: snum

   :ref:`3 <9899_7.21.5.8p3>`

The first call in the sequence searches the string pointed to by s1 for the first character that is not contained in the current separator string pointed to by s2. If no such character is found, then there are no tokens in the string pointed to by s1 and the strtok function returns a null pointer. If such a character is found, it is the start of the first token.

.. _9899_7.21.5.8p4:

.. container:: snum

   :ref:`4 <9899_7.21.5.8p4>`

The strtok function then searches from there for a character that is contained in the current separator string. If no such character is found, the current token extends to the end of the string pointed to by s1, and subsequent searches for a token will return a null pointer. If such a character is found, it is overwritten by a null character, which terminates the current token. The strtok function saves a pointer to the following character, from which the next search for a token will start.

.. _9899_7.21.5.8p5:

.. container:: snum

   :ref:`5 <9899_7.21.5.8p5>`

Each subsequent call, with a null pointer as the value of the first argument, starts searching from the saved pointer and behaves as described above.

.. _9899_7.21.5.8p6:

.. container:: snum

   :ref:`6 <9899_7.21.5.8p6>`

The implementation shall behave as if no library function calls the strtok function.

.. rubric:: Returns

.. _9899_7.21.5.8p7:

.. container:: snum

   :ref:`7 <9899_7.21.5.8p7>`

The strtok function returns a pointer to the first character of a token, or a null pointer if there is no token.

.. _9899_7.21.5.8p8:

.. container:: snum

   :ref:`8 <9899_7.21.5.8p8>`

EXAMPLE

::

    #include <string.h>
    static char str[] = "?a???b,,,#c";
    char *t;
    t   =   strtok(str, "?");       //   t   points to the token "a"
    t   =   strtok(NULL, ",");      //   t   points to the token "??b"
    t   =   strtok(NULL, "#,");     //   t   points to the token "c"
    t   =   strtok(NULL, "?");      //   t   is a null pointer

