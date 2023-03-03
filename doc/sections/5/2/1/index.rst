.. _9899_5.2.1:

5.2.1 Character sets
^^^^^^^^^^^^^^^^^^^^


.. toctree::
   :maxdepth: 2

   1/index
   2/index


.. _9899_5.2.1p1:

:ref:`1 <9899_5.2.1p1>` Two sets of characters and their associated collating sequences shall be defined: the set in which source files are written (the source character set), and the set interpreted in the execution environment (the execution character set). Each set is further divided into a basic character set, whose contents are given by this subclause, and a set of zero or more locale-specific members (which are not members of the basic character set) called extended characters. The combined set is also called the extended character set. The values of the members of the execution character set are implementation-defined.

.. _9899_5.2.1p2:

:ref:`2 <9899_5.2.1p2>` In a character constant or string literal, members of the execution character set shall be represented by corresponding members of the source character set or by escape sequences consisting of the backslash \\ followed by one or more characters. A byte with all bits set to 0, called the null character, shall exist in the basic execution character set; it is used to terminate a character string.

.. _9899_5.2.1p3:

:ref:`3 <9899_5.2.1p3>` Both the basic source and basic execution character sets shall have the following members: the 26 uppercase letters of the Latin alphabet

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-rule

         .. container:: syntax-terminal

            A

         .. container:: syntax-terminal

            B

         .. container:: syntax-terminal

            C

         .. container:: syntax-terminal

            D

         .. container:: syntax-terminal

            E

         .. container:: syntax-terminal

            F

         .. container:: syntax-terminal

            G

         .. container:: syntax-terminal

            H

         .. container:: syntax-terminal

            I

         .. container:: syntax-terminal

            J

         .. container:: syntax-terminal

            K

         .. container:: syntax-terminal

            L

         .. container:: syntax-terminal

            M

      .. container:: syntax-rule

         .. container:: syntax-terminal

            N

         .. container:: syntax-terminal

            O

         .. container:: syntax-terminal

            P

         .. container:: syntax-terminal

            Q

         .. container:: syntax-terminal

            R

         .. container:: syntax-terminal

            S

         .. container:: syntax-terminal

            T

         .. container:: syntax-terminal

            U

         .. container:: syntax-terminal

            V

         .. container:: syntax-terminal

            W

         .. container:: syntax-terminal

            X

         .. container:: syntax-terminal

            Y

         .. container:: syntax-terminal

            Z



the 26 lowercase letters of the Latin alphabet


.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-rule

         .. container:: syntax-terminal

            a

         .. container:: syntax-terminal

            b

         .. container:: syntax-terminal

            c

         .. container:: syntax-terminal

            d

         .. container:: syntax-terminal

            e

         .. container:: syntax-terminal

            f

         .. container:: syntax-terminal

            g

         .. container:: syntax-terminal

            h

         .. container:: syntax-terminal

            i

         .. container:: syntax-terminal

            j

         .. container:: syntax-terminal

            k

         .. container:: syntax-terminal

            l

         .. container:: syntax-terminal

            m

      .. container:: syntax-rule

         .. container:: syntax-terminal

            n

         .. container:: syntax-terminal

            o

         .. container:: syntax-terminal

            p

         .. container:: syntax-terminal

            q

         .. container:: syntax-terminal

            r

         .. container:: syntax-terminal

            s

         .. container:: syntax-terminal

            t

         .. container:: syntax-terminal

            u

         .. container:: syntax-terminal

            v

         .. container:: syntax-terminal

            w

         .. container:: syntax-terminal

            x

         .. container:: syntax-terminal

            y

         .. container:: syntax-terminal

            z



the 10 decimal digits

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-rule

         .. container:: syntax-terminal

            0

         .. container:: syntax-terminal

            1

         .. container:: syntax-terminal

            2

         .. container:: syntax-terminal

            3

         .. container:: syntax-terminal

            4

         .. container:: syntax-terminal

            5

         .. container:: syntax-terminal

            6

         .. container:: syntax-terminal

            7

         .. container:: syntax-terminal

            8

         .. container:: syntax-terminal

            9



the following 29 graphic characters

.. container:: syntax-block

   .. container:: syntax-production

      .. container:: syntax-rule

         .. container:: syntax-terminal

            \!

         .. container:: syntax-terminal

            \"

         .. container:: syntax-terminal

            \#

         .. container:: syntax-terminal

            \%

         .. container:: syntax-terminal

            \&

         .. container:: syntax-terminal

            \'

         .. container:: syntax-terminal

            \(

         .. container:: syntax-terminal

            \)

         .. container:: syntax-terminal

            \*

         .. container:: syntax-terminal

            \+

         .. container:: syntax-terminal

            \,

         .. container:: syntax-terminal

            \-

         .. container:: syntax-terminal

            \.

         .. container:: syntax-terminal

            \/

         .. container:: syntax-terminal

            \:

      .. container:: syntax-rule

         .. container:: syntax-terminal

            \;

         .. container:: syntax-terminal

            \<

         .. container:: syntax-terminal

            \=

         .. container:: syntax-terminal

            \>

         .. container:: syntax-terminal

            \?

         .. container:: syntax-terminal

            \[

         .. container:: syntax-terminal

            \\

         .. container:: syntax-terminal

            \]

         .. container:: syntax-terminal

            \^

         .. container:: syntax-terminal

            \_

         .. container:: syntax-terminal

            \{

         .. container:: syntax-terminal

            \|

         .. container:: syntax-terminal

            \}

         .. container:: syntax-terminal

            \~

the space character, and control characters representing horizontal tab, vertical tab, and form feed. The representation of each member of the source and execution basic character sets shall fit in a byte. In both the source and execution basic character sets, the value of each character after 0 in the above list of decimal digits shall be one greater than the value of the previous. In source files, there shall be some way of indicating the end of each line of text; this International Standard treats such an end-of-line indicator as if it were a single new-line character. In the basic execution character set, there shall be control characters representing alert, backspace, carriage return, and new line. If any other characters are encountered in a source file (except in an identifier, a character constant, a string literal, a header name, a comment, or a preprocessing token that is never converted to a token), the behavior is undefined.

.. _9899_5.2.1p4:

:ref:`4 <9899_5.2.1p4>` A letter is an uppercase letter or a lowercase letter as defined above; in this International Standard the term does not include other characters that are letters in other alphabets.

.. _9899_5.2.1p5:

:ref:`5 <9899_5.2.1p5>` The universal character name construct provides a way to name other characters.

**Forward references**: universal character names (:ref:`6.4.3 <9899_6.4.3>`), character constants (:ref:`6.4.4.4 <9899_6.4.4.4>`), preprocessing directives (:ref:`6.10 <9899_6.10>`), string literals (:ref:`6.4.5 <9899_6.4.5>`), comments (:ref:`6.4.9 <9899_6.4.9>`), string (:ref:`7.1.1 <9899_7.1.1>`).

