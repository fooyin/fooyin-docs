Regular Expressions
===================

Regular expressions match patterns in text. FooScript uses Qt/PCRE regular expression
syntax and provides functions for testing, extracting, collecting, and replacing
matches.

Quoting and escaping
--------------------

Quote regex patterns because characters such as parentheses, commas, and dollar
signs also have meaning in FooScript. Backslashes before ordinary characters are
preserved inside quotes, so regex tokens such as ``\d`` and replacement captures
such as ``\1`` can be written directly. Use ``\"`` for a literal quote and
``\\`` for a literal backslash.

For example, this pattern matches ``Track`` followed by a number:

.. code-block:: text

   "^Track \d+$"

Testing for a match
-------------------

``$regex_test(text,"pattern"[,flags])`` returns a true condition when the pattern
matches any part of the text. It is intended for conditions such as ``$if``:

.. code-block:: text

   $if($regex_test(%title%,"\blive\b",i),Live recording,Studio recording)

Matching is not anchored automatically. Use ``^`` and ``$`` when the whole input
must follow the pattern. An invalid pattern or unsupported flag tests false.

Extracting the first match
--------------------------

``$regex_match(text,"pattern"[,group[,flags]])`` returns the first matching text.
The optional group may be a capture number or name. The default group, ``0``,
returns the complete match.

.. code-block:: text

   $regex_match(Track 42,"Track (\d+)",1)

This returns ``42``. Named captures are also supported:

.. code-block:: text

   $regex_match(Track 42,"Track (?<number>\d+)",number)

To pass flags while returning the complete match, specify group ``0`` explicitly:

.. code-block:: text

   $regex_match(FOOYIN,"fooyin",0,i)

Extracting all matches
----------------------

``$regex_matches(text,"pattern",separator[,group[,flags]])`` returns every
non-overlapping match, joined by the supplied separator. Group selection works
the same way as for ``$regex_match``.

.. code-block:: text

   $regex_matches(A1 B22 C333,"([A-Z])(\d+)"," / ",2)

This returns ``1 / 22 / 333``.

Replacing matches
-----------------

``$regex_replace(text,"pattern",replacement[,flags])`` replaces every
non-overlapping match. Refer to captured groups in the replacement with ``\1``,
``\2``, etc.

.. code-block:: text

   $regex_replace(%title%,"Live","Acoustic")

For a title such as ``Example Song (Live)``, this produces
``Example Song (Acoustic)``.

A more advanced example can use a captured group to standardise featured artist
credits:

.. code-block:: text

   $regex_replace(%title%,"(?i)\s*\((?:feat\.?|ft\.?)\s+([^)]*)\)$"," [feat. \1]")

For a title such as ``Example Song (feat. Guest Artist)``, this produces
``Example Song [feat. Guest Artist]``. If the pattern does not match, the original
text is returned. An invalid pattern or unsupported flag returns an empty result.

Flags
-----

.. list-table::
   :widths: 15 85
   :header-rows: 1

   * - **Flag**
     - **Meaning**
   * - ``i``
     - Case-insensitive matching
   * - ``m``
     - Makes ``^`` and ``$`` match the start and end of each line
   * - ``s``
     - Allows ``.`` to match newline characters
   * - ``x``
     - Enables extended syntax, ignoring unescaped whitespace and allowing comments
   * - ``U``
     - Inverts greediness so quantifiers are lazy by default

Unicode character properties are always enabled. Inline modifiers supported by
Qt, such as ``(?i)``, may also be placed in the pattern.

There is no ``g`` flag. ``$regex_replace`` always replaces all matches,
``$regex_matches`` always collects all matches, and the test and singular match
functions stop after the first match.

Empty and invalid results
-------------------------

The extraction functions return an empty result when there is no match, a capture
did not participate, the requested group does not exist, or the pattern or flags
are invalid. Use ``$regex_test`` when an empty match must be distinguished from no
match.

Performance
-----------

Compiled patterns are cached per thread, so a fixed pattern used by every row in
a playlist is compiled once and then reused. Patterns generated from track data
may continually replace cache entries and should be avoided when a fixed pattern
can express the same operation.

Regular expressions run wherever their FooScript is evaluated. Sorting a large
playlist or rebuilding a library tree can therefore execute a pattern for every
track. Avoid unnecessarily complex expressions, especially nested ambiguous
quantifiers such as ``(.*)*``, and use ``$regex_test`` instead of extracting all
matches when only a yes-or-no result is needed.
