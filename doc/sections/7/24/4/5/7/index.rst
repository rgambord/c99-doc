.. _9899_7.24.4.5.7:

7.24.4.5.7 The wcstok function
""""""""""""""""""""""""""""""

.. rubric:: Synopsis

.. _9899_7.24.4.5.7p1:

.. container:: snum

   :ref:`1 <9899_7.24.4.5.7p1>`



::

    #include <wchar.h>
    wchar_t *wcstok(wchar_t * restrict s1,
         const wchar_t * restrict s2,
         wchar_t ** restrict ptr);

.. rubric:: Description

.. _9899_7.24.4.5.7p2:

.. container:: snum

   :ref:`2 <9899_7.24.4.5.7p2>`

A sequence of calls to the wcstok function breaks the wide string pointed to by s1 into a sequence of tokens, each of which is delimited by a wide character from the wide string pointed to by s2. The third argument points to a caller-provided wchar_t pointer into which the wcstok function stores information necessary for it to continue scanning the same wide string.

.. _9899_7.24.4.5.7p3:

.. container:: snum

   :ref:`3 <9899_7.24.4.5.7p3>`

The first call in a sequence has a non-null first argument and stores an initial value in the object pointed to by ptr. Subsequent calls in the sequence have a null first argument and the object pointed to by ptr is required to have the value stored by the previous call in the sequence, which is then updated. The separator wide string pointed to by s2 may be different from call to call.

.. _9899_7.24.4.5.7p4:

.. container:: snum

   :ref:`4 <9899_7.24.4.5.7p4>`

The first call in the sequence searches the wide string pointed to by s1 for the first wide character that is not contained in the current separator wide string pointed to by s2. If no such wide character is found, then there are no tokens in the wide string pointed to by s1 and the wcstok function returns a null pointer. If such a wide character is found, it is the start of the first token.

.. _9899_7.24.4.5.7p5:

.. container:: snum

   :ref:`5 <9899_7.24.4.5.7p5>`

The wcstok function then searches from there for a wide character that is contained in the current separator wide string. If no such wide character is found, the current token extends to the end of the wide string pointed to by s1, and subsequent searches in the same wide string for a token return a null pointer. If such a wide character is found, it is overwritten by a null wide character, which terminates the current token.

.. _9899_7.24.4.5.7p6:

.. container:: snum

   :ref:`6 <9899_7.24.4.5.7p6>`

In all cases, the wcstok function stores sufficient information in the pointer pointed to by ptr so that subsequent calls, with a null pointer for s1 and the unmodified pointer value for ptr, shall start searching just past the element overwritten by a null wide character (if any).

.. rubric:: Returns

.. _9899_7.24.4.5.7p7:

.. container:: snum

   :ref:`7 <9899_7.24.4.5.7p7>`

The wcstok function returns a pointer to the first wide character of a token, or a null pointer if there is no token.

.. _9899_7.24.4.5.7p8:

.. container:: snum

   :ref:`8 <9899_7.24.4.5.7p8>`

EXAMPLE

::

    #include <wchar.h>
    static wchar_t str1[] = L"?a???b,,,#c";
    static wchar_t str2[] = L"\t \t";
    wchar_t *t, *ptr1, *ptr2;
    t   =   wcstok(str1,   L"?", &ptr1);          //   t   points to the token L"a"
    t   =   wcstok(NULL,   L",", &ptr1);          //   t   points to the token L"??b"
    t   =   wcstok(str2,   L" \t", &ptr2);        //   t   is a null pointer
    t   =   wcstok(NULL,   L"#,", &ptr1);         //   t   points to the token L"c"
    t   =   wcstok(NULL,   L"?", &ptr1);          //   t   is a null pointer

